public class Media { 

     public static void main(String[] args) {

          double N1, N2, N3, N4, Media;  

          System.out.print("Nota 1: ");
          N1 = Double.parseDouble(System.console().readLine());
          System.out.print("Nota 2: ");
          N2 = Double.parseDouble(System.console().readLine());
          System.out.print("Nota 3: ");
          N3 = Double.parseDouble(System.console().readLine());
          System.out.print("Nota 4: ");
          N4 = Double.parseDouble(System.console().readLine());

          Media = Math.round(((N1 + N2 + N3 + N4) / 4.0));       

          System.out.println("Media: " + Media);

     }

}