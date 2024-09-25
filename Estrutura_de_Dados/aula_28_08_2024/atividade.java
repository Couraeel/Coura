package aula_28_08_2024;

import java.util.ArrayList;

import javax.swing.JOptionPane;

public class atividade {
	public static void main(String[] args) {
		
		//cria a lista
		ArrayList<Integer> lista = new ArrayList<Integer>();
		String nrElementos = JOptionPane.showInputDialog("Quantos nrs a lista vai ter?");
		int nElementos = Integer.valueOf(nrElementos);
		
		//Repetição respónsavel por capturar os valores digitados pelo usuario e adicioná los na lista
		for(int i = 0; i< nElementos; i++) {
			String valor =
					JOptionPane.showInputDialog("Informe o valor: "+ i);
			lista.add(Integer.valueOf(valor));
		}
		
		int soma = 0;
		for(int i = 0; i< lista.size(); i ++) {
			soma = soma + lista.get(i);
		}
		System.out.println("Soma dos Elementos: "+ soma);
		
	
		int pares = 0;
		int indicesimpares = 0;
		int elemento = 0;
		for(int i = 0; i < lista.size(); i++) {
			elemento = lista.get(i);
			soma = soma + elemento;
			}
			if(elemento % 2 ==0) {
				pares = pares + elemento;
			}
			if(elemento % 2 ==1) {
				indicesimpares = indicesimpares + elemento;
		}
			System.out.println("Soma dos Elementos: "+ soma);
			System.out.println("Soma dos pares: "+ pares);
			System.out.println("Soma dos impares: "+ indicesimpares);
			
}
