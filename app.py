from flask import Flask, jsonify, request
from pony.orm import db_session
from schema.bd import db, Livro

app = Flask(__name__)

#Rota para criação do livro
@app.route('/', methods=['POST'])
@db_session
def create_book():
    data = request.json
    name = data['name']
    author = data['author']

    Livro(name=name, author=author)
    return jsonify(
        {"Status": "Created"})

#Rota para Ler um livro de acordo com seu id
@app.route('/<string:name2>', methods=['GET'])
@db_session
def get_byid(name2):
    book = Livro.get(id=name2)
    
    return jsonify(
        {"Status": "Response",
        "Id": book.id,
        "Name": book.name,
        "Author": book.author}
        )
    




app.run(debug=True)



    
