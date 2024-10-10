class Employee:
    def __init__(self,name,salary = 0):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def mostrar_dados():
        print(f"Nome do Funcionario: {self.get_name}")
        print(f"Salario do Funcionario: {self.get_salary}")

    def set_name(self,new_val):
        self.name = new_val
    
    def set_salary(self,new_val):
        self.salary = new_val

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Manager(Employee):
    def __init__(self,name,salary = 0,quan_emp = 0, decimot = 0):
        super().__init__(name,salary)
        self.quant_emp = quan_emp
        self.decimot = decimot
    
    def get_quant_emp(self):
        return self.quant_emp
    
    def get_decimot(self):
        return self.decimot

    def mostrar_dados_Manager():
        print(f"Nome do Gerente: {self.get_name}")
        print(f"Salario do Gerente: {self.get_salary}")
        print(f"Quantidade do Gerente: {self.get_quant_emp}") 

    def set_quant_emp(self,new_val):
        self.quant_emp = new_val

if __name__ == '__main__':
    emp1 = Employee("Mateus",69000)
    emp2 = Employee("Ricardo",0.24)
    emp3 = Employee("Lucão")
    manag1 = Manager("Lorena", 40028922)

    namealt = str(input("Digite o nome do funcionario:"))
    emp3.set_name(namealt)

    salaryalt = int(input("Digite o salario do funcionario:"))
    emp3.set_salary(salaryalt)

    emp3.mostrar_dados

    print(emp1.get_salary())