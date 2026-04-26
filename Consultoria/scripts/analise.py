from modules.data_analyzer import DataAnalyzer
from modules.visualizer import DataVisualizer
import pandas as pd

# Carregando dados processados
dados_processados = pd.read_csv("../data/processed/dados_processados.csv")

# Analisando os dados
analyzer = DataAnalyzer(dados_processados)
estatisticas = analyzer.get_statistics()

# Visualizando os dados
visualizer = DataVisualizer(dados_processados)
visualizer.plot_histogram(column="idade")  # Exemplo de visualização
print("Análise concluída!")