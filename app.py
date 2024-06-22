from flask import Flask, jsonify, request
from pony.orm import db_session
from schema.bd import db, Livro

app = Flask(__name__)

#Rota para criação do livro
@app.route('/', methods=['POST'])
@db_session
def get_all():
    data = request.json
    name = data['name']
    author = data['author']

    Livro(name=name, author=author)
    return jsonify(
        {"Status": "Created"})

#Rota para Ler um livro de acordo com seu id


app.run(debug=True)



    
