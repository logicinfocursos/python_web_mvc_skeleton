# app/controllers/main_controller.py
from flask import render_template
from app.models.main_model import MainModel

class MainController:
    def __init__(self, app):
        self.app = app
        self.model = MainModel()

  
    def index(self):
        data = self.model.get_data()
        return render_template('home/index.html', data=data)

   # Adicione este decorator
    def contact(self):
        return render_template('contact/contact.html', data='Contacts')
