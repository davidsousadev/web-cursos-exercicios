public class Zoologico {
    private Jaula[] jaulas;

    public Zoologico(Jaula[] jaulas) {
        this.jaulas = jaulas;
    }
    public void listarAnimais(){
        for (int i = 0; i < this.jaulas.length; i++) {
            if (this.jaulas[i].getAnimal().getMovimento()=="Correr") {
                System.out.println("Animal: " + this.jaulas[i].getAnimal().getNome() + ", Som: " + this.jaulas[i].getAnimal().emitirSom() + ", Movimento: "+jaulas[i].getAnimal().getMovimento());
            }
            else{
                System.out.println("Animal: " + this.jaulas[i].getAnimal().getNome() + ", Som: " + this.jaulas[i].getAnimal().emitirSom());
            }
        }
    }
}
