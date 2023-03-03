"""
Задание 5.
Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.
Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три
Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""
st = input(f'Enter words by the space: ').split()
i = 0
while i < len(st):
    if len(st[i]) < 10:
        print(f'{i + 1}. {st[i]}')
    else:
        i_th = st[i]
        print(f'{i + 1}. {i_th[:10]}')
    i += 1