# run.py
from flask import Flask
from app.routes import setup_routes

app = Flask(__name__, template_folder='app/views/templates', static_folder='app/static')

setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
