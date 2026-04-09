import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from src.logging.logger import get_logger
from src.exception.exception import CustomException
import sys

nltk.download("stopwords")

logger = get_logger(__name__)

class DataCleaning:

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.stemmer = PorterStemmer()

    def clean_text(self, text):
        text = str(text).lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"[^a-zA-Z ]", " ", text)

        words = text.split()
        words = [w for w in words if w not in self.stop_words]
        words = [self.stemmer.stem(w) for w in words]

        return " ".join(words)

    def clean_data(self, df):
        try:
            logger.info("Cleaning data started")

            df = df.drop_duplicates()
            df = df.fillna("")

            df["text"] = df["text"].apply(self.clean_text)

            # Remove empty text
            df = df[df["text"].str.strip() != ""]

            logger.info("Cleaning completed")

            return df

        except Exception as e:
            raise CustomException(e, sys)