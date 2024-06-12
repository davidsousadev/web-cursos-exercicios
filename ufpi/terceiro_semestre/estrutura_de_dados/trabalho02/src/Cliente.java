package src;

public class Cliente {
    String nome;
    String cpf;

    public Cliente(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }
    // Getters
    public String getNome() {
        return nome;
    }

    public String getCpf() {
        return cpf;
    }
    @Override
    public String toString() {
        return "Nome:" + nome +" - CPF:" + cpf;
    }
}


