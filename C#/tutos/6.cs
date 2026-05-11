using System;

namespace six
{
    class Program
    {
        static void Main(string[] args)
        {
            string password = "password";
            Console.Write("What is your name: ");
            string name = Console.ReadLine();
            Console.Write("Enter your password: ");
            string repeat = Console.ReadLine();
            if (password==repeat)
            {
                Console.WriteLine($"\nYou may enter {name}.");
            }
            else
            {
                Console.WriteLine($"\nYour password is incorrect {name}");
            }

            Console.Write("Select number from 0 to 100: ");
            string txtnumber = Console.ReadLine();
            int number = int.Parse(txtnumber); // Convert.ToInt16(txtnumber)
            if (number>50)
            {
                Console.WriteLine("Number is bigger than 50");
            }
            else if (number==50)
            {
                Console.WriteLine("Number is 50");
            }
            else
            {
                Console.WriteLine("Number is smaller than 50");
            }

            int point = 45;
            int time = 165;
            if (point>30 && time<200) // musejí být obě podmínky True jinak se udělá else
            {
                Console.WriteLine("You are amazing");
            }
            else
            {
                Console.WriteLine("Not good");
            }

            int point2 = 15;
            int time2 = 165;
            if (point2>30 || time2<200) // musí být alespoň jedna podmínka True jinak se udělá else
            {
                Console.WriteLine("You are amazing");
            }
            else
            {
                Console.WriteLine("Not good");
            }

            if (!(point2==15)) // // Vykřičník (negace) obrací pravdivost: podmínka platí, když se point2 NErovná 15
            {
                Console.WriteLine("Points are not equel to 15");
            }
            else
            {
                Console.WriteLine("Points are equel to 15");
            }

            string country = "US";
            int age = 42;
            if ((country == "US" || country == "GB") && (age > 0 && age < 100))
            {
                Console.WriteLine("Welcome " + name);
            }
            else
            {
                Console.WriteLine("Goodbye " + name);
            }
        }
    }
}