space = ' '
class Titular(object):
    def __init__(self,cpf,nome,sob_nome):
        self.cpf = cpf
        self.nome = nome
        self.sob_nome = sob_nome

    def get_cpf(self):
         return self.cpf

    def get_nome(self):
         return self.nome

    def get_sob_nome(self):
         return self.sob_nome

    def nome_com(self):
        nome_com = self.nome + space + self.sob_nome
        return nome_com

    def set_cpf(self,new_val):
        self.cpf = new_val

    def set_nome(self,new_val):
         self.nome = new_val

    def set_sob_nome(self,new_val):
         self.sob_nome = new_val

    def mostrar_dados(self):
        print("Seu cpf esta cadstrado como: {self.get_cpf()}")
        print(f"Seu nome esta cadastrado como: {self.get_nome()}")
        print(f"Seu sobrenome está cadastrado como: {self.get_sob_nome()}")
        print(f"Seu nome completo em nosso cadastro é: {self.nome_com()}")
class Account(object):
    def __init__(self,number,obj_titular,saldo,limit = 1000):
        self.number = number
        self.obj_titular = obj_titular
        self.saldo = saldo
        self.limit = limit

    def get_number(self):
        return self.number

    def get_obj_titular(self):
        return self.obj_titular

    def get_saldo(self):
        return self.saldo

    def get_limit(self):
        return self.limit

    def mostrar_dados(self):
        print(f'O numero de sua conta é: {self.get_number()}')
        print(f"O objeto de titular é: {self.get_obj_titular()}")
        print(f"O seu saldo atual é: {self.get_saldo()}")
        print(f"Seu limite é: {self.get_limit()}")


    def set_number(self,new_val):
        self.number = new_val

    def set_obj_titular(self,new_val):
        self.obj_titular = new_val

    def set_saldo(self,new_val):
        self.saldo = new_val

    def set_limit(self,new_val):
        self.limit = new_val

    def saque(self):
        saq = int(input("Digite o valor que deseja sacar: "))
        self.saldo -= saq

    def deposito(self):
        dep = int(input("Digite o valor que deseja depositar: "))
        self.saldo += dep

if __name__ == '__main__':
    tit1 = Titular(0,'sla','fez')
    cont1 = Account(0,0,2500)

while True:

    cont1.saque()

    altbool = int(input("O que deseja alterar em seu cadastro?:"))
    if altbool == 1:
        name_alt = str(input("Digite seu primeiro nome:"))
        tit1.nome = name_alt
    if altbool == 2:
        sobnome_alt = str(input("Digite seu sobrenome:"))
        tit1.sob_nome = sobnome_alt
    if altbool == 3:
        cpf_alt = int(input("Digite seu cpf:"))
        tit1.cpf = cpf_alt
    continuar = int(input("Deseja continuar?"))
    if bool(continuar) == False:
        break



tit1.mostrar_dados()
cont1.mostrar_dados()



