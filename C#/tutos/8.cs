using System;

namespace eight
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i = 1; i <= 10; i++)
            {
                Console.WriteLine(i); // Vypíšou se čísla od 1 do 10
            }

            for(
                int i = 0; // Initializer (Inicializátor) nastavuje počáteční hodnotu proměnné předtím, než cyklus vůbec začne běžet.
                i <= 20; // Condition (Podmínka) určuje pravidlo, které se před každým opakováním kontroluje, a pokud platí, cyklus pokračuje dál.
                i+=2 // Iterator (Iterátor) mění hodnotu řídicí proměnné po každém proběhlém kroku cyklu, aby se mohl posunout k dalšímu opakování.
            )
            {
                Console.WriteLine(i); // Vypíšou se sudá čísla od 0 do 20
            }

            int x = 5;
            while (x>0) // Cyklus poběží tak dlouho, dokud je podmínka True, a skončí v momentě, kdy se změní na False
            {
                Console.WriteLine(x);
                x--;
            }

            int sum = 0;
            int num = 100;
            while(num>=0)
            {
                sum+=num;
                num--;
            }
            Console.WriteLine("The sum (100+99+98+...+0) is: "+sum);

            int b = 5;
            do // Tento cyklus se provede vždy alespoň jednou, bez ohledu na to, zda je podmínka pravdivá (True), nebo ne. Teprve po prvním průchodu se podmínka vyhodnotí a cyklus buď pokračuje, nebo skončí.
            {
                Console.WriteLine(b);
                b++;
            } while (b<5);

            for(int c =0; c <10; c++)
            {
                if(c==5)
                {
                    break; // Vynechá číslo 5 a ukončí cyklus
                }
                Console.WriteLine(c);
            }

            for(int d =0; d <10; d++)
            {
                if(d==5)
                {
                    continue; // Vynechá číslo 5 a pokračuje v cyklu
                }
                Console.WriteLine(d);
            }
        }
    }
}