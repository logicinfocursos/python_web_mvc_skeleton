from flask import Flask
from app.controllers.main_controller import MainController

app = Flask(__name__, template_folder='app/views/templates')
MainController(app)

if __name__ == '__main__':
    app.run(debug=True)
