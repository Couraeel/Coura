'''
quant = 0
lista = []
soma = 0
while True:
    num = int(input("Digite uma nota:"))
    if num == -1:
        break
    quant += 1
    soma = soma + num
    list.append(lista,num)
med = soma / quant
print(lista)
print("A quantidade de números digitados é:",len(lista))
print(med)
'''

quant = 0
lista = []
soma = 0
while True:
    num = int(input("Digite uma nota:"))
    if num == 0:
        break
    if num % 2 == 0:
        quant += 1
        soma = soma + num
    list.append(lista,num)
med = soma / quant
print(lista)
print("A quantidade de números digitados é:",len(lista))
print(med)
    