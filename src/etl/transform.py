import re

class Transform:

    def clean_text(self, text):
        text = str(text).lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"[^a-zA-Z ]", " ", text)
        return text

    def get_text(self, row):
        return " ".join([str(v) for v in row.values if isinstance(v, str)])

    def detect_target(self, df):
        for col in df.columns:
            if any(x in col.lower() for x in ["fraud", "fake", "label"]):
                return col
        return None

    def transform_data(self, dfs):
        final_data = []

        for df in dfs:

            target_col = self.detect_target(df)

            for _, row in df.iterrows():

                text = self.get_text(row)
                text = self.clean_text(text)

                if target_col:
                    target = row[target_col]
                else:
                    target = -1

                final_data.append({
                    "text": text,
                    "target": target
                })

        return final_data