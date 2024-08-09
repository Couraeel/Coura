'''
C - Create
R - Read
U - Update 
D - Delete
E - Exit
'''

l_nomes = []
def menu():
    print("[C] - Create")
    print("[R] - Read")
    print("[U] - Update")
    print("[D] - Delete")
    print("[E] - Exit")
    opcao = input("Opção:").upper()
    while True:
        if opcao == "C" or "R" or 'U' or "D" or "E":
            break
        else:
            print("opcao ERRADA")
    return opcao

def create():
    nome = input("Nome:").upper()
    l_nomes.append(nome)

def read():
    print(l_nomes)

def update():
    print("digite a posição e o ekemento desejado")
    p = int(input("posicao:"))
    n = str(input("digite o elemento:")).upper()
    l_nomes[p] = n

def delete():
    deletar = str(input("Digite o elemento a ser deletado:")).upper()
    l_nomes.remove(deletar)

