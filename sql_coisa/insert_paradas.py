import sqlite3

conexao = sqlite3.connect('livrarias.db')
cur = conexao.cursor()

sql = '''insert into tb_cliente
    (cpf, name, age)
    values('CAITVI', 'Lorena', 22)'''


cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()

print("Fechou a base de dados")