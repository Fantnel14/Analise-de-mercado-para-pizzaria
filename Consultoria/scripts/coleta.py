from modules.data_collector import DataCollector

# Coletando dados de uma API
api_url = "https://api.exemplo.com/dados"
collector = DataCollector(api_url=api_url)
dados_brutos = collector.from_api()

# Salvando os dados brutos
dados_brutos.to_csv("../data/raw/dados_brutos.csv", index=False)
print("Dados brutos coletados e salvos!")