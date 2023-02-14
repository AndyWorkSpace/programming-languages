using System;

namespace PrimeraAplicacion
{
    class Program
    {
        static void Main(string[] args)
        {
            //-- definir las varaibles
            float Nota1, Nota2, Nota3, Promedio;
            Console.Write("Ingrese Nota 1 = ");
            Nota1 = float.Parse(Console.ReadLine());
            Console.Write("Ingrese Nota 1 = ");
            Nota2 = float.Parse(Console.ReadLine());
            Console.Write("Ingrese Nota 1 = ");
            Nota3 = float.Parse(Console.ReadLine());
            //-- Calcular promedio
            Promedio = (Nota1 + Nota2 + Nota3) / 3;
            //-- Mostrar resultado
            Console.WriteLine("Promedio = " + Promedio);
            //-- Pause
            Console.ReadLine();
            //string Nombre;
            //Console.WriteLine("Ingrese su nombre!");//salto de line con Writeline
            //Nombre = Console.ReadLine();
            //Console.Write("Hello " + Nombre);//No hay salto de linea con Write
        }
    }
}
