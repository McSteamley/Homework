// Задача 1: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа. Не использовать строки для расчета.

// 456 -> 5
// 782 -> 8
// 918 -> 1
int Prompt(string massage)
{
    System.Console.Write(massage);
    int number = Convert.ToInt32(Console.ReadLine());
    return number;
}
bool ValidateNumber(int number)
{
    if (number < 100 || number >= 1000)
    {
        System.Console.WriteLine("Это не трехзначное число! ");
        return false;
    }
    return true;

}
int number = Prompt("Введите трехзначное число: ");
if (ValidateNumber(number))
{
    int SecondDigit = number / 10 % 10; // Пускай у нас есть число АБВ Остаток деления числа на 100 будет БВ , Делим его на 10 ( в C# Целочисленное деление , получаем Б. Б - вторая цифра числа АБВ)
    System.Console.WriteLine($" Вторая цифра числа {number} равна {SecondDigit} ");
}