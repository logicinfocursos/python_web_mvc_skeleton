# app/controllers/error_controller.py
from flask import render_template

class ErrorController:
    def __init__(self, app):
        self.app = app

    def page_not_found(self, e):
        return render_template('errors/404.html', data='A página que você está procurando não existe - 404!!!'), 404
