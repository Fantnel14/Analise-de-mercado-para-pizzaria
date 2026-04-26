from modules.data_cleaner import DataCleaner
import pandas as pd

# Carregando dados brutos
dados_brutos = pd.read_csv("../data/raw/dados_brutos.csv")

# Limpando os dados
cleaner = DataCleaner(dados_brutos)
dados_limpos = cleaner.clean_data()

# Salvando os dados processados
dados_limpos.to_csv("../data/processed/dados_processados.csv", index=False)
print("Dados processados e salvos!")