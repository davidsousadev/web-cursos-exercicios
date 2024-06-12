package src;

import java.util.Arrays;

public class FilaAtendentes {
    private Atendente[] atendentes;
    private int capacidade;
    private int inicio;
    private int fim;
    private int tamanho;

    public FilaAtendentes(int capacidade) {
        this.capacidade = capacidade;
        atendentes = new Atendente[capacidade];
        inicio = 0;
        fim = -1;
        tamanho = 0;
    }
    // Adicionar
    public void enqueue(Atendente atendente){
        if (isFull()){
            throw new IllegalStateException("A fila está cheia!");
        }
        fim = (fim + 1) % capacidade;
        atendentes[fim] = atendente;
        tamanho++;
        }
    // Remover
    public Atendente dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("A fila está vazia!");
        }
        Atendente atendente = atendentes[inicio];
        inicio = (inicio + 1) % capacidade;
        tamanho--;
        // Chamei a função de adicionar para inserir o atendente no final da fila dos atendentes, pois o atendente pode atender outros clientes depois de já ter atendido um cliente.
        enqueue(atendente);
        return atendente;
    }

    public Atendente front() {
        if (isEmpty()) {
            throw new IllegalStateException("A fila está vazia!");
        }
        return atendentes[inicio];
    }

    public Boolean isEmpty() {
        return tamanho == 0;
    }

    public Boolean isFull() {
        return tamanho == capacidade;
    }
    
    @Override
    public String toString() {
        return "Fila de atendentes: " + Arrays.toString(atendentes);
    }
}