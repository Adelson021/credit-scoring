import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin

# ---------------------------
# 1. Definir o transformer de remoção de outliers
# ---------------------------
class OutlierRemover(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=2.0):
        self.threshold = threshold

    def fit(self, X, y=None):
        self.limits_ = {}
        for col in X.select_dtypes(include=['number']).columns:
            Q1 = X[col].quantile(0.25)
            Q3 = X[col].quantile(0.75)
            IQR = Q3 - Q1
            lim_inf = Q1 - self.threshold * IQR
            lim_sup = Q3 + self.threshold * IQR
            self.limits_[col] = (lim_inf, lim_sup)
        return self

    def transform(self, X):
        X_out = X.copy()
        mask = np.ones(len(X_out), dtype=bool)
        for col, (lim_inf, lim_sup) in self.limits_.items():
            mask &= (X_out[col] >= lim_inf) & (X_out[col] <= lim_sup)

        X_filtered = X_out.loc[mask].reset_index(drop=True)

        # Se remover todos os dados, retorna os dados originais sem remoção de outliers
        if X_filtered.shape[0] == 0:
            print("⚠ Nenhuma amostra restante após remoção de outliers! Mantendo os dados originais...")
            return X_out.reset_index(drop=True)
        
        return X_filtered

# ---------------------------
# 2. Configurar as colunas para o pré-processamento
# ---------------------------
num_features = ['renda', 'idade', 'tempo_emprego', 'qtd_filhos', 'qt_pessoas_residencia']
cat_features = ['posse_de_veiculo', 'sexo', 'posse_de_imovel', 'tipo_renda', 'educacao', 'estado_civil', 'tipo_residencia']

# Pipeline para variáveis numéricas: imputação, escalonamento e PCA
num_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=3))
])

# Pipeline para variáveis categóricas: imputação e one-hot encoding
cat_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(drop='first', dtype=int))
])

# Combinar as transformações em um ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', num_transformer, num_features),
    ('cat', cat_transformer, cat_features)
])

# Pipeline completo: primeiro remove outliers, depois aplica as transformações
full_pipeline = Pipeline([
    ('outlier_removal', OutlierRemover()),
    ('preprocessor', preprocessor)
])

# ---------------------------
# 3. Função para carregar o modelo
# ---------------------------
@st.cache_data
def load_model():
    with open('../credit-scoring/model_final.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# ---------------------------
# 4. Função para carregar dados
# ---------------------------
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None

# ---------------------------
# 5. Interface do Streamlit
# ---------------------------
st.title("Predição com Modelo Treinado")

uploaded_file = st.file_uploader("Carregar arquivo CSV para previsão", type=["csv"])

if uploaded_file:
    # Carregar os dados
    df_novos = load_data(uploaded_file)

    # Converter datas para formato adequado (se existirem colunas de datas)
    for col in df_novos.select_dtypes(include=['object']):
        try:
            df_novos[col] = pd.to_datetime(df_novos[col])
        except:
            pass  # Se a conversão falhar, significa que não é uma data válida

    st.write("Dados carregados:")
    st.dataframe(df_novos.head())

    # Aplicar o pipeline para pré-processamento
    X_processed = full_pipeline.fit_transform(df_novos)

    # Carregar o modelo treinado
    model = load_model()

    # Fazer previsão
    predictions = model.predict(X_processed)

    # Exibir previsões corretamente
    st.write("Previsões do Modelo:")
    st.dataframe(pd.DataFrame(predictions.astype(str), columns=["Previsão"]))


