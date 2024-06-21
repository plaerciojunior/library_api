from flask import Flask
from schema.bd import db, livro

app = Flask(__name__)

@app.route('/', methods=['GET'])
@db_session
def get_all():
    
