package aula_04_09_2024;

import java.util.HashMap;

public class Mymap {
	public static void main(String[] args) {
		int i = 0;
		HashMap<String, String> Mymap = new HashMap<>();
		Mymap.put("Nome", "João");
		Mymap.put("Idade", "24");
		Mymap.put("Altura", "0,80");
		Mymap.put("Endereço", "Brasilia");
		
		System.out.println(Mymap);
		
		if (Mymap.size() != i) {
			System.out.println("Deu bom oh");
		}
		if (Mymap.size() == i) {
			System.out.println("Tem nada aq nn doidão");
			}
		for (String p: Mymap.values()) {
			System.out.println(p);
		}
			
	}	
}

import java.util.HashSet; // Import the HashSet class
HashSet<String> cars = new HashSet<String>();
//Add Items
public class Main {
  public static void main(String[] args) {
    HashSet<String> cars = new HashSet<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("BMW");
    cars.add("Mazda");
    System.out.println(cars);
//Verificar se existe um item
cars.contains("Mazda");
//Remove an Item
cars.remove("Volvo");
//Remove all
cars.clear();
//ArrayList Size
cars.size();
