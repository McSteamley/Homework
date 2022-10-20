Console.WriteLine("Введите число в диапазоне от 1 до 7 >>>");
int number = int.Parse(Console.ReadLine());

if(number==6 || number==7)
{
    Console.WriteLine("Номер дня недели является выходным");
}

else
     Console.WriteLine("Номер дня недели не является выходным");