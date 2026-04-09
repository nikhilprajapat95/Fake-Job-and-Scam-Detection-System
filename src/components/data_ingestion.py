import pandas as pd
from src.database.mongo_connection import get_mongo_client
from src.logging.logger import get_logger
from src.exception.exception import CustomException
import sys

logger = get_logger(__name__)

class DataIngestion:

    def load_data(self):
        try:
            logger.info("Loading data from MongoDB")

            client = get_mongo_client()
            db = client["fake_job_db"]
            collection = db["jobs"]

            data = list(collection.find({}, {"_id": 0}))  # remove Mongo _id

            df = pd.DataFrame(data)

            logger.info(f"Data loaded with shape: {df.shape}")

            return df

        except Exception as e:
            raise CustomException(e, sys)