import mysql.connector

conexao = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1',
                                     database = 'db_loja')

print('conexao',conexao)
cursor = conexao.cursor()
"""sql = '''
CREATE TABLE IF NOT EXISTS tb_produtos (
    idt INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    preco DECIMAL(9,2) NULL,
    PRIMARY KEY (idt)
)
'''
"""
sql = '''
ALTER TABLE tb_produtos
CHANGE COLUMN data_validade data DATE NULL
'''

cursor.execute(sql)
cursor.close()
conexao.close()
print("Conexão com o banco de dados fechada.")