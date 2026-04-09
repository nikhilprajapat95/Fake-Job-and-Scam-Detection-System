import pickle
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from src.logging.logger import get_logger
from src.exception.exception import CustomException
import sys

logger = get_logger(__name__)

class ModelTrainer:

    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)

    def train(self, X, y):
        try:
            logger.info("Model training started")

            # Remove unknown labels
            mask = y != -1
            X = X[mask]
            y = y[mask]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            self.model.fit(X_train, y_train)

            logger.info("Model training completed")

            return self.model, X_test, y_test

        except Exception as e:
            raise CustomException(e, sys)

    def save_model(self, model, vectorizer):
        try:
            os.makedirs("models", exist_ok=True)

            with open("models/model.pkl", "wb") as f:
                pickle.dump(model, f)

            with open("models/vectorizer.pkl", "wb") as f:
                pickle.dump(vectorizer, f)

            logger.info("Model saved successfully")

        except Exception as e:
            raise CustomException(e, sys)