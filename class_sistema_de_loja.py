import time

class product():
    def __init__(self, name,buy,sell, amount, cod, validity):
        self.name = name
        self.buy = buy
        self.sell = sell
        self.amount = amount
        self.cod = cod
        self.validity = validity

    def get_name (self):
        return self.name
    
    def get_buy (self):
        return self.buy
    
    def get_sell (self):
        z = self.get_buy()
        sellv = (self.get_buy() / 100) * 15 #taxa
        sellf = self.get_buy()
        sellf += sellv #valor de acrescimo 
        return sellf #valor final
    
    def get_amount (self):
        return self.amount
        
    def get_cod (self):
        return self.cod
    
    def get_validity (self):
        return self.validity
    


    def set_name (self, new_val):
        self.name = new_val
    
    def set_buy (self, new_val):
        self.buy = new_val
        
    def set_sell (self, new_val):
        self.buy = new_val
        sellv = (new_val / 100) * 15 #taxa
        sellf = new_val
        sellf += sellv #valor de acrescimo 
        return sellf #valor final
        
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
        print(f"Valor de compra: {self.buy}")
        print(f"Preço: {self.sell}")
        print(f"Quantidade: {self.amount}")
        print(f"Código: {self.cod}")
        print(f"Validade: {self.validity}")

    #mostrar os dados por get
    def dados (self):
        print(f"Nome do produto: {self.get_name()}")
        print(f"Valor de compra: {self.get_buy()}")
        print(f"Preço: {self.get_sell()}")
        print(f"Quantidade: {self.get_amount()}")
        print(f"Código: {self.get_cod()}")
        print(f"Validade: {self.get_validity()}")
        
    def dados_set (self):
        print(f"Nome do produto: {self.get_name()}")
        print(f"Valor de compra: {self.get_buy()}")
        print(f"Preço: {self.set_sell()}")
        print(f"Quantidade: {self.get_amount()}")
        print(f"Código: {self.get_cod()}")
        print(f"Validade: {self.get_validity()}")


if __name__ == '__main__':
    
    produto1 = product("Leite",100,8, 10, 105.14, "05/25")
    produtox = product("Arroz",10,16, 18, 105.15, "08/25")
    print(produto1.get_sell())

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
                compra = float(input("Digite o valor de compra deste Produto:"))
                produto1.set_buy ({compra})
            except ValueError:
                print("Dado incompativél")

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
            produto1.dados_set()

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
