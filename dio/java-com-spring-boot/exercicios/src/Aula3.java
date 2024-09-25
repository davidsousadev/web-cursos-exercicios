public class Aula3 { // Controle de fluxo
    public static void main(String[] args) throws Exception {
        // if e else
        boolean x = true;

        if (x) {
            System.err.println("X é: " + x);
        }

        boolean y = false;

        if (y==true) {
            System.out.println("Y é: " + y);
        }
        else{
            System.out.println("Y é: " + y);
        }
        
        // Operador Ternario
        boolean z = true;
        
        System.out.println("Z é: " + (z ? true : false));

        // Switch Case

        int opcao = 1;

        switch (opcao) {
            case 0:
                System.out.println("Opção: " + opcao);
                break;
        
            default:
            System.out.println("Opção invalida!");
                break;
        }

    }
}
