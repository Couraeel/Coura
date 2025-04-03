import mysql.connector

conexao_db = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1')
                                     #database = '')

print('conexao',conexao_db)
cursor = conexao_db.cursor()
sql= '''CREATE DATABASE if not exists db_empresa'''
cursor.execute(sql)
cursor.close()
conexao_db.close()
