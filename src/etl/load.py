from src.database.mongo_connection import get_mongo_client

class Load:

    def load_to_mongo(self, data):
        client = get_mongo_client()

        db = client["fake_job_db"]
        collection = db["jobs"]

        collection.insert_many(data)

        print("Data loaded into MongoDB")