# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int(input('Введите N: '))
print(f'Для N = {N}: ', end = ' ')

arr = []
for i in range(N):
    arr.append(random.randint(-N,N))

print(arr)

result = 1

f = open('file.txt', 'r')
for i in f:
    result *= arr[int(i)]
f.close()

print(f'Произведение элементов на заданных позициях: {result}')