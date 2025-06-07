from flaskr import create_app
from flask_cors import CORS

app = create_app()
CORS(app, origins=["https://vercel-frontend-nine-dun.vercel.app/"])


