from pony.orm import *
import uuid

db = Database() #Criando o banco de dados

#Criando as tabela Livro

class Livro(db.Entity):
    id = PrimaryKey(uuid.UUID, default=uuid.uuid4)
    name = Required(str, unique=True)
    author = Required(str)


#Conectando com o banco de dados 
db.bind(provider='sqlite', filename='database.sqlite', create_db=False)

#Mapeando/Criando tabela livro no banco de dados
db.generate_mapping(create_tables=True)