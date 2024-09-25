package aula4;

import java.util.ArrayList;
import java.util.Iterator;

import javax.swing.JOptionPane;

public class Principal {
	
	public static void main(String[] args) {
		// Recupera a informa��o que ser� utilizada para definir a quantidade
		// de elementos que a lista ter�
		String nrElementos = 
		JOptionPane.showInputDialog("Quantos nrs a lista vai ter?");
		
		// Converte a informa��o passada pelo usu�rio de String para Integer
		int nElementos = Integer.valueOf(nrElementos);
		
		// Cria a lista
		ArrayList<Integer> lista = new ArrayList<Integer>();
		
		// Repeti��o respons�vel por capturar os valores digitados pelo usu�rio
		// e adicion�-los na lista
		for(int i = 0; i < nElementos; i++) {
			String valor = 
				JOptionPane.showInputDialog("Informe o valor " + i);
			lista.add(Integer.valueOf(valor));
		}
		// Apresenta o resultado da lista montada
		System.out.println("Lista completa: " + lista);
		
		int soma = 0;
		int pares = 0;
		int indicesImpares = 0;
		int elemento = 0;
		for(int i = 0; i < lista.size(); i++) {
			elemento = lista.get(i);
			soma = soma + elemento;
			
			if(elemento % 2 == 0) {
				pares = pares + elemento;
			}
			
			if(i % 2 == 1) {
				indicesImpares = indicesImpares + elemento;
			}
			
		}
		System.out.println("Soma dos elementos: " + soma);
		System.out.println("Soma dos pares: " + pares);
		System.out.println("Soma dos endere�os impares: " + indicesImpares);

	}

}
