
class Pessoa:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
     
    def get_name(self):
        return self.name
    def get_idade(self):
        return self.idade
    
    def apresentar(self):
        print(f"Meu name é {self.name}")
        print(f"Tenho {self.idade} anos")

    def dados(self):
        print(f"name: {self.name}")
        print(f"idade: {self.idade}")


class Funcionario(Pessoa):
    def __init__(self,name,idade, cargo):
        super().__init__(name,idade)
        self.cargo = cargo
    
    def get_cargo(self):
        return self.cargo

    def mostrar_dados_Funcionario(self):
        print(f"name do Funcionario: {self.get_name}")
        print(f"Salario do Funcionario: {self.get_idade}")
        print(f"Quantidade do Funcionario: {self.get_cargo}") 

    def set_cargo(self,new_val):
        self.cargo = new_val

if __name__ == "__main__":
    Pessoa1 = Pessoa("Lorena", 2)
    Pessoa2 = Pessoa("MatHeus", 87)
    Func1 = Funcionario("MatHeus", 87, "estagiario")

    print("Daod do Pessoa:")
    Pessoa1.apresentar()
    Func1.mostrar_dados_Funcionario()
    print("\n")