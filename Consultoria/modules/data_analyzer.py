import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_statistics(self):
        """Retorna estatísticas descritivas."""
        return self.data.describe()