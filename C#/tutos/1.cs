using System;

namespace one
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = "Samuel";
            Console.WriteLine("Hello " + name);

            int age = 16;
            Console.WriteLine($"I am {age} years old.");

            double height = 1.83;
            Console.WriteLine("I am" + height + "meters tall.");

            bool isStudent = true;
            Console.WriteLine($"Am I student: {isStudent}");
            
            char dolar = '$';
            Int16 money = 752;
            Console.WriteLine($"I have {money}{dolar}");
            /*
                Tohle jsou pro celá čísla:
                short bit = 16;
                int bit = 32;
                long bit = 64;
                int128 bit = 128

                Tohle jsou pro desetinná čísla:
                float bit = 32
                double bit = 64
                decimal bit = 128
            */
        }
    }
}