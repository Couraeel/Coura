package aula3;

public class Principal {
	
	public static void main(String[] args) {
		int valores[] = {2,3,5,8,1,4};
		int todos = 0;
		int impares = 0;
		int pares = 0;
		
		// 1 - Soma de todos os valores
		for(int i = 0; i < valores.length; i++) {
			todos = todos + valores[i];
		}
		System.out.println("A soma total é: " + todos);
		
		// 2 - Soma do valores que ocupam endereços impares
		for(int i = 0; i < valores.length; i++) {
			if(i % 2 == 1) {
				impares = impares + valores[i];
			}
		}
		System.out.println("O total de ímpares é: " + impares);
		
		// 3 - Soma dos pares
		for(int i = 0; i < valores.length; i++) {
			if(valores[i] % 2 == 0) {
				pares = pares + valores[i];
			}
		}
		System.out.println("O total de pares é: " + pares);
		
	}

}
