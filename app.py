from flask import Flask, jsonify, request
from pony.orm import db_session, select
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
        {"Status": "Book Created"})

#Rota para Ler um livro de acordo com seu id
@app.route('/<string:id>', methods=['GET'])
@db_session
def get_byid(id):
    book = Livro.get(id=id)
    
    return jsonify(
        {"Status": "Response",
        "Id": book.id,
        "Name": book.name,
        "Author": book.author}
        )
    

#Rota para atualizar um livro de acordo com seu id.
@app.route('/<string:id>', methods=['PUT'])
@db_session
def update_byid(id):
    data = request.json
    name = data['name']
    author = data['author']
    book = Livro.get(id=id)
    
    book.name = name
    book.author = author

    return jsonify({
        "Status": "Book Updated"
    })

#Rota para deletar livro de acordo com seu id.
@app.route('/<string:id>', methods=['DELETE'])
@db_session
def delete_byid(id):
    book = Livro.get(id=id)
    book.delete()
    return jsonify({
        "Status": "Book Deleted"
    })


#Rota para retornar todos os livros do banco de dados.
@app.route('/', methods=['GET'])
@db_session
def get_allbooks():
    all_books = Livro.select()[:]
    livros_list = [{"id": str(livro.id), "name": livro.name, "author": livro.author} for livro in all_books]
    return jsonify(livros_list)
    



app.run(debug=True)



    
