lista_par = []
lista_impar = []
quant_par = 0
quant_impar = 0
soma_par = 0
soma_impar = 0
while True:
    num = int(input("Digite um valor:"))
    if num == 0:
        break
    if num % 2 == 0:
        lista_par.append(num)
        quant_par += 1
        soma_par = sum(lista_par)
    else:
        lista_impar.append(num)
        quant_impar += 1
        soma_impar = sum(lista_impar)
med_par = soma_par / quant_par
med_impar = soma_impar / quant_impar
print(f"A media de numeros pares é:{med_par}")
print(f"A media de numeros impares é:{med_impar}")

lista_altura = []
lista_genero = ["m, f"]
maior_altura = 0
menor_altura = 99
quant_homem = 0
quant_mulher = 0
while True:
    num3 = float(input("Digite a altura:"))
    if num3 == 0:
        break
    num2 = str(input("Digite o gênero:"))
    if num2 == "m":
        quant_homem += 1
    else:
        quant_mulher += 1
    if num3 > maior_altura:
        maior_altura = num3
    if num3 < menor_altura:
        menor_altura = num3
print(f"A maior altura é:{maior_altura}\nA menor altura é:{menor_altura}")
print(f"a quantidade de homens é:{quant_homem}\nA quantidade de mulheres é:{quant_mulher}")
