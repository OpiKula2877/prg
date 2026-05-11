using System;

namespace four
{
    class Program
    {
        static void Main(string[] args)
        {
            // Znak uvozovek nemůžeme v textu použít jen tak, proto před něj vložíme zpětné lomítko \, aby se uvozovka brala jako obyčejný text.
            Console.WriteLine("Person said: \"Hello!\"");
            
            // Zpětné lomítko se znakem 'n' (\n) vytvoří nový řádek, takže se text vypíše pod sebe.
            Console.WriteLine("One\nTwo\nThree");

            // Znak \t funguje jako tabulátor. Odsadí text do pravidelných sloupců, takže budou hodnoty pod sebou krásně zarovnané.
            Console.WriteLine("Name\tAge\tHobby");
            Console.WriteLine("Samuel\t16\tNothing");

            // Znak @ uvozuje doslovný řetězec (Verbatim String). Vypíná speciální význam zpětných lomítek, takže je C# bere jako obyčejný text.
            // Bez znaku @: Každé zpětné lomítko musíme zdvojit (\\), aby ho C# vůbec vypsal.
            Console.WriteLine("C:\\Users\\Samuel\\Documents"); 
            // Se znakem @: Lomítka píšeme normálně (\), kód je díky tomu mnohem čitelnější.
            Console.WriteLine(@"C:\Users\Samuel\Documents");
        }
    }
}