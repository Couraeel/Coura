class Vehicle():
    def __init__(self,price,model,km):
        self.price = price
        self.model = model
        self.km = km

    def get_price(self):
        return self.price

    def get_model(self):
        return self.model

    def get_km(self):
        return self.km

    def set_price(self,new_val):
        self.price = new_val

    def set_model(self,new_val):
        self.model = new_val

    def set_km(self,new_val):
        self.km = new_val

    

class Car(Vehicle):
    def __init__(self,price,model,km,trunk):
        super().__init__(price,model,km)
        self.trunk = trunk

    def get_trunk(self):
        return self.trunk

    def set_trunk(self,new_val):
        self.trunk = new_val

    

class Moto(Vehicle):
    def __init__(self,price,model,km,bag):
        super().__init__(price,model,km)
        self.bag = bag

    def get_bag(self):
        return self.bag

    def set_bag(self,new_val):
        self.bag = new_val

    

if __name__ == '__main__':
    V1 = Vehicle(100,'vião',969)
    C1 = Car(240,'carro',1000,'sim')
    M1 = Moto(1470,'moto',45,'sim')

    print("Digite [1] para sim e [0] para não")
    escol = int(input("Voce deseja alterar algum dado ?"))
    if bool(escol) == True:
        print("Qual deseja mudar?\n[1]  ")



    print(f"O Preço deste veículo é: R${V1.get_price()}")
    print(f"O Modelo deste veículo é: {V1.get_model()}")
    print(f"A Kilometragem deste veículo é: {V1.get_km()}")
    print(f"O Preço deste veículo é: R${C1.get_price()}")
    print(f"O Modelo deste veículo é: {C1.get_model()}")
    print(f"A Kilometragem deste veículo é: {C1.get_km()}")
    print(f"Este carro possui porta-malas?: {C1.get_trunk()}")
    print(f"O Preço deste veículo é: R${M1.get_price()}")
    print(f"O Modelo deste veículo é: {M1.get_model()}")
    print(f"A Kilometragem deste veículo é: {M1.get_km()}")
    print(f"Esta moto possui bag?: {M1.get_bag()}")