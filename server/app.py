from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
from config import Config

print('>>>>>>>')
# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)
CORS(app)

# MongoDB configuration
client = MongoClient(Config.MONGODB_URI)
db = client[Config.MONGODB_DB]

# JWT configuration
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = Config.JWT_EXPIRATION_DELTA

# Import and register blueprints
from api.auth import auth_bp
from api.upload import upload_bp

app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(upload_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=Config.PORT)