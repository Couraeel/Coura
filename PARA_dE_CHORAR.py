import random
import time
import sys

'''try:
    12 / 0
except ZeroDivisionError:
    print("deu ruim oh")
finally:
    print("Sempre da isso mn")

try:
    num1 = int(input("Bota um numero ai doido:"))
    num2 = int(input("Bota outro numero ai doido:"))
    valor = num1 / num2
except ZeroDivisionError:
    print("deu ruim oh")
except ValueError:
    print("nn bota letra nn")
finally:
    print("sempre ocorre")

try:
    f = open("<dados.txt>", "r")
except OSError:
    print("deu ruim oh")
finally:
    print("sempre ocorre")

n = 100
cont = 0 

y = random.randint(1,n)
while True:
    cont +=1
    x = int(input("Digite um numero: "))
    if x == y:
        print("acertou man")
        print("tentativas: {cont}")
        break
    elif x > y:
        print("é menor mn")
    elif x < y:
        print("é maior mn")
    else:
        n -= 1'''

def loading_animation():
    print("Saindo", end="")
    for _ in range(3):
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush() 



telefone = []
print("[1] - Adicionar telefone\n[2] - Remover telefone\n[3] - Verificar telefone\n[4] - Mostrar agenda \n[5] - Sair")
while True:
    opcao = int(input("escolha a opcao: "))
    if opcao == 1:
        x = int(input("digite o telefone: "))
        telefone.append(x)
    elif opcao == 2:
        print(telefone)
        y = int(input("escolha qual dos telefones será removido: "))
        y += 1
        telefone.pop(y)
    elif opcao == 3:
        z = int(input("escreva o telefone que deseja verificar: "))
        if z in telefone:
            print("o telefone esta na lista")
        else:
            print("o telefone nao esta na lista")
    elif opcao == 4:
        print(telefone)

    elif opcao == 5:
        loading_animation()

        break
    else:
        print("valor invalido")