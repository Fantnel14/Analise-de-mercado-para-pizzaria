import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column, bins=10, kde=True):
        """Gera um histograma para uma coluna específica."""
        if column in self.data.columns:
            sns.histplot(self.data[column], bins=bins, kde=kde)
            plt.title(f"Histograma de {column}")
            plt.xlabel(column)
            plt.ylabel("Frequência")
            plt.show()
        else:
            raise ValueError(f"Coluna '{column}' não encontrada nos dados.")