import time

class product():
    def __init__(self, name, amount, cod, validity):
        self.name = name
        self.amount = amount
        self.cod = cod
        self.validity = validity

    def get_name (self):
        return self.name
    
    def get_amount (self):
        return self.amount
        
    def get_cod (self):
        return self.cod
    
    def get_validity (self):
        return self.validity
    

    def set_name (self, new_val):
        self.name = new_val
    
    def set_amount (self, new_val):
        self.amount = new_val
        
    def set_cod (self, new_val):
        self.cod = new_val
    
    def set_validity (self, new_val):
        self.validity = new_val

    def aumentar_amount(self,new_val):
        quant = int(input("Digite a quantidade a ser adicionada ao estoque:"))
        self.amount += quant

    def reduzir_amount(self,new_val):
        quant1 = int(input("Digite a quantidade a ser reduzida ao estoque:"))
        self.amount += quant1

    #mostra os dados diretamente pelos atributos
    def mostra_dados(self):
        print(f"Nome: {self.name}")
        print(f"Preço: {self.amount}")
        print(f"Quantidade: {self.cod}")
        print(f"Código: {self.validity}")

    #mostrar os dados por get
    def dados (self):
        print(f"Nome do produto: {self.get_name()}")
        print(f"Quantidade: {self.get_amount()}")
        print(f"Código: {self.get_cod()}")
        print(f"Validade: {self.get_validity()}")


if __name__ == '__main__':
    
    produto1 = product("Leite", 10, 105.14, "05/25")
    produto2 = product("Arroz", 18, 105.15, "08/25")

    #mostrar os dados ja definidos
    produto1.dados()
    print("Digite 1 para 'sim' e 0 para 'não'")
    option = int(input("Você gostaria de adicionar seus produtos?:"))

    if bool(option) == True: 
        while True:
            #dados com set
            nome = str(input("Digite o nome do Produto:"))
            produto1.set_name ({nome})

            try:
                quantidade = int(input("Digite a quantidade deste Produto:"))
                produto1.set_amount ({quantidade})
            except ValueError:
                print("Dado incompativél")

            try:
                Codigo = float(input("Digite o código deste Produto:"))
                produto1.set_cod ({Codigo})
            except ValueError:
                print("Dado incompativél")

            validade1 = str(input("Digite o mês de validade do Produto:"))
            validade2 = int(input("Digite o ano de validade do Produto:"))
            validade = f"{validade1}/{validade2}"
            produto1.set_validity (validade)

            #mostrar os dados com set
            produto1.dados()

            print("\n Digite 1 para 'sim' e 0 para 'não'")
            option2 = int(input("Você gostaria de adicionar outro produto?:"))
            if bool(option) == False:
                break
     
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print("Programa encerrado")
    else:
        print("Programa encerrado")