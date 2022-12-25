

#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

import random
saiz = int(input("Ведите длину списка: "))
my_list = []

for i in range(saiz):
    my_list.append(random.randint(0,20))
print(my_list)

result_list = []

i = 0
while i != saiz//2:
    a = my_list[i]
    b = my_list[-1-i]
    result_list.append(a+b)
    i+=1

if saiz%2==0:
    print(result_list)
else:
    result_list.append(my_list[i]*2)
    print(result_list)