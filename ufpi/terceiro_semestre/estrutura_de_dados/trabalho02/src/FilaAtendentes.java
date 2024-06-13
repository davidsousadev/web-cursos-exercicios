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
        // Reenfileiramento do atendente no final da fila após o atendimento, garantindo disponibilidade para atender novos clientes. Os clientes são removidos da fila após o atendimento.
        enqueue(atendente);
        return atendente;
    }
    // Retorna o primeiro atendente da fila sem removê-lo.
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
    //Ajustei a formatação da impressão da lista apenas para melhor visualização
    @Override
    public String toString() {
        return "Fila dos últimos atendentes: " + Arrays.toString(atendentes);
    }
}