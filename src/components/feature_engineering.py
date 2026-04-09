from sklearn.feature_extraction.text import TfidfVectorizer
from src.logging.logger import get_logger
from src.exception.exception import CustomException
import sys

logger = get_logger(__name__)

class FeatureEngineering:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)

    def transform(self, df, fit=True):
        try:
            logger.info("Feature engineering started")

            if fit:
                X = self.vectorizer.fit_transform(df["text"]).toarray()
            else:
                X = self.vectorizer.transform(df["text"]).toarray()

            y = df["target"]

            logger.info("Feature engineering completed")

            return X, y

        except Exception as e:
            raise CustomException(e, sys)