using System;

namespace five
{
    class Program
    {
        static void Main(string[] args)
        {
            bool isStudent = true;
            bool isAbroad = false;
            Console.WriteLine(isStudent); // Vypíše se "True"
            Console.WriteLine(isAbroad); // Vypíše se "False"

            int score = 120;
            Console.WriteLine(score>=80); // Jelikož platí tato podmínka (Score je větší nebo rovno jak 80) napíše se True
            Console.WriteLine(score<=80); // Jelikož neplatí tato podmínka (Score není menší nebo rovno jak 80) napíše se False

            int x = 5;
            int y = 9;
            // Rovná se (==) – vrací true, pokud jsou obě hodnoty stejné
            Console.WriteLine(x == y);
            // Nerovná se (!=) – vrací true, pokud jsou hodnoty odlišné
            Console.WriteLine(x != y);
            // Větší než (>) – vrací true, pokud je hodnota vlevo větší než vpravo
            Console.WriteLine(x > y);
            // Menší než (<) – vrací true, pokud je hodnota vlevo menší než vpravo
            Console.WriteLine(x < y);
            // Větší nebo rovno (>=) – vrací true, pokud je hodnota vlevo větší nebo přesně stejná
            Console.WriteLine(x >= y);
            // Menší nebo rovno (<=) – vrací true, pokud je hodnota vlevo menší nebo přesně stejná
            Console.WriteLine(x <= y);

            string password = "X3g0d2T";
            string repeat = "X3g0d2T";
            Console.WriteLine(password == repeat);
            Console.WriteLine(password != repeat);

        }
    }
}