import sqlite3

conexao = sqlite3.connect('db_empresa.db')
cursor = conexao.cursor()

sql = '''insert into tb_funcionario
    (idt, name, salario)
    values('451', 'Lorena', 4500.00)'''


cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()

print("Fechou a base de dados")