package aula_04_09_2024;

import java.util.HashMap;

public class bruh {
	
	public static void main(String[] args) {
		
		HashMap<String, String> things = new HashMap<>();
		things.put("Rafael", "lindio");
		things.put("MatHeus", "gaymer");
		things.put("Richard", "trouxa");
		
		//things.remove("");
		//things.clear();
		//things.size();
		/*System.out.println(things.get("Rafael"));*/
		System.out.println(things);
	}	
}
/**Arrays armazenam itens como uma coleção ordenada, linear e deve ser 
acessado com um número de índice. No HashMap entanto, armazene 
itens em pares " chave / valor " e você pode acessá-los por um 
índice de outro tipo (por exemplo, a String).
Um objeto é usado como uma chave (índice) para outro objeto (valor). 
Pode armazenar diferentes tipos: String chaves e Integer valores, ou o mesmo tipo, como: String chaves e String valores.**/
