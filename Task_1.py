# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = abs(float(input('Введите вещественное число: ')))
Sum = 0

while (a // 1) != a:
    a *= 10
    
while a >= 10:
    Sum = Sum + (a % 10)
    a = int(a / 10)

Sum = int(Sum + a)
print(f'Сумма цифр: {Sum}')