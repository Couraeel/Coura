import java.util.HashMap;
import java.util.ArrayList;
public class Prova_molina {  
    public static void main(String[] args) {
/**Uma função recursiva tem que seguir duas regras básicas:
Ter uma condição de parada e Tornar o problema mais simples
SE <condição de parada satisfeita> Retornar
senão Divida o problema num caso mais simples utilizando recursão**/
    int a =2;
    int b =3;
    int resultado = somar(a,b);

    System.out.println("O resultado é:");
    System.out.print(resultado);

    int number = 5;
    int fatorial = 1;

    for(int i = 1;i <= number; i++){
        fatorial = fatorial * i;
        System.out.println(i);
    }

    int result = calculo(4);
    System.out.println(result);
/////////////////////////////////////////////////////////////////////////////////////
    }
    //RECURSIVIDADE
    public static int somar(int a, int b){
        int resultado = a + b;
        return resultado;
    }
    public static int calculo(int n){
        if (n == 0 || n == 1){
            return 1;
        }
        else{
            return n * calculo(n - 1);
        }
    }
}
//////////////////////////////////////////////////////////////////////////////////
// ARRAYLIST
public class ARRAY {
	public static void main(String[] args) {
        ArrayList<String> cars = new ArrayList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    System.out.println(cars);
        //cars.get(0); (Access item)
        //cars.set(0, "Opel"); (change item)
        //cars.remove(0); (remove an item)
        //cars.clear(); (remove all)
        //cars.size(); (array size)
    }
}

//////////////////////////////////////////////////////////////////////////////////
// HASHMAP
public class Mymap {
    /**enquanto Arrays armazenam itens de forma ordenada,linear e se é 
    acessada pelo numero do índice, o hash map por outro lado armazena 
    itens em pares (chave/valor). um objeto é usado como chave(indice) 
    para outro objeto (valor) **/
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
//////////////////////////////////////////////////////////////////////////////////
// HASHSET
/** HashSet<String> cars = new HashSet<String>();
//Add Items
é uma coleção de itens onde cada item é único, nao é possível 
acessar os itens diretamente mas sim verificar se os mesmos existem
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
}}**/
//InsertionSort - Sua teoria baseia-se em ordenar os valores da esquerda para a direita
//pior caso - elementos desordenados (lista decrescente)/medio caso - elementos misturados
//melhor caso - elementos ordenados (lista crescente)

