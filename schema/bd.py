from pony.orm import *

db = Database() #Criando o banco de dados

#Criando as tabela Livro

class livro(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    author = Required(str)


#Conectando com o banco de dados 
db.bind(provider='sqlite', filename='libray.sqlite', create_db=False)

#Mapeando/Criando tabela livro no banco de dados
db.generate_mapping(create_tables=True)