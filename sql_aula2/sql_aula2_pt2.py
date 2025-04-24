import mysql.connector

conexao = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1',
                                     database = 'db_loja')

print('conexao',conexao)
cursor = conexao.cursor()

search_selc = input("nome: ")

sql = '''SELECT CODIGO 
FROM produto
where nome = '{search_selec}'
'''

#sql = f'''delete 
#FROM produto
#where nome = '{search_selec}'
#'''


cursor.execute(sql)
print(cursor.fetchall())
cursor.close()
conexao.close()
print("Conexão com o banco de dados fechada.")
