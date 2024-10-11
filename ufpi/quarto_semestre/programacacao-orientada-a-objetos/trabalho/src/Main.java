public class Main {
    public static void main(String[] args) throws Exception {

        Animal caramelo = new Cachorro("Caramelo", 1);
        Animal bob = new Cavalo("Bob", 7);
        Animal clea = new Preguica("Clea", 12);
        Veterinario veterinario = new Veterinario(caramelo);
        System.out.println("Cachorro: " + caramelo.getNome() + ", Idade: " + caramelo.getIdade() + ", Som: "+caramelo.getSom());
        System.out.println("Cavalo: " + bob.getNome() + ", Idade: " + bob.getIdade() + ", Som: "+bob.getSom());
        System.out.println("Preguiça: " + clea.getNome() + ", Idade: " + clea.getIdade() + ", Som: "+clea.getSom());
        System.out.println("Movimento do cavalo: " + bob.movimento());
        System.out.println("Som do cavalo: " + bob.emitirSom());
        System.out.println("O animal de nome: " + caramelo.getNome() + ", está sendo examinado pelo veterinario e está emitindo esse som: "+ veterinario.examinarAnimal(caramelo));

        // Zoologico
        Jaula[] jaula = new Jaula[10];
        
        jaula[0] = new Jaula(new Cachorro("Thor", 5));
        jaula[1] = new Jaula(new Cavalo("Luke",4));
        jaula[2] = new Jaula(new Preguica("Nina", 5));
        jaula[3] = new Jaula(new Cachorro("Theo", 6));
        jaula[4] = new Jaula(new Cavalo("Maya", 2));
        jaula[5] = new Jaula(new Preguica("Lola", 5));
        jaula[6] = new Jaula(new Cachorro("Amora", 7));
        jaula[7] = new Jaula(new Cavalo("Meg", 4));
        jaula[8] = new Jaula(new Preguica("Bob", 2));
        jaula[9] = new Jaula(new Cachorro("Felix", 5));

        Zoologico zoologico = new Zoologico(jaula);

        zoologico.listarAnimais();
    }   
}
