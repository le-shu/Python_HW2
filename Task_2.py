# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('Введите число: '))
list = []
f = 1

for i in range(1, N+1):
    f = i*f
    list.append(f)

print(f'Произведения от 1 до {N}: {list}')