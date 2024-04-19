//package atividade;

public class Alunox {
    // Atributos Nome e idade
    public String nome;
    public int idade;

    // Método AtualizaIdade
    public void AtualizeIdade(int novaIdade) {
        this.idade = novaIdade;
    }

    public static void main(String[] args) {
        Alunox aluno1 = new Alunox();
        aluno1.nome = "David";
        aluno1.idade = 27;
        System.out.println("Aluno: " + aluno1.nome + " - Idade: " + aluno1.idade);
        aluno1.AtualizeIdade(28);
        System.out.println("Aluno: " + aluno1.nome + " - Idade: " + aluno1.idade);
    }
}
