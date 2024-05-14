# API-Flask

CRUD "pessoa" | microserviços | API em Flask | Docker | DB

Como rodar o projeto:
- python -m venv .venv
- pip install flask
- $env:FLASK_APP = "main.py"
- pip install mysql-connector-python
- docker
- docker build -t nome_imagem-db .
- docker run -d -p 3306:3306 -e MYSQL_USER=usuario -e MYSQL_PASSWORD=senha123 -e MYSQL_DATABASE=dbpessoa -e MYSQL_ROOT_PASSWORD=senha123 nome_imagem-db
