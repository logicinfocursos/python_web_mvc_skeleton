from flask import render_template
from app.models.main_model import MainModel

class MainController:
    def __init__(self, app):
        self.app = app
        self.model = MainModel()

        @app.route('/')
        def index():
            data = self.model.get_data()
            return render_template('home/index.html', data=data)
