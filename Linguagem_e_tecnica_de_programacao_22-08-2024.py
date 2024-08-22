#Linguagem_e_tecnica_de_programacao_22-08-2024

class Pessoa:
    def __init__(self, nome,age,color,height):
        self.nome = nome
        self.age = age
        self.color = color
        self.height = height

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.age}, Cor: {self.color}, Altura: {self.height}m"


class CadastroPessoas:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, nome, age, color, height):
        pessoa = Pessoa(nome, age, color, height)
        self.pessoas.append(pessoa)

    def buscar_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome.lower() == nome.lower():
                return pessoa
        return None


# Exemplo de uso
cadastro = CadastroPessoas()

# Adicionando pessoas ao cadastro
nome = input("Digite o nome: ")
cpf = input("Digite o CPF: ")
cor = input("Digite a cor: ")
altura = float(input("Digite a altura (em metros): "))

cadastro.adicionar_pessoa(nome, cpf, cor, altura)

cadastro.adicionar_pessoa("Rafael", 18, "pardo", 1.75)
cadastro.adicionar_pessoa("Mateus", 18, "branco", 1.75)
cadastro.adicionar_pessoa("Lorena", 18, "branca", 0.80)
cadastro.adicionar_pessoa("Ricardo", 18, "pardo", 1.70)

# Buscando uma pessoa pelo nome
nome = input("Digite o nome da pessoa que deseja buscar: ")
pessoa_encontrada = cadastro.buscar_pessoa(nome)
if pessoa_encontrada:
    print(f"Pessoa adicionada com sucesso:\n{pessoa_encontrada}")

if pessoa_encontrada:
    print(pessoa_encontrada)
else:
    print("Pessoa não encontrada.")
