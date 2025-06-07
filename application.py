from flaskr import create_app
from flask_cors import CORS


CORS(app, origins=["https://vercel-frontend-nine-dun.vercel.app/"])
app = create_app()

