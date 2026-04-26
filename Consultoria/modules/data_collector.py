import requests
import pandas as pd

class DataCollector:
    def __init__(self, api_url=None, file_path=None):
        self.api_url = api_url
        self.file_path = file_path

    def from_api(self):
        """Coleta dados de uma API."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return pd.DataFrame(response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição: {e}")

    def from_file(self):
        """Coleta dados de um arquivo (CSV, Excel, etc.)."""
        try:
            if self.file_path.endswith('.csv'):
                return pd.read_csv(self.file_path)
            elif self.file_path.endswith('.xlsx'):
                return pd.read_excel(self.file_path)
            else:
                raise ValueError("Formato de arquivo não suportado.")
        except Exception as e:
            raise Exception(f"Erro ao ler o arquivo: {e}")