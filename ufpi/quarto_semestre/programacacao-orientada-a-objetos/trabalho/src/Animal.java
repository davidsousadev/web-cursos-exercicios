public abstract class Animal {
    private String nome;
    private int idade;
    private String som;
    private String movimento;

    // Método Construtor
    public Animal(String nome, int idade, String som, String movimento) {
        this.nome = nome;
        this.idade = idade;
        this.som = som;
        this.movimento = movimento;
    }

    // Getters
    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public String getSom() {
        return som;
    }

    public String getMovimento() {
        return movimento;
    }

    // Setters
    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public abstract String emitirSom();

    public abstract String movimento();
}

