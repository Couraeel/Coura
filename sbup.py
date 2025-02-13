class Person:
    def __init__(self,name,dep):
        self.name = name
        self.dep = dep

class Prof(Person):
    def __init__(self, name, dep, salario = 0, quant_turma = 0, val_turma = 0):
        super().__init__(name, dep)
        self.salario = salario = salario
        self.quant_turma = quant_turma
        self.val_turma = val_turma

    def get_name(self):
        return self.name

    def get_dep(self):
        return self.dep

    def get_quant_turma(self):
        return self.quant_turma

    def get_val_turma(self):
        return self.val_turma

    def get_salario(self):
        return self.quant_turma * self.val_turma

    def set_name(self, new_val):
        self.name = new_val

    def set_dep(self, new_val):
        self.dep = new_val

    def set_quant_turma(self, new_val):
        self.quant_turma = new_val

    def set_val_turma(self, new_val):
        self.val_turma = new_val

    def mostrar_dados_prof(self):
        print(f"Nome do Prof: {self.get_name()}")
        print(f"Dependencia do Prof: {self.get_dep()}")
        print(f"quantidade de turmas do Prof: {self.get_quant_turma()}")
        print(f"Valor das turmas do Prof: {self.get_val_turma()}")
        print(f"Salario do Prof: {self.get_salario()}")


class Func(Person):
    def __init__(self, name, dep, salario_fixo):
        super().__init__(name, dep)
        self.salario_fixo = salario_fixo

    def get_name(self):
        return self.name

    def get_dep(self):
        return self.dep

    def get_salario_fixo(self):
        return self.salario_fixo

    def set_name(self, new_val):
        self.name = new_val

    def set_dep(self, new_val):
        self.dep = new_val

    def set_salario_fixo(self, new_val):
        self.salario_fixo = new_val

def main():
    pers1 = Person("Mateus",1)
    pers2 = Person("Ricardo",2)
    prof1 = Prof("Rafael",5, 10, 2, 15)
    func1 = Func("Lorena",4,10500)

    namealt = str(input("Digite o nome do Professor:"))
    prof1.set_name(namealt)

    depalt = str(input("Digite o dependencia do Professor:"))
    prof1.set_dep(depalt)

    quant_turma_alt = int(input("Digite a quantidade de turmas do Professor:"))
    prof1.set_quant_turma(quant_turma_alt)

    val_turma_alt = int(input("Digite o valor das turmas do Professor:"))
    prof1.set_val_turma(val_turma_alt)

    prof1.mostrar_dados_prof()

if __name__ == '__main__':
    main()
adicionar o bonus de dependente (cada um equivale a 100 reias)
    #