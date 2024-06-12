package src;

public class Banco {
    private FilaClientes filaClientes;
    private FilaAtendentes filaAtendentes;

    public Banco(FilaAtendentes filaAtendentes, FilaClientes filaClientes) {
        this.filaAtendentes = filaAtendentes;
        this.filaClientes = filaClientes;
    }

    public FilaAtendentes getAtendentes() {
        return filaAtendentes;
    }

    public FilaClientes getFilaClientes() {
        return filaClientes;
    }

    public Atendimento atenderClientes() {
        if (filaClientes.isEmpty()) {
            throw new IllegalStateException("Nenhum cliente na fila!");
        }
        if(filaAtendentes.isEmpty()){
            throw new IllegalStateException("Nenhum atendente na fila!");
        }
        Cliente cliente = filaClientes.dequeue();
        Atendente atendente = filaAtendentes.dequeue();
        return new Atendimento(cliente, atendente);
    }
}
