using System;

namespace two
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 8;
            int y = 3;

            Console.WriteLine(x+y); // Přičítání //
            Console.WriteLine(x-y); // Odčítání //
            Console.WriteLine(x*y); // Násobení //
            Console.WriteLine(x/y); // Dělení bez zbytku //
            Console.WriteLine(Convert.ToDouble(x)/Convert.ToDouble(y)); // Dělení se zbytkem //
            Console.WriteLine(x%y); // Zbytek z dělení //
            int z = x; // Dáváme tomu hodnotu 8 //
            z += x+y; // Přičteme z hodnotu 8+3 //
            z++; // Přičteme 1 //
            y--; // Odečteme 1 //
            Console.WriteLine($"{z} {y}");
            Console.WriteLine(++x); // Tohle nám říká: "Nejdříve přičti 1 a pak vytiskni" // // Tzv. prefixová inkrementace //
            Console.WriteLine(x++); // Tohle nám říká: "Nejdříve vytiskni a pak přičti 1" // // Tzv. postfixová inkrementace //
            Console.WriteLine(x); // Tohle už nám dá výsledek už s +1 //
            x = x-5; // Pouze odečte z x číslo 5 // // Lepší zápis je x -= 5 //
            Console.WriteLine(x);

            int a = 5, b = 9, c = 2; // Takto se dá také přiřazovat hodnoty //

            // Se stringama je to takto

            string name = "Samuel";
            string surname = "Pelc";
            string fullname = name + " " + surname;
            Console.WriteLine("My name is " + fullname);
        }
    }
}