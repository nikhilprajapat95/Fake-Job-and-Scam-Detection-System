import pickle
import numpy as np

from src.logging.logger import get_logger
from src.exception.exception import CustomException
import sys

logger = get_logger(__name__)

class PredictionPipeline:

    def __init__(self):
        try:
            with open("models/model.pkl", "rb") as f:
                self.model = pickle.load(f)

            with open("models/vectorizer.pkl", "rb") as f:
                self.vectorizer = pickle.load(f)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, text):
        try:
            logger.info("Prediction started")

            text_vector = self.vectorizer.transform([text]).toarray()

            prediction = self.model.predict(text_vector)[0]
            probability = self.model.predict_proba(text_vector)[0][1]

            return prediction, probability

        except Exception as e:
            raise CustomException(e, sys)