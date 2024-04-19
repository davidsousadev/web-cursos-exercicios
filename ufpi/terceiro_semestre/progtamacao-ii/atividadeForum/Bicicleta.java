package atividade;

public class Bicicleta {
    // Atributos da classe Bicicleta
    public String marca;
    public String modelo;
    public double peso;
    public String cor;
    public int aro;
    public int velocidadeAtual;
    public double alturaCela;
    public double alturaCelaMaxima;
    public int calibragemPneus;
    public int calibragemPneusMaxima;

    // Método construtor
    public Bicicleta(String marca, String modelo, double peso, String cor, int aro, double alturaCelaMaxima, int calibragemPneusMaxima) {
        this.marca = marca;
        this.modelo = modelo;
        this.peso = peso;
        this.cor = cor;
        this.aro = aro;
        this.velocidadeAtual = 0;
        this.alturaCela = 0;
        this.alturaCelaMaxima = alturaCelaMaxima;
        this.calibragemPneus = 0;
        this.calibragemPneusMaxima = calibragemPneusMaxima;
    }

    // Métodos
    public void pedalar() {
        System.out.println("Pedalando ...");
        this.velocidadeAtual += 7;
    }

    public void frear() {
        if (this.velocidadeAtual > 0) {
            System.out.println("Freando ...");
            this.velocidadeAtual = 0;
        } else {
            System.out.println("No momento a bicicleta está parada!");
        }
    }

    public void ajustarAlturaCela(double novaAltura) {
        if (novaAltura <= this.alturaCelaMaxima && novaAltura > 0) {
            this.alturaCela = novaAltura;
            System.out.println("Altura da cela atualizada para: " + alturaCela);
        } else {
            System.out.println("A altura não foi ajustada o mínimo é 0 e a altura máxima da cela é : " + this.alturaCelaMaxima);
        }
    }

    public void ajustarCalibragemPneus(int novaCalibragem) {
        if (novaCalibragem <= calibragemPneusMaxima && novaCalibragem > 0) {
            this.calibragemPneus = novaCalibragem;
            System.out.println("A calibragem dos pneus foi atualizada para: " + this.calibragemPneus);
        } else {
            System.out.println("Essa calibragem dos pneus não foi atualizada o mínimo é 0 e o máximo é : " + this.calibragemPneusMaxima);
        }
    }

    public static void main(String[] args) {

        // Objetos
        Bicicleta bicicleta1 = new Bicicleta("Caloi", "Andes", 10.5, "Azul", 26, 1.2, 50);
        Bicicleta bicicleta2 = new Bicicleta("Monark", "Barra Circular", 12.0, "Preta", 24, 1.0, 45);
        Bicicleta bicicleta3 = new Bicicleta("Houston", "V-Brake", 11.5, "Branca", 26, 1.1, 48);
        Bicicleta bicicleta4 = new Bicicleta("Bandeirante", "Power Game - com Rodinhas", 9.0, "Vermelha", 20, 0.9, 40);

        // Exemplos de utilização dos métodos
        System.out.println("Exemplos de Utilização de métodos: \n");
        bicicleta1.pedalar();
        System.out.println("Velocidade atual da Bicicleta " + bicicleta1.marca + " - " + bicicleta1.modelo + ": " + bicicleta1.velocidadeAtual + " Km/h.\n");
        bicicleta2.frear();
        System.out.println("Velocidade atual da Bicicleta " + bicicleta2.marca + " - " + bicicleta2.modelo + ": " + bicicleta2.velocidadeAtual + " Km/h.\n");
        bicicleta3.ajustarAlturaCela(7);
        System.out.println("Altura atual da cela da Bicicleta " + bicicleta3.marca + " - " + bicicleta3.modelo + ": " + bicicleta3.alturaCela + " M.\n");
        bicicleta4.ajustarCalibragemPneus(40);
        System.out.println("Calibragem atual da Bicicleta " + bicicleta4.marca + " - " + bicicleta4.modelo + ": " + bicicleta4.calibragemPneus + " PSI.");
    }
}
