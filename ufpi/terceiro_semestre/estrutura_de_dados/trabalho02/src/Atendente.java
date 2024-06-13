package src;
// Atributo: String nome.
public class Atendente {
    private String nome;

    public Atendente(String nome) {
        this.nome = nome;
    }
    
    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Atendente: " + nome;
    }
}
