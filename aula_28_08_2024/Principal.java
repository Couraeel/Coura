package aula_28_08_2024;

import javax.swing.JOptionPane;

public class Principal {

    public static void main(String[] args) {
       String n1 = JOptionPane.showInputDialog("Informe n1");
       String n2 = JOptionPane.showInputDialog("Informe n2");
       int resultado = (Integer.valueOf(n1) + Integer.valueOf(n2));
       JOptionPane.showMessageDialog(null, resultado);
       
    }
}

