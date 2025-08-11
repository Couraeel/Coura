t = 0
func = []
while True:
    menu = int(input("Oq deseja fazer?: \n 1- Cadastrar um funcionario \n 2- Excluir um funcionario \n 3 - Mostrar Funcionarios \n 4 - Média salarial \n 5 - Funcionarios que mais recebem \n 6-sair\n:"))

    if menu == 1:
        funcionario = {}
        funcionario['nome'] = input("Nome: ")
        funcionario['idade'] = int(input("Idade: "))
        funcionario['cargo'] = input("Cargo: ")
        funcionario['salario'] = float(input("Salario: "))
        func.append(funcionario)

    elif menu == 2:
        break    

    elif menu == 3:        
        for r in func:
            print(f'Nome:{r['nome']}')
            print(f'Cargo:{r['cargo']}')
    

    elif menu == 4:
        media = 0
        for r in func:
            media = media + r['salario']
        print(f'A media é: {media/len(func)}')


    elif menu == 5:
        for r in func:
            if r['salario'] > 5000:
                print(f'Nome:{r['nome']}')
                print(f'Cargo:{r['cargo']}')
                print(f'Idade:{r['idade']}')
                print(f'Salario:{r['salario']}')


    elif menu == 6:
        break
    else:
        break