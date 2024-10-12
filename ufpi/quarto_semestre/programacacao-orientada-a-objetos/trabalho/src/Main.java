/*
UNIVERSIDADE FEDERAL DO PIAUÍ
CENTRO DE EDUCAÇÃO ABERTA E A DIST NCIA
CURSO DE LICENCIATURA EM COMPUTAÇÃO
DISCIPLINA: PROGRAMAÇÃO ORIENTADA A OBJETOS
Profª  Dr. Francisco Airton Silva
Aluno: David Sousa da Silva
 */

public class Main {
    public static void main(String[] args) throws Exception {

        Animal lola = new Cachorro("Lola", 1);
        Animal bili = new Cavalo("Bili", 7);
        Animal clea = new Preguica("Clea", 12);

        // Emitindo som de forma polimórfica
        System.out.println("Animal: " + lola.getNome() + ", está emitindo som: " + lola.getSom());
        System.out.println("Animal: " + bili.getNome() + ", está emitindo som: " + bili.getSom());
        System.out.println("Animal: " + clea.getNome() + ", está emitindo som: " + clea.getSom());
        System.out.println();

        // Veterinário
        Veterinario veterinario = new Veterinario();

        System.out.println("Animal: "+lola.getNome()+", está no Veterinário sendo examinado e emitindo som: "+veterinario.examinar(lola));
        System.out.println("Animal: "+bili.getNome()+", está no Veterinário sendo examinado e emitindo som: "+veterinario.examinar(bili));
        System.out.println("Animal: "+clea.getNome()+", está no Veterinário sendo examinado e emitindo som: "+veterinario.examinar(clea));
        System.out.println();

        // Zoológico
        Jaula[] jaula = new Jaula[10];
        
        jaula[0] = new Jaula(new Cachorro("Thor", 5));
        jaula[1] = new Jaula(new Cavalo("Luke",4));
        jaula[2] = new Jaula(new Preguica("Nina", 5));
        jaula[3] = new Jaula(new Cachorro("Theo", 6));
        jaula[4] = new Jaula(new Cavalo("Maya", 2));
        jaula[5] = new Jaula(new Preguica("Lola", 5));
        jaula[6] = new Jaula(new Cachorro("Amor", 7));
        jaula[7] = new Jaula(new Cavalo("Meeg", 4));
        jaula[8] = new Jaula(new Preguica("Boob", 2));
        jaula[9] = new Jaula(new Cachorro("Fefi", 5));

        Zoologico zoologico = new Zoologico(jaula);

        zoologico.listarAnimais();
    }   
}