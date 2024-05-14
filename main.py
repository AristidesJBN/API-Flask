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

@app.route('/pessoa/<int:id_pessoa>', methods=['POST'])
def update_pessoa(id_pessoa):
    pessoa = request.json

    cursor = mydb.cursor()
    update_query = "UPDATE pessoa SET nome_pessoa = %s, data_nascimento = %s WHERE id_pessoa = %s"
    cursor.execute(update_query, (pessoa['nome_pessoa'], pessoa['data_nascimento'], id_pessoa))
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='Usuário atualizado!',
            pessoa=pessoa
        )
    )

@app.route('/pessoa/<int:id_pessoa>', methods=['DELETE'])
def delete_pessoa(id_pessoa):
    cursor = mydb.cursor()
    delete_query = "DELETE FROM pessoa WHERE id_pessoa = %s"
    cursor.execute(delete_query, (id_pessoa,))
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='Usuário excluído!'
        )
    )

app.run()