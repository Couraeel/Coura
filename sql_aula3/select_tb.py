import mysql.connector

conexao = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1',
                                     database = 'db_loja')
print('conexao',conexao)
cursor = conexao.cursor()

sql = '''SELECT * FROM tb_produtos'''  

cursor.execute(sql)

print('Registros inseridos:',cursor.rowcount)
print('cursor.statement',cursor.statement)

l_registros = cursor.fetchall()

#print(l_registros)

for registro in l_registros:
    print(registro)