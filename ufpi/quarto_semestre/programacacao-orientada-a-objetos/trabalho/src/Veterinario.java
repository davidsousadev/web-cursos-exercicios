public class Veterinario{
    private Animal animal;
    public Veterinario(Animal animal) {
        this.animal = animal;
    }

    public String examinarAnimal(Animal animal){
        return this.animal.emitirSom();
    }
}
