import mysql.connector

def create_connection():
    con = mysql.connector.connect(user = 'root',
                                     password = 'ceub123456',
                                     host = '127.0.0.1')
                                     #database = '')
    print('Conexao:', con) #teste
    return con

def create_database():
    sql_create = "CREATE DATABASE if not exists db_lolja"
    cursor.execute(sql_create)  #executa comando sql
    sql_use = "use db_lolja"
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

def create_table_func():
    sql = '''
    CREATE TABLE IF NOT EXISTS tb_funcionario (
    idt INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    salario DECIMAL(9,2) NOT NULL,
    nascimento DATE,
    depart_num int,
    PRIMARY KEY (idt),
    FOREIGN KEY (depart_num) REFERENCES tb_departamento(idt)
    )
    '''
    cursor.execute(sql)
    print("Conexão com o banco de dados fechada.")

def insert_table_func():
    sql = '''
    INSERT INTO tb_funcionario (name, salario, nascimento,depart_num)
    VALUES (%s, %s, %s, %s)
    '''
    # Garantir que o usuário insira exatamente 3 valores separados por espaço
    while True:
        inputs = input  ("Digite o nome, salario, data de nascimento e o departamento do funcionario: ").split()
        if len(inputs) == 4:
            break
        print("Entrada inválida. Por favor, insira exatamente 3 valores.")

    print(inputs)


    #dadosnome = (input('Digite o nome do funcionario: '))
    #dadossalario = (input('Digite o salario do funcionario: '))
    #dadosnasc = (input('Digite a data de nascimento do funcionario: '))
    #dadosdepart = (input('Digite o numero do departamento do funcionario: '))

    #dados = ('Saiko', 9.50, '2000-06-09',1)
    cursor.execute(sql, inputs)
    conexao.commit()  #confirma a inserção no banco de dados
    print('Dados inseridos com sucesso!')


def create_table_depart():
    sql = '''
    CREATE TABLE IF NOT EXISTS tb_departamento (
    idt INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    PRIMARY KEY (idt),
    FOREIGN KEY (idt) REFERENCES tb_funcionario(depart_num)
    )
    '''
    cursor.execute(sql)
    print("Conexão com o banco de dados fechada.")

def insert_table_depart():
    sql = '''
    INSERT INTO tb_produtos (name, preco, data_val)
    VALUES (%s, %s, %s)
    '''
    dados = ('Produto 1', 10.00, '2023-10-01')
    cursor.execute(sql, dados)
    conexao.commit()  #confirma a inserção no banco de dados
    print('Dados inseridos com sucesso!')

def delete_table_func():
    sql = '''
    DELETE FROM tb_funcionario WHERE idt = %s
    '''
    dados = (1,)
    cursor.execute(sql, dados)
    conexao.commit()  #confirma a inserção no banco de dados
    print('Dados deletados com sucesso!')

def select_table():
    sql = '''
    SELECT * FROM tb_funcionario
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    conexao = create_connection()
    cursor = conexao.cursor()

    create_database()
    create_table_depart()
    #insert_table()
    #create_table_func()
    #insert_table_func()
    #select_table()
    #delete_table_func()