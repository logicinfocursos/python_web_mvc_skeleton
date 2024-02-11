# app/controllers/products_controller.py
from flask import render_template

class ProductsController:
    def __init__(self, app):
        self.app = app

    def list_products(self):
        # Lógica para listar produtos (ainda não implementada)
        return render_template('products/productList.html', data='List of Products')
    
    def product_details(self, product_id):
        # Lógica para obter detalhes do produto (ainda não implementada)
        return render_template('products/productDetails.html', data=product_id)
