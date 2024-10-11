public class Cachorro extends Animal{
    public Cachorro(String nome, int idade) {
        super(nome, idade, "au au au", "Correr");
    }

    public String movimento(){
        return getMovimento();
    }
    @Override
    public String emitirSom() {
        return getSom();    
    }
}