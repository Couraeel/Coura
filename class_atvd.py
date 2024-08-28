class Pessoa:
    def __init__(self, name, nascimento, cor_fav, age):
        self.name = name
        self.nascimento = nascimento
        self.cor_fav = cor_fav
        self.age = age

    def get_name(self):
        return self.name
    def get_nascimento(self):
        return self.nascimento
    def get_cor_fav(self):
        return self.cor_fav
    def get_age(self):
        return self.age
    
    #mostrar dados
    def dados(self):
        print(f"Nome: {self.name}")
        print(f"Data de nascimento: {self.nascimento}")
        print(f"Cor favorita: {self.cor_fav}")
        print(f"Idade: {self.age}")

    #mostrar dados via get
    def dados_via_get(self):
        print(f"Nome: {self.get_name()}")
        print(f"Data de nascimento: {self.get_nascimento()}")
        print(f"Cor favorita: {self.get_cor_fav()}")
        print(f"Idade: {self.get_age()}")

    #retornar os dados
    def dados_volta(self):
        return {
            "nome": self.name,
            "Data de nascimento": self.nascimento,
            "Cor favorita": self.cor_fav,
            "idade": self.age
        }
    


    
def main():
    #objetos
    person1 = Pessoa("Mateus", 1945, "roxo", 69)
    person2 = Pessoa("Lorena", 2019, "azul-marinho tem que ser MARINHO ou vermelho vermelho normal não vinho ou um preto", 6)
    person3 = Pessoa("Ricardo", 2001, 1.60, 24)

    print("Mostrando dados diretamente dos atributos:")
    person1.dados()
    print("\n")

    print("Mostrando dados usando métodos Get:")
    person2.dados_via_get()
    print("\n")

    print("Retornando dados como dicionário:")
    dados_person3 = person3.dados_volta()
    print(dados_person3)


if __name__ == "__main__":
    main()  