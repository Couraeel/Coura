import sqlite3

database = 'livrarias.db'
conexao = sqlite3.connect(database)
cur = conexao.cursor()

sql = '''create table tb_cliente(
    cpf text primary key,
    name text not null,
    age integer)'''

#sql = '''create table if not exist tb_cliente(
#    cpf text primary key,
#    name text not null,
#    age integer)'''

cur.execute(sql)
cur.close()
conexao.close()

print("Fechou a base de dados")