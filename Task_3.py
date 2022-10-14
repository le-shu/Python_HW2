# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
dict = {n: ((1+(1/n))**n) for n in range(1, n+1)}
sum = 0

for item in dict.values():
    sum += item

print(dict)
print(round(sum,2))