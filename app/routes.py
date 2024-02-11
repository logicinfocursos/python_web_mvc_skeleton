# app/routes.py
from app.controllers.main_controller import MainController
from app.controllers.products_controller import ProductsController
from app.controllers.error_controller import ErrorController


def setup_routes(app):

    main_controller = MainController(app)
    products_controller = ProductsController(app)
    error_controller = ErrorController(app)

    # Rota para listar as páginas home e demais páginas estáticas do projeto, contact, about, etc
    app.add_url_rule('/', 'index', main_controller.index)
    app.add_url_rule('/home', 'index', main_controller.index)
    app.add_url_rule('/contact', 'contact', main_controller.contact)
    
    # Rota para listar produtos
    app.add_url_rule('/products', 'list_products', products_controller.list_products)
     # Rota para mostrar detalhes do produto
    app.add_url_rule('/products/<product_id>', 'product_details', products_controller.product_details)

    # Adicione outras rotas conforme necessário

    # Rota para lidar com erro 404
    app.register_error_handler(404, error_controller.page_not_found)
