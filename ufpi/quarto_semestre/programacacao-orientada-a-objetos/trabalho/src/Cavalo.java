public class Cavalo extends Animal{
    public Cavalo(String nome, int idade) {
        super(nome, idade, "iii rrrrí","Correr");
    }
    public String movimento(){
        return getMovimento();
    }
    @Override
    public String emitirSom() {
        return getSom();    
    }
}