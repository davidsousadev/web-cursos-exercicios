//package atividade;

public class Aluno {
    public String nome;
    public int idade;

    // Adição de getters e setters
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void atualizeIdade(int novaIdade) {
        this.setIdade(novaIdade);
    }
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno();
        aluno1.nome = "David";
        aluno1.idade = 27;
        System.out.println("Aluno: " + aluno1.getNome() + " - Idade: " + aluno1.getIdade());
        aluno1.atualizeIdade(28);
        System.out.println("Aluno: " + aluno1.getNome() + " - Idade: " + aluno1.getIdade());
    }
}
