package aula1;

public class Principal {
	
	public static void main(String[] args) {
		Aluno a1 = new Aluno();
		a1.nome = "Alejandro";
		a1.ra = 123456;
		a1.email = "rs@gmail.com";
		a1.responderChamada();
		
		Aluno a2 = new Aluno();
		a2.nome = "Luiz";
		a2.ra = 78940;
		a2.email = "luiz@gmail.com";
		System.out.println(a2.nome);
		
	}

}
