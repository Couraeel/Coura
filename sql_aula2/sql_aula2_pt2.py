import mysql.connector

conexao = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1',
                                     database = 'db_empresa')

print('conexao',conexao)
cursor = conexao.cursor()
sql = '''
CREATE TABLE IF NOT EXISTS tb_funcionario (
    idt INTEGER,
    name VARCHAR(46) NOT NULL,
    salario DECIMAL(9,2) NULL,
    PRIMARY KEY (idt)
)
'''
cursor.execute(sql)
cursor.close()
conexao.close()
print("Conexão com o banco de dados fechada.")