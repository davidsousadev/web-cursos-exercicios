package src;

public class Atendimento {
    private Cliente cliente;
    private Atendente atendente;

    public Atendimento(Cliente cliente, Atendente atendente) {
        this.cliente = cliente;
        this.atendente = atendente;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public Atendente getAtendente() {
        return atendente;
    }

    @Override
    public String toString() {
        return "Cliente: " + cliente + ", " + atendente;
    }
}
