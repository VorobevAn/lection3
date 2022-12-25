

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так:
#[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


k = int(input('Введите число: '))
my_list = [0,1]

for i in range(k-1):
    my_list.append(my_list[i] + -my_list[i+1])
my_list.reverse()
for i in range(k-1,(k*2)-1):
    my_list.append(my_list[i] + my_list[i+1])
print(my_list)