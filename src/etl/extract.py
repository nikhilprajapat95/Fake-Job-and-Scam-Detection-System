import os
import pandas as pd

class Extract:
    def __init__(self, data_path):
        self.data_path = data_path

    def extract_files(self):
        dataframes = []

        for file in os.listdir(self.data_path):
            file_path = os.path.join(self.data_path, file)

            if file.endswith(".csv"):
                df = pd.read_csv(file_path)
            elif file.endswith((".xlsx", ".xls")):
                df = pd.read_excel(file_path)
            else:
                continue

            df["source"] = file
            dataframes.append(df)

        return dataframes