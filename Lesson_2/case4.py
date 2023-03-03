"""
Задание 4.
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3
Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
lst = input('Enter values by the space: ').split()
print(f'Your list: {lst}')
i = 0
ln = len(lst)
if ln % 2 == 0:
    while i < ln:
        temp = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = temp
        i += 2
else:
    while i < ln - 1:
        temp = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = temp
        i += 2

print(f'Result: {lst}')