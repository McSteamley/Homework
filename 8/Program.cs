//Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа. Не использовать строки для расчета.

// 456 -> 46
// 782 -> 72
// 918 -> 98

int number = new Random().Next(100,1000);
int thritDigit = number % 10;
int temp = number / 10;
int secondDigit = temp % 10;
int firstDigit = number / 100;
int result = firstDigit * 10 + thritDigit;
Console.WriteLine($"{number} -> {result}");