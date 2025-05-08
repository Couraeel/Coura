import mysql.connector

def create_connection():
    con = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1')
                                     #database = '')
    print('Conexao:', con) #teste
    return con

def create_database():
    sql_create = "CREATE DATABASE if not exists db_loja_3"
    cursor.execute(sql_create)  #executa comando sql
    sql_use = "use db_loja_3"
    cursor.execute(sql_use)

def create_table():
    sql = '''
    CREATE TABLE IF NOT EXISTS tb_produtos (
    idt INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    preco DECIMAL(9,2) NOT NULL,
    data_val DATE,
    PRIMARY KEY (idt)
    )
    '''
    cursor.execute(sql)
    print("Conexão com o banco de dados fechada.")

def insert_table():
    sql = '''
    INSERT INTO tb_produtos (name, preco, data_val)
    VALUES (%s, %s, %s)
    '''
    dados = ('Produto 1', 10.00, '2023-10-01')
    cursor.execute(sql, dados)
    conexao.commit()  #confirma a inserção no banco de dados
    print('Dados inseridos com sucesso!')

if __name__ == '__main__':
    conexao = create_connection()
    cursor = conexao.cursor()
    create_database()
    create_table(cursor)
    insert_table(cursor,conexao)