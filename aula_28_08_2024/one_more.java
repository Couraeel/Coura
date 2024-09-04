package aula_28_08_2024;

import java.util.ArrayList;

import javax.swing.JOptionPane;

public class one_more {
	 public static void main(String[] args) {
	String nrElementos = JOptionPane.showInputDialog("Quantos nrs a lista vai ter?");
	int nElementos = Integer.valueOf(nrElementos);
	ArrayList lista = new ArrayList();
	for(int i = 0; i< nElementos; i++) {
		String valor = 
				JOptionPane.showInputDialog("Informe o valor " + i);
		lista.add(valor);
	}
	System.out.println(lista);
	 }
}
