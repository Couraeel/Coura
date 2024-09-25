package exercicio;

public class Principal {
	
	public static void main(String[] args) {
		
		Carro c1 = new Carro();
		c1.nome = "Song";
		c1.marca = "BYD";
		c1.modelo = "Xing Ling";
		c1.placa = "AZR193B";
		c1.temCarroceria = false;
		c1.temTeto = true;
		c1.tracao = "dianteira";
		c1.ano = 2024;
		
		System.out.println(c1.nome);
		
		Aviao a1 = new Aviao();
		a1.nome = "371";
		a1.marca = "Boeing";
		a1.modelo = "Boeing 371a";
		a1.altitudeMax = 10000;
		a1.ano = 2001;
		a1.numeroMotor = 123456;
		a1.compania = "TAM";

	
		
	}

}
