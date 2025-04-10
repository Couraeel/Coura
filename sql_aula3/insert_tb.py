import mysql.connector

conexao = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1',
                                     database = 'db_loja')
print('conexao',conexao)
cursor = conexao.cursor()

sql = '''insert into tb_produtos
    (name, preco, data_validade)
    values(%s,%s,%s)'''

data = ('Guilerme', 9999.00, '2000-01-01') 

#sql = '''DELETE FROM tb_produtos WHERE idt = 1'''

print('Registros inseridos:',cursor.rowcount)
print('cursor.statement',cursor.statement)

cursor.execute(sql,data)
conexao.commit()
cursor.close()
conexao.close()

print("Fechou a base de dados")