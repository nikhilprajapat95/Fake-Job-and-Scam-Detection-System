from src.components.data_ingestion import DataIngestion
from src.components.data_cleaning import DataCleaning
from src.components.feature_engineering import FeatureEngineering
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

from src.logging.logger import get_logger
from src.exception.exception import CustomException
import sys

logger = get_logger(__name__)

class TrainingPipeline:

    def run_pipeline(self):
        try:
            logger.info("🚀 Training Pipeline Started")

            # Step 1: Load data from MongoDB
            ingestion = DataIngestion()
            df = ingestion.load_data()

            # Step 2: Clean data
            cleaner = DataCleaning()
            df = cleaner.clean_data(df)

            # Step 3: Feature Engineering
            fe = FeatureEngineering()
            X, y = fe.transform(df, fit=True)

            # Step 4: Model Training
            trainer = ModelTrainer()
            model, X_test, y_test = trainer.train(X, y)

            # Step 5: Evaluation
            evaluator = ModelEvaluation()
            metrics = evaluator.evaluate(model, X_test, y_test)

            print("\n📊 Model Performance:")
            print(metrics)

            # Step 6: Save model + vectorizer
            trainer.save_model(model, fe.vectorizer)

            logger.info("✅ Training Pipeline Completed")

        except Exception as e:
            raise CustomException(e, sys)