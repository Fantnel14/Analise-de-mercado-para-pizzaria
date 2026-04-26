class DataCleaner:
    def __init__(self, data):
        self.data = data

    def clean_data(self, columns_to_convert=None):
        """Realiza a limpeza dos dados."""
        # Remover valores nulos
        self.data = self.data.dropna()
        
        # Converter colunas para o tipo correto, se especificado
        if columns_to_convert:
            for column, dtype in columns_to_convert.items():
                if column in self.data.columns:
                    self.data[column] = self.data[column].astype(dtype)
        
        return self.data
