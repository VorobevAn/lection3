

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите чило: '))
a = number
my_list = []
while number >= 1:
    my_list.append(number % 2)
    number = number//2
my_list.reverse()
print(f'число {a} в двоичном -> ', end="")
print(*my_list)
