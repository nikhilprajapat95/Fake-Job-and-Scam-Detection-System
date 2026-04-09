from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.logging.logger import get_logger
from src.exception.exception import CustomException
import sys

logger = get_logger(__name__)

class ModelEvaluation:

    def evaluate(self, model, X_test, y_test):
        try:
            logger.info("Model evaluation started")

            y_pred = model.predict(X_test)

            metrics = {
                "accuracy": accuracy_score(y_test, y_pred),
                "precision": precision_score(y_test, y_pred),
                "recall": recall_score(y_test, y_pred),
                "f1_score": f1_score(y_test, y_pred)
            }

            logger.info(f"Evaluation: {metrics}")

            return metrics

        except Exception as e:
            raise CustomException(e, sys)