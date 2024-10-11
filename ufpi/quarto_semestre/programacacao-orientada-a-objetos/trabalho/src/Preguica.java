public class Preguica extends Animal{
    public Preguica(String nome, int idade) {
        super(nome, idade, "aaaaaa","Subir em árvores");
    }
    public String movimento(){
        return getMovimento();
    }
    @Override
    public String emitirSom() {
        return getSom();    
    }
}
