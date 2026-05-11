using System;

namespace seven
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Napiš číslo od 1-3 nebo exit: ");
            string choice = Console.ReadLine();
            switch (choice)
            {
                case "1":
                    Console.WriteLine("You chose number 1");
                    break; // Break ukončí pouze switch blok a program pokračuje dál pod ním.
                case "2":
                    Console.WriteLine("You chose number 2");
                    break;
                case "3":
                    Console.WriteLine("You chose number 3");
                    break;
                case "exit":
                case "Exit":
                    Console.WriteLine("Exiting program...");
                    return; // Return ukončí celou metodu Main, čímž se ukončí i celý program.
                default:
                    Console.WriteLine("Invalid choice");
                    break;
            }

            Console.Write("How old are you: ");
            int age = int.Parse(Console.ReadLine());
            string isAdult = age<=18 ? "Too young":"Old enough";
            Console.WriteLine(isAdult);

            int hours = 17;
            string isOpen = hours>18 ? "open":"close";
            Console.WriteLine($"The shop is now {isOpen}");

            double bill = 1800;
            bill = bill>=1000 ? bill*0.90 : bill;
            Console.WriteLine("The bill is: " + bill);
        }
    }
}