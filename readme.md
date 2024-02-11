## python web skeleton template
Iremos criar um esqueleto para iniciar os seus projetos web com python.

Para tanto usaremos o flask um framework (ou micro framework), leve mas bem seguro onde você instalará mais recursos a medida que o seu projeto for evoluindo.

Usaremos o visual code como IDE em ambiente windows.

O projeto usará o padrão <b>MVC</b>.

<hr/>

## criar o ambiente
(instruções para ambiente windows usando visual code e python 3)

#### instalações e configurações

###### 1. crie um ambiente virtual:
<pre>c:\python\jobs>python -m venv venv</pre>

###### 2. ativar o ambiente virtual:
<pre>c:\python\jobs>venv\Scripts\activate</pre>
observe que o seu prompt irá indicar que o ambiente virtural está ativo, você terá o texto (venv) sendo exibido:
<pre>(venv) c:\python\jobs></pre>

###### 3.instalar o flask
<pre>(venv) c:\python\jobs>pip install flask</pre>

###### 4. estrutura de pastas do projeto
<pre>
myapp/
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── main_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── main_model.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── templates/
│   │   │   ├── index.html
├── run.py
</pre>

###### 5. crie arquivos <pre>__init __.py</pre> 
inserir arquivos __init __.py vazios em todos os diretórios para torná-los pacotes Python.

#### preencher os diretórios

###### 6. preencha o arquivo <i><small>main_model.py</small></i>
<pre>class MainModel:
    def get_data(self):
        return "Hello from Model"
</pre>

###### 7. preencha o arquivo <i><small>index.html</small></i>dentro do diretório <i><small>views/templates/home</small></i>

~~~<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask MVC Example</title>
</head>
<body>
    <h1>{{ data }}</h1>
</body>
</html>
~~~
<p>a variável data que está entre {{data}} será preenchida através da função get_data()</p>

###### 8. preencha o arquivo <i><small> main_controller.py:</small></i>
<pre>from flask import render_template
from app.models.main_model import MainModel

class MainController:
    def __init__(self, app):
        self.app = app
        self.model = MainModel()

        @app.route('/')
        def index():
            data = self.model.get_data()
            return render_template('index.html', data=data)
</pre>

###### 9. preencha o arquivo <i><small>run.py:</small></i>
<pre>from flask import Flask
from app.controllers.main_controller import MainController

app = Flask(__name__, template_folder='app/views/templates')
MainController(app)

if __name__ == '__main__':
    app.run(debug=True)
</pre>

###### 10. execute o aplicativo:
<pre>(venv) c:\python\jobs>python run.py</pre>


###### 11. Abra o navegador e acesse 
<pre>http://127.0.0.1:5000/ </pre>

<strong>a sua aplicação estará em execução na porta 5000</strong>


## downloads, fontes e documentação
python: https://docs.python.org/3/
flask: https://flask.palletsprojects.com/en/3.0.x/

bootstrap: https://getbootstrap.com/docs/5.0/getting-started/introduction/
bootstrap cdn:
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>

## tutorials
https://www.youtube.com/watch?v=2eN51HrYl9A&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=7


### static folder (project assets)
por padrão o flask busca esses arquivos na pasta static, para definir o local da pasta static, altere a seguinte instrução no arquivo run.py:
<pre>app = Flask(__name__, template_folder='app/views/templates', static_folder='app/static')</pre>

se desejar inserir arquivos css/js que estão em app/static para usar em base.html:

~~~ 
 <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
 <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
~~~

para usar a tag img para apresentar imagens que estão em app/static:
~~~ 
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="loogo"> 
~~~
