from flask import Flask
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager
from flask_cors import CORS
app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Teams'

app.config["JWT_SECRET_KEY"] = "yoyohoho"  # Change this!
jwt = JWTManager(app)

db = MySQL(app)