class Bank():
    def __init(self,name,balance = 0):
        name.self = name
        balance.self = balance 

    def get_name(self):
        return self.name
    
    def set_name(self,new_val):
        self.name = new_val
    
    def get_balance(self):
        return self.balance
    
    def set_balance(self,new_val):
        self.balance = new_val
    
    def get_genre(self):
        return self.genre
    
    def set_genre(self,new_val):
        self.genre = new_val
    
    def get_Pj(self):
        return self.Pj
    
    def set_Pj(self,new_val):
        self.Pj = new_val

    def __str__(self):
        conta1 = f'Nome{self.name}, R${self.balance}'
        return conta1
    
    def deposit(self,val):
        val = float(input("Digite o valor que deseja depositar:"))
        self.balance += val 

    def withdraw(self,val):
        val = float(input("Digite o valor que deseja sacar:"))
        self.balance -= val 

    def Pf (Bank):
        def __init(self,name,balance = 0,gender = "",cpf=""):
            super().__init__(name,balance = 0)
            self.cpf = cpf
            self.gender = gender

    def Pj (Bank):
        def __init(self,name,balance = 0,cnpj=""):
            super().__init__(name,balance = 0)
            self.cpf = cnpj
    
if __name__ == '__main__':
    person1 = Bank(f'Nome: {"Mateus"}, Saldo: R${400}, Gênero: {"M"}, Cpf: {"098.098.98"}')
    person2 = Bank(f'Nome: {"Ricardo.ltda"}, Saldo: R${0,36}, Cnpj: {000}')
    
    option = int(input("Você gostaria de adicionar um cnpj?:"))
    if bool(option) == True:
        cnpjc = "00.000.000.000.00"
        x,y,z,w,r = cnpjc.split(".")
        x = str(input(""))
        y = str(input(""))
        z = str(input(""))
        w = str(input(""))
        r = str(input(""))


        if w != "0001":
            print("cnpj incorreto")
        w = "0001"
        cnpj_comp = str(x+"."+y+"."+z+"/"+w+"-"+r)
        print(cnpj_comp)
    else:
        pass