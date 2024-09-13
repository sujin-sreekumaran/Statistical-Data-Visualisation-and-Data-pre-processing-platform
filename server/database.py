from pymongo.mongo_client import MongoClient
from server.config import Config

uri = Config.MONGODB_URI

# Create a new client and connect to the server
client = MongoClient(uri)

# Initialize the database
db = client[Config.MONGODB_DB]

# Test the connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Function to get the database instance
def get_db():
    return db
