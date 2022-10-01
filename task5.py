# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number_row_length = int(input('Введите длину ряда: '))

fibonacci1 = []
for i in range(0, number_row_length+1):
    if i == 0:
        fibonacci1.insert(i, i)
    elif i == 1:
        fibonacci1.insert(i, i)
    else:
        fibonacci1.append(fibonacci1[i-1]+fibonacci1[i-2])

fibonacci2 = []
for i in range(1, number_row_length+1):
    if i == 1:
        fibonacci2.insert(i, i)
    else:
        fibonacci2.append(((-1)**(i+1))*fibonacci1[i])
        
fibonacci2.reverse()
print(fibonacci1)
print(fibonacci2)
print(fibonacci2+fibonacci1)

