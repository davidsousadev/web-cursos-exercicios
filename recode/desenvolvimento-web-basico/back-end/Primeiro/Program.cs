using System;

namespace Primeiro{//Nome do Projeto
    class Program{//Classe sendo utilizada
        static void Main(string[] args){
            Console.WriteLine("Ola mundo!");
            int i = 3;
            Console.WriteLine(i);   // saída: 3
            Console.WriteLine(i++); // saída: 3
            Console.WriteLine(i);   // saída: 4

            double a = 1.5;
            Console.WriteLine(a);   // saída: 1.5
            Console.WriteLine(++a); // saída: 2.5
            Console.WriteLine(a);   // saída: 2.5

            int e = 3;
            Console.WriteLine(e);   // saída: 3
            Console.WriteLine(e--); // saída: 3
            Console.WriteLine(e);   // saída: 2

            double o = 1.5;
            Console.WriteLine(o);   // saída: 1.5
            Console.WriteLine(--o); // saída: 0.5
            Console.WriteLine(o);   // saída: 0.5

            Console.WriteLine(+4);     // saída: 4
            Console.WriteLine(-4);     // saída: -4
            Console.WriteLine(-(-4));  // saída: 4

            Console.WriteLine(13 / 5);    // saída: 2
            Console.WriteLine(-13 / 5);   // saída: -2
            Console.WriteLine(13 / -5);   // saída: -2
            Console.WriteLine(-13 / -5);  // saída: 2

            Console.WriteLine(13 / 5.0);       // saída: 2.6
            int u = 13;
            int b = 5;
            Console.WriteLine((double)u / b);  // saída: 2.6

            Console.WriteLine(5 % 4);   // saída: 1
            Console.WriteLine(5 % -4);  // saída: 1
            Console.WriteLine(-5 % 4);  // saída: -1
            Console.WriteLine(-5 % -4); // saída: -1

            Console.WriteLine(5 + 4);       // saída: 9
            Console.WriteLine(5 + 4.3);     // saída: 9.3

            Console.WriteLine(47 - 3);      // saída: 44
            Console.WriteLine(5 - 4.3);     // saída: 0.7
        }
    }
}