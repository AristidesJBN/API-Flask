import mysql.connector
from flask import Flask, make_response, jsonify, request

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha123',
    database='dbpessoa'
)

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/pessoa', methods=['GET'])
def get_pessoa():

    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM pessoa')
    get_query = cursor.fetchall()

    dados_tratados = list()
    for pessoa in get_query:
        dados_tratados.append(
            {
                'id_pessoa': pessoa[0],
                'nome_pessoa': pessoa[1],
                'data_nascimento': pessoa[2]
            }
        )

    return make_response(
        jsonify(dados_tratados)
    )

@app.route('/pessoa', methods=['POST'])
def create_pessoa():    
    pessoa = request.json

    cursor = mydb.cursor()
    post_query = "INSERT INTO pessoa (nome_pessoa, data_nascimento) VALUES (%s, %s)"
    cursor.execute(post_query, (pessoa['nome_pessoa'], pessoa['data_nascimento']))
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='Usuário cadastrado!',
            pessoa=pessoa
        )
    )

app.run()