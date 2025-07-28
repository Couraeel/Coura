'''name = str(input("Digite seu nome:"))

while True:
    value = int(input("Digite um valor:"))
    menu = int(input("Oq deseja fazer com seu valor \n 1- saber se o numero é par ou impar \n 2- media do valor (digite outros 2)\n 3-sair\n:"))

    if menu == 1:
        if value % 2 or 0:
            print("seu numero é par")
        else:
            print("seu numero é par")

    elif menu == 2:
        value2 = int(input("digite um segundo valor"))
        value3 = int(input("digite um terceiro valor"))

        media = (value + value2 + value3)/3
        print(media)

    elif menu == 3:
        break
    else:
        break'''






def biggest():
    x = 0
    value = int(input("Digite um valor:"))
    value2 = int(input("Digite um segundo valor:"))
    if value > value2:
        x += value
    else:
        x += value2
    print(x)
    
#biggest()


def primos():


list = []
def media():
    while True:
        value = int(input("Digite um valor:"))
        if value == -1:
            break
        else:
            list.append(value)
    x = sum(list) / len(list)
    print(x)

media()