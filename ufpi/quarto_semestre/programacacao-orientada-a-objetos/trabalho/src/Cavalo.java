public class Cavalo extends Animal{
    public Cavalo(String nome, int idade) {
        super(nome, idade, "iiirrrrí","Correr");
    }
    public String movimento(){
        return getMovimento();
    }
    @Override
    public String emitirSom() {
        return getSom();    
    }
}