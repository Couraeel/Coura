import sqlite3

conexao = sqlite3.connect('livrarias.db')
cur = conexao.cursor()

sql = '''SELECT name, age, cpf FROM tb_cliente'''  # Select specific columns

cur.execute(sql)
l_registros = cur.fetchall()

# Optional: Print the fetched records
for registro in l_registros:
    print(registro)