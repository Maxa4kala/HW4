#Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки
#a1 = 7
#d = 2
#n = 5
#for i in range(n):
#    print(a1 + i * d, end=' ')


#Определить индексы элементов массива (списка), значения которых 
#принадлежат заданному диапазону (т.е. не меньше заданного минимума 
#и не больше заданного максимума)
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
max = 10
min = 6
# for i in range(len(lst_1)):
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(list_2)
# или
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')
