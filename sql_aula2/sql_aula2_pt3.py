import mysql.connector

conexao = mysql.connector.connect(user='root',
                                   password='ceub123456',
                                   host='127.0.0.1',
                                   database='db_loja')
print('Conexão estabelecida:', conexao)
cursor = conexao.cursor()


prod_name = input("Digite o nome do produto: ")
prod_preco = float(input("Digite o preço do produto: "))
prod_date = input("Digite a data de validade do produto (YYYY-MM-DD): ")

sql = '''INSERT INTO tb_produtos (name, preco, data_validade) VALUES (%s, %s, %s)'''
values = (prod_name, prod_preco, prod_date)

try:
    cursor.execute(sql, values)
    conexao.commit()  # Commit the transaction

    print('Registros inseridos:', cursor.rowcount)
    print('cursor.statement', cursor.statement)
except mysql.connector.Error as err:
    print("Erro ao inserir dados:", err)
finally:
    cursor.close()
    conexao.close()
    print("Conexão com o banco de dados fechada.")
