using System;

namespace tree
{
    class Program
    {
        static void Main (string[] args)
        {
            string nickname; // Vytvoříme proměnou nickname //
            Console.Write("What is your nickname: "); // Napíšeme podtext k zapsání //
            nickname = Console.ReadLine(); // Zde zasadíme hodnotu z terminálu k proměnné nickname //
            Console.WriteLine($"Your nickname is {nickname}"); // Využijeme proměnou nickname //
            int age; // Teď zkusíme číslo //
            Console.Write("How old are you: "); // Zse se zeptáme //
            age = Convert.ToInt16(Console.ReadLine()); // Musíme to převíst na inteager (číslo) //
            Console.WriteLine($"You are {age} years old"); // vypíšeme proměnou age //
            // také se používá int.Parse()
            int age2;
            Console.Write("How old are you: ");
            age2 = int.Parse(Console.ReadLine()); // Pokud by jsme měli hodnotu null tak to okamžitě spadne, u Conver.ToInt32() by to program spolknul //
            Console.WriteLine($"You are {age} years old");

            // Můžeme také pomocí Console.ReadLine() udělat sčítadlo
            string input1 = Console.ReadLine();
            string input2 = Console.ReadLine();
            int number1 = Convert.ToInt32(input1);
            int number2 = int.Parse(input2);
            int resoult = number1 + number2;
            Console.WriteLine($"The sum of these two numbers is {resoult}.");
        
        }
    }
}