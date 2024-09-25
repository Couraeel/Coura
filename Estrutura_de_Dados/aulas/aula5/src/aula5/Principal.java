package aula5;

import java.util.HashMap;

public class Principal {

	public static void main(String[] args) {

		HashMap<String, String> capitais = new HashMap<>();
		capitais.put("Inglaterra", "Londres");
		capitais.put("Brasil", "Brasília");
		capitais.put("Argentina", "Bueno Aires");

		capitais.put("Brasil", "Salvador");
		capitais.remove("Brasil");

		System.out.println("Lista completa: " + capitais);

		// Exemplo que apresenta as chaves que compoem
		// a lista
		for (String i : capitais.keySet()) {
			System.out.println("Chave:" + i);
		}

		for (String i : capitais.values()) {
			System.out.println("Valor:" + i);
		}

	}
}
