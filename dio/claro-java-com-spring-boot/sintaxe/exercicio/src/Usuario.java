public class Usuario {
    public static void main(String[] args) throws Exception {
        SmartTV smartTV = new SmartTV();

        smartTV.ligar();
        System.out.println(smartTV.ligada);
        smartTV.escolherCanal(19);
        System.out.println(smartTV.canal);
    }
}
