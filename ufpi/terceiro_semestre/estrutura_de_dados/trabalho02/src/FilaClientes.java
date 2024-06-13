package src;

import java.util.Arrays;
// Segue toda a implementação dos métodos de fila mostrado na vídeo-aula.
public class FilaClientes {
    private Cliente[] clientes;
    private int capacidade;
    private int inicio;
    private int fim;
    private int tamanho;

    public FilaClientes(int capacidade) {
        this.capacidade = capacidade;
        clientes = new Cliente[capacidade];
        inicio = 0;
        fim = -1;
        tamanho = 0;
    }
    // Adicionar
    public void enqueue(Cliente cliente){
        if (isFull()){
            throw new IllegalStateException("A fila está cheia!");
        }
        fim = (fim + 1) % capacidade;
        clientes[fim] = cliente;
        tamanho++;
        }
    // Remover
    public Cliente dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("A fila está vazia!");
        }
        Cliente cliente = clientes[inicio];
        inicio = (inicio + 1) % capacidade;
        tamanho--;
        return cliente;
    }

    public Cliente front() {
        if (isEmpty()) {
            throw new IllegalStateException("A fila está vazia!");
        }
        return clientes[inicio];
    }

    public Boolean isEmpty() {
        return tamanho == 0;
    }

    public Boolean isFull() {
        return tamanho == capacidade;
    }

    @Override
    public String toString() {
        return "Fila dos últimos clientes: " + Arrays.toString(clientes);
    }
}

