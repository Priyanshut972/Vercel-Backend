from flaskr import create_app
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://vercel-frontend-nine-dun.vercel.app/"])


