list = []
print("Digite um valor para ser adicionado a lista Digite X para sair")
while True:
    dados = int(input("Digite um valor"))
    if dados == 0:
        break
    list.append(dados)
    
print((list))
print( len(list))
print( sum(list))
print(max(list))
print(min(list))
busca = int(input("Digite o valor que deseja procurar:"))
position = list.index(busca)
if busca in list:
   print("Esse valor esta na lista, na posicão "position)
else: print("Esse valor não esta na lista:")
print(sorted(list))
list.insert(1,33)
print(list)
list.sort()
list.reverse()
print(list)
med = sum(list) / len(list)
print(f"{med:.3f}")
