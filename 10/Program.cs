// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
// A (3,6,8); B (2,1,-7), -> 15.84
// A (7,-5, 0); B (1,-1,9) -> 11.53

Console.WriteLine("Введите координаты x,y,z для точки А разделяя их пробелом: ");
string[] A = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries);
Console.WriteLine("Введите координаты x,y,z для точки B разделяя их пробелом: ");
string[] B = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries);

double xA = double.Parse(A[0]);
double yA = double.Parse(A[1]);
double zA = double.Parse(A[2]);

double xB = double.Parse(B[0]);
double yB = double.Parse(B[1]);
double zB = double.Parse(B[2]);

double S = Math.Sqrt(Math.Pow(xB - xA, 2) + Math.Pow(yB - yA, 2) + Math.Pow(zB - zA, 2));
Console.WriteLine($"A({xA},{yA},{zA}); B({xB},{yB},{zB}) -> {S:f3}");
