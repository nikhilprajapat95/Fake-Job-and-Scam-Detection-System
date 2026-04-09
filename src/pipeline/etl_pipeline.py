from src.etl.extract import Extract
from src.etl.transform import Transform
from src.etl.load import Load

class ETLPipeline:

    def run_pipeline(self, path):

        extractor = Extract(path)
        transformer = Transform()
        loader = Load()

        dfs = extractor.extract_files()
        transformed_data = transformer.transform_data(dfs)

        loader.load_to_mongo(transformed_data)

        print("🚀 ETL Pipeline Completed")