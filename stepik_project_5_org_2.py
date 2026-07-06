# На вход программе подаются два натуральных числа n и m. Напишите программу для создания
# матрицы размером n×m, заполнив ее символами '.' и '*' в шахматном порядке. В левом верхнем углу должна
# стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами. На вход программе на
# одной строке через пробел подаются два натуральных числа n и m – количество строк и столбцов в матрице.
# Программа должна вывести матрицу, описанную в условии задачи.
n, m = map(int, input().split())  # input() - считывает строку с клавиатуры, .split() - разбивает строку
# по пробелам, map(int, ...) - превращает строки в числа
for i in range(n):  # переменная i - номер строки матрицы
    mat = []  # пустой список для текущей строки матрицы, в него добавляем точки и звездочки
    for j in range(m):  # переменная j - номер столбца матрицы
        mat.append('.' if (i + j) % 2 == 0 else '*')  # для каждой клетки считаем сумму индексов (i + j),
        # проверяем на четность, если сумма индексов (i + j) % 2 == 0, то число четное, значит ставим '.',
        # иначе '*'
    print(*mat)


n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]
for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'
for row in board:
    print(*row)


n, m = map(int, input().split())
for i in range(n):
    row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
    print(*row)


n, m = input().split()
n, m = int(n), int(m)
matrix = [['.' for _ in range(m) ] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j + 1) % 2 == 0:
            matrix[i][j] = '*'
for i in range(n):
    print(*matrix[i])


n, m = [int(i) for i in input().split()]
line = ((['.']+['*']) * m)
for i in range(n):
    print(*line[:m])
    line.append(line.pop(0))


# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и
# заполняет ее по следующему правилу: числа на побочной диагонали равны 1; числа, стоящие выше этой
# диагонали, равны 0; числа, стоящие ниже этой диагонали, равны 2. Полученную матрицу выведите на экран.
# Числа в строке разделяйте одним пробелом.
n = int(input())
mat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            mat[i][j] = 1
        elif i + j > n - 1:
            mat[i][j] = 2
for row in mat:
    print(*row)


n = int(input())
matrix = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i + j + 1 < n:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 2
for row in matrix:
    print(*row)


def f(i, j, n):
    if i == n - j - 1:
        return 1
    elif i < n - j - 1:
        return 0
    else:
        return 2
n = int(input())
res = [[f(i, j, n) for j in range(n)] for i in range(n)]
for x in res:
    print(*x)


x = int(input())
mtx = [[0] * x for _ in range(x)]
for i in range(x):
    for j in range(x):
        mtx[j][x - i - 1] = 2
        mtx[i][x - i - 1] = 1
    print(*mtx[i])


# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m и заполняет ее числами от 1 до n⋅m в соответствии с образцом. На вход программе на одной
# строке подаются два натуральных числа n и m – количество строк и столбцов в матрице. Программа должна
# вывести матрицу в соответствии с образцом. Для вывода элементов матрицы как в примерах отводите ровно
# 3 символа на каждый элемент. Для этого используйте строковый метод ljust().
n, m = map(int, input().split())  # input() - считывает строку с клавиатуры, .split() - разбивает строку
# по пробелам, map(int, ...) - превращает строки в числа
mat = [[0] * m for _ in range(n)]  # создаем матрицу m столбцов n строк заполненную нулями.
# заполнение матрицы значениями
for i in range(n):  # внешний цикл по индексу строк i
    for j in range(m):  # вложенный цикл по индексу столбцов j
        mat[i][j] = 1 + m * i + j  # рассчитываем порядковый номер ячейки по формуле: '1' - начало матрицы,
        # 'm * i' - умножаем количество элементов 'm' на номер строки 'i', 'j' - индекс текущего столбца
# вывод матрицы на экран
for i in range(n):  # обходим матрицу по строкам
    for j in range(m):  # обходим матрицу по столбцам
        print(str(mat[i][j]).ljust(3), end=' ')  # str(mat[i][j]) - переводит число внутри матрицы в
        # строковый формат, .ljust(3) - дополняет строку пробелами справа до длины 3 символа, end=' '-
        # указывает функции print делать пробел после вывода элемента
    print()  # осуществляет перевод на новую строку после вывода каждой строки матрицы


n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        mat = 1 + m * i + j
        print(str(mat).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
mat = [[str(1 + m * i + j).ljust(3) for j in range(m)] for i in range(n)]
print('\n'.join(' '.join(row) for row in mat))  # ' '.join(row)- Объединяет все элементы одной строки
# матрицы в единый текст через пробел. '\n'.join(...)- Соединяет получившиеся строки между собой, вставляя
# между ними перенос строки (\n), и выводит всё одним махом.


n, m = map(int, input().split())
mat = [[str(1 + m * i + j).ljust(3) for j in range(m)] for i in range(n)]
for row in mat:
    print(*row)


# принимаем n и m, разделяем и плучаем i and j
nm = input().split()
n, m = int(nm[0]), int(nm[1])
matrix, num = [], 1
# создаем матрицу и заполняем
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(j)
    matrix.append(temp)
for i in range(n):
    for j in range(m):
        matrix[i][j] = num
        num += 1
# вывод нарядной матрицы
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m, заполнив ее в соответствии с образцом. Программа должна вывести указанную матрицу в
# соответствии с образцом. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый
# элемент. Для этого используйте строковый метод ljust().
n, m = map(int, input().split())  # input() - считывает строку с клавиатуры, .split() - разбивает строку
# по пробелам, map(int, ...) - превращает строки в числа
mat = [[0] * m for _ in range(n)]  # создаем матрицу m столбцов n строк заполненную нулями.
# заполнение матрицы значениями
for i in range(n):  # внешний цикл по индексу строк i
    for j in range(m):  # вложенный цикл по индексу столбцов j
        mat[i][j] = 1 + n * j + i  # рассчитываем порядковый номер ячейки по формуле: '1' - начало матрицы,
        # 'n * i' - умножаем количество элементов 'n' на номер столбца 'j', 'i' - индекс текущей строки
        # (n - это количество строк, соответственно n элементов в каждом столбце равно количеству строк)
# вывод матрицы на экран
for i in range(n):  # обходим матрицу по строкам
    for j in range(m):  # обходим матрицу по столбцам
        print(str(mat[i][j]).ljust(3), end=' ')  # str(mat[i][j]) - переводит число внутри матрицы в
        # строковый формат, .ljust(3) - дополняет строку пробелами справа до длины 3 символа, end=' '-
        # указывает функции print делать пробел после вывода элемента
    print()  # осуществляет перевод на новую строку после вывода каждой строки матрицы


n, m = [int(i) for i in input().split()]
matrix = [
    list(range(i + 1, i + 1 + n * (m - 1) + 1, n))
    for i in range(n)
]
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()


# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером
# n×n, заполнив ее в соответствии с образцом. На вход программе подается натуральное число n – количество
# строк и столбцов в матрице. Программа должна вывести указанную матрицу в соответствии с образцом:
# разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.
n = int(input())
mat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            mat[i][j] = 1
        elif i + j == n - 1:
            mat[i][j] = 1
for row in mat:
    print(*row)


n = int(input())
matr = [[0] * n for _ in range(n)]
for i in range(n):
    matr[i][i] = 1
    matr[i][n - 1 - i] = 1
for i in range(n):
    for j in range(n):
        print(str(matr[i][j]).ljust(3), end='')
    print()


a = int(input())
for i in range(a):
    sample = [0] * a
    sample[i] = 1
    sample[~i] = 1
    print(*sample)


(lambda n = int(input()): [print(*[str(int(i == j or i == n-j-1)).ljust(3) for j in range(n)])
                         for i in range(n)])()


# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером
# n×n, заполнив ее в соответствии с образцом. На вход программе подается натуральное число n – количество
# строк и столбцов в матрице.
n = int(input())
mat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            mat[i][j] = 1
        elif i + j == n - 1:
            mat[i][j] = 1
        elif i < j and i < n - 1 - j:
            mat[i][j] = 1
        elif i > j and i > n - 1 - j:
            mat[i][j] = 1
for row in mat:
    print(*row)


n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
            matrix[i][j] = 1
for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


n = int(input())
mtx = [[1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i > j and i < n - 1 -j) or (i < j and i > n - 1 -j):
            mtx[i][j] = 0
for i in range(n):
    for j in range(n):
        print(str(mtx[i][j]).ljust(3), end='')
    print()


# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m, заполнив ее в соответствии с образцом.
n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mat[i][j] = (j + i) % m + 1  # используется для циклического сдвига чисел в строках матрицы,
        # чтобы элементы каждой следующей строки сдвигались влево на одну позицию.
for i in range(n):
    for j in range(m):
        print(str(mat[i][j]).ljust(3), end=' ')
    print()
# j — это индекс текущего столбца (меняется от 0 до m-1).
# i — это индекс текущей строки (меняется от 0 до n-1).
# Сложение j + i означает, что в каждой новой строке i стартовое значение для столбцов увеличивается на 1.
# То есть числа начинают «бежать» вперед. Количество столбцов равно m. Когда сумма j + i достигает или
# превышает m, оператор % m сбрасывает значение обратно в ноль. Например, если m = 4, то остатки от
# деления на 4 всегда будут находиться в диапазоне от 0 до 3. Числа 4, 5, 6 превратятся в 0, 1, 2.
# Это и создает бесконечный «круг».
# Операция (j + i) % m выдает числа от 0 до m-1. Прибавление + 1 сдвигает этот диапазон, делая его
# читаемым: от 1 до m.


n, m = map(int, input().split())
s = list(range(1, m + 1))  # формируем первоначальный список
for _ in range(0, n):
    print(*s)  # выводим список
    s = s[1:] + [s[0]]  # формируем новый список, отрезая первый элемент и приставляя его в конец списка


n, m = [int(i) for i in input().split()]
numbers = list(range(1, m + 1))
matrix = []
for _ in range(n):
    matrix.append(numbers)
    # переносим первый элемент списка в конец
    numbers = numbers[1:] + [numbers[0]]
for row in matrix:
    print(*row)


n, m = map(int, input().split())
row = list(range(1, m + 1))
for _ in range(n):
    print(*row)
    x = row.pop(0)
    row.append(x)


# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m, заполнив ее "змейкой" в соответствии с образцом.
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:  # число 0 считается ложью (False), а число 1 (и любое другое ненулевое число) —
        # истиной (True). Для четных строк остаток равен 0. Условие не срабатывает, код идет дальше.
        # Для нечетных строк остаток равен 1. Условие становится истинным (True), и код выполняет
        # команду внутри него.
        matrix[i].reverse()  # matrix[i] — это наша текущая строка под номером i. Если перед этим циклом
        # в нечетной строке matrix[1] лежали числа [4, 5, 6], то команда matrix[1].reverse()
        # превратит их в [6, 5, 4].
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mat[i][j] = m * i + ((i + 1) % 2) * (j + 1) + (i % 2) * (m - j)  # m * i — базовое смещение.
        # Показывает, сколько элементов уже находится в предыдущих строках. ((i + 1) % 2) и (i % 2) —
        # это переключатели (триггеры), принимающие значения 0 или 1 в зависимости от индекса строки i.
        # Если строка четная (i = 0, 2, 4...), то (i + 1) % 2 равно 1, а i % 2 равно 0.
        # Формула превращается в: m * i + (j + 1). Числа идут по возрастанию. Если строка нечетная
        # (i = 1, 3, 5...), то (i + 1) % 2 равно 0, а i % 2 равно 1.
        # Формула превращается в: m * i + (m - j). Числа идут по убыванию.
for i in range(n):
    for j in range(m):
        print(str(mat[i][j]).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
for i in range(n):
    # Создаем срез чисел для текущей строки
    row = list(range(m * i + 1, m * i + m + 1))
    # Если строка нечетная, разворачиваем ее
    if i % 2 != 0:
        row = row[::-1]
    # Красиво печатаем строку (f-строки заменяют ljust)
    print(*(f"{x:<3}" for x in row))


n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]
val = 1  # счетчик, который хранит текущее число для записи в матрицу, начинается с 1
for i in range(n):
    if i % 2 == 0:  # если номер строки четный
        for j in range(m):
            mat[i][j] = val  # берем текущее значение из переменной val и сохраняем его в матрицу mat
            # на пересечение строки i и столбца j.
            val += 1  # берем текущее значение счетчика, прибавляем к нему единицу и сохраняем обратно в val.
    else:  # если номер строки нечетный
        for j in range(m - 1, -1, -1):  # идем в обратном порядке по столбцам
            mat[i][j] = val
            val += 1
for row in mat:  # наружный цикл, берет из целой матрицы каждую строку по отдельности
    for val in row:  # внутренний цикл, чтобы доставать из строки каждое число по отдельности
        print(str(val).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
for i in range(n):
    # Генерируем числа для текущей строки
    row = list(range(m * i + 1, m * i + m + 1))
    # Каждую вторую (нечетную) строку разворачиваем задом наперед
    if i % 2 != 0:
        row = row[::-1]
    # Выводим элементы строки, используя ljust
    for x in row:
        print(str(x).ljust(3), end=' ')
    print()  # Перенос на новую строку после завершения ряда


# принимаем размеры матрицы на вход
n, m = [int(i) for i in input().split()]
# формируем первоначальную матрицу
matrix = [[i * m + j for j in range(1, m + 1)] for i in range(n)]
# переворачиваем каждый второй ряд первоначальной матрицы
for row in matrix[1::2]:
    row.reverse()
# выводим итоговую матрицу
for row in matrix:
    print(*row)


n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        print(str(i * m + j + 1).ljust(3) if i % 2 == 0 else str((i + 1) * m - j).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print(str(j + i * m + 1).ljust(3), end=' ')
        else:
            print(str((i + 1) * m - j).ljust(3), end=' ')
    print()


n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
for i in range(1, n, 2):
    matrix[i].reverse()
for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()


# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m, заполнив ее "диагоналями" в соответствии с образцом. Для вывода элементов матрицы как
# в примерах отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust().
n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]
x = 0  # число, которым будем заполнять матрицу
for i in range(n + m - 1):  # перебираем диагонали по индексам, все возможные значения суммы индексов, так
    # как индексы нумеруются с 0, получаем -1
    for j in range(n):  # перебираем строки
        for k in range(m):  # перебираем столбцы
            if j + k == i:  # принадлежит ли клетка текущей диагонали, перебираются все возможные суммы
                # индексов, все диагонали, для каждой диагонали просматриваются все клетки матрицы, если
                # сумма индексов клетки равна номеру текущей диагонали - в клетку записывается
                # следующее число
                x += 1  # увеличиваем число на 1
                mat[j][k] = str(x)  # записываем новое число в найденную клетку
for j in range(n):
    for k in range(m):
        print(str(mat[j][k]).ljust(3), end=' ')
    print()


n, m = [int(el) for el in input().split()]
matrix = [[None for _ in range(m)] for _ in range(n)]
cnt = 1
# проходим по всем диагоналям
for d in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == d:
                matrix[i][j] = cnt
                cnt += 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()


n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
total = 1
for l in range(n * m ):
    for i in range(n):
        for j in range(m):
            if i + j == l:
                matrix[i][j] = total
                total += 1
for i in range(n):
    print(*matrix[i])


# Принимаем параметры матрицы
n, m = map(int, input().split())
# Создаем скелет матрицы
matrix = [[0] * m for i in range(n)]
# Задаем отсчет с единицы
d = 1
for k in range(1, n + m):               # Цикл перебирающий сумму индексов в диагонали
    for i in range(n):                  # Перебираем строки
        for j in range(m):              # Перебираем столбцы
            if i + j + 1 == k:          # Выявляем ячейки, относящиеся к искомой диагонали
                matrix[i][j] = d        # Присваиваем обнаруженной ячейке порядковый номер
                d += 1                  # Обновляем счетчик
# Распечатываем полученную матрицу
for row in range(n):
    for col in range(m):
        print(str(matrix[row][col]).ljust(3), end=' ')
    print()


n, m = [int(x) for x in input().split()]
l = [[0] * m for _ in range(n)]
k = 1
for j in range(m + n):
    for i in range(n):
        if 0 <= j - i < m:
            l[i][j - i] = k
            k += 1
for i in range(n):
    print(*l[i])


# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m, заполнив ее "спиралью" в соответствии с образцом.
n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]
# Задаем начальные границы и направление движения
top, bottom = 0, n - 1  # top — индекс самой верхней доступной строки (начинаем с 0).
# bottom — индекс самой нижней доступной строки.
left, right = 0, m - 1  # left — индекс самого левого доступного столбца.
# right — индекс самого правого доступного столбца.
x = 1  # Счетчик начинается с 1 и увеличивается на каждом шаге.
while top <= bottom and left <= right:  # Цикл продолжается до тех пор, пока верхняя граница не
    # пересеклась с нижней, а левая — с правой. То есть пока внутри еще осталось свободное место.
    # Идем слева направо
    for i in range(left, right + 1):  # Перебираем индексы столбцов от текущего left до right включительно.
        mat[top][i] = x  # В текущую верхнюю строку (top) записываем число.
        x += 1  # Увеличиваем число для следующей ячейки.
    top += 1  # Самая верхняя строка полностью заполнена. Сдвигаем верхнюю границу top на одну строку вниз.
    # Идем сверху вниз
    for i in range(top, bottom + 1):  # Перебираем индексы строк от новой top до bottom включительно.
        mat[i][right] = x  # В самый правый доступный столбец (right) записываем числа.
        x += 1  # Увеличиваем число.
    right -= 1  # Самый правый столбец полностью заполнен. Сдвигаем правую границу right на один
    # столбец влево.
    # Идем справа налево
    if top <= bottom:  # Проверка. Так как мы только что изменили top, нужно убедиться, что строки еще
        # остались, чтобы не продублировать запись.
        for i in range(right, left - 1, -1):  # Перебираем столбцы в обратном порядке: от right до left
            # (включительно, поэтому -1 во втором аргументе) с шагом -1.
            mat[bottom][i] = x  # Записываем числа в самую нижнюю доступную строку (bottom).
            x += 1  # Увеличиваем число.
        bottom -= 1  # Нижняя строка заполнена. Сдвигаем нижнюю границу bottom на одну строку вверх.
    # Идем снизу вверх
    if left <= right:  # Проверка. Проверяем, остались ли еще столбцы после изменения right на шаге
        # top, bottom + 1
        for i in range(bottom, top - 1, -1):  # Перебираем строки в обратном порядке: от bottom до top
            # снизу вверх.
            mat[i][left] = x  # Записываем числа в самый левый доступный столбец (left).
            x += 1  # Увеличиваем число.
        left += 1  # Левый столбец заполнен. Сдвигаем левую границу left на один столбец вправо.
# Вывод матрицы
for row in mat:  # Перебираем каждую строку матрицы.
    for val in row:  # Перебираем каждое число в текущей строке
        print(str(val).ljust(3), end=' ')
    print()


n, m = [int(num) for num in input().split()]
i = 0
j = 0
cnt = 1
a = [[0 for _ in range(m)] for _ in range(n)]
while cnt < m * n:
    while j < m - 1 and a[i][j + 1] == 0:
        a[i][j] = cnt
        j += 1
        cnt += 1
    while i < n - 1 and a[i + 1][j] == 0:
        a[i][j] = cnt
        i += 1
        cnt += 1
    while j > 0 and a[i][j - 1] == 0:
        a[i][j] = cnt
        j -= 1
        cnt += 1
    while i > 0 and a[i - 1][j] == 0:
        a[i][j] = cnt
        i -= 1
        cnt += 1
a[i][j] = cnt
for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
l = [[0] * m for _ in range(n)]
num = 1
k = 0                                 # уровень квадрата: 0 - внешний, 1 - вложенный и т.д.
product = n * m + 1                   # вынесено в переменную, т.к. n и m меняются в цикле
while num < product:
    for j in range(k, m):             # верхняя сторона
        l[k][j] = num
        num += 1
    for i in range(k + 1, n):         # правая сторона
        l[i][j] = num
        num += 1
    if num == product:                # костыль для случаев с маленькими n, m
        break
    for j in range(m - 2, k - 1, -1): # нижняя сторона
        l[i][j] = num
        num += 1
    for i in range(n - 2, k, -1):     # левая сторона
        l[i][j] = num
        num += 1
    m -= 1                            # изменяю размер сторон для будущего квадрата
    n -= 1
    k += 1
for row in l:
    for el in row:
        print(str(el).ljust(3), end='')
    print()


n, m = map(int, input().split())
i = 1; j = 0; c = 0
a = [[0] * (100) for _ in range(100)]
while c < m * n:
    while a[i][j+1] == 0 and j < m: a[i][j+1] = c+1; j += 1; c += 1
    while a[i+1][j] == 0 and i < n: a[i+1][j] = c+1; i += 1; c += 1
    while a[i][j-1] == 0 and j > 1: a[i][j-1] = c+1; j -= 1; c += 1
    while a[i-1][j] == 0 and i > 1: a[i-1][j] = c+1; i -= 1; c += 1
for i in range(1, n+1):
    for j in range(1, m+1):
        print(str(a[i][j]).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
arr = [[0]*m for i in range(n)]
x, y, dx, dy = 0, 0, 0, 1
for i in range(n*m):
    arr[x][y] = i + 1
    if arr[(x + dx) % n][(y + dy) % m]!=0:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy
for row in arr:
    print(*row)


# Принимаем параметры матрицы
# Альтернативный код: n, m = [int(i) for i in input().split()]
n, m = map(int, input().split())
# Создаем нулевую матрицу размером 'n x m'
matrix = [[0] * m for _ in range(n)]
# Задаем параметры направления смещения
# row_dir - смещение по строкам
# col_dir - смещение по столбцам
# Как видно в нашем случае мы двинемся горизонтально вправо
row_dir, col_dir = 0, 1
# Задаем координаты стартовой ячейки
row, column = 0, 0
# Цикл-счетчик порядкового номера от 1 до n * m
for counter in range(1, n * m + 1):
    # Присваиваем текущей ячейке номер счетчика
    matrix[row][column] = counter
    # Проверяем, не пора ли сделать поворот?
    # Проблема выхода за пределы матрицы решается делением с остатком
    if matrix[(row + row_dir) % n][(column + col_dir) % m]:
        # Поворачиваем направление смещения по часовой стрелке на 90 градусов
        row_dir, col_dir = col_dir, -row_dir
    # Задаем координаты следующей ячейки в соответствии с направлением смещения
    row += row_dir
    column += col_dir
# Распечатываем заполненную матрицу
for row in matrix:
    # переводим матрицу в строковый формат для эстетики отображения
    print(*(f'{e:<3}' for e in row), sep='')


n,m = map(int,input().split())
l = [[0 for i in range(m)] for i in range(n)]
c = 0
i = 0
j = -1
while c != n*m:
    while j < m - 1 and l[i][j+1] == 0:   # двигаюсь влево
        j += 1
        c += 1
        l[i][j] = c
    while i < n - 1 and l[i+1][j] == 0:   # двигаюсь вниз
       i += 1
       c += 1
       l[i][j] = c
    while j > 0 and l[i][j-1] == 0 :   # двигаюсь вправо
       j -= 1
       c += 1
       l [i][j] = c
    while i > 0 and l[i - 1][j] == 0:   # двигаюсь вверх
       i -= 1
       c += 1
       l[i][j] = c
for row in l:
    print(*row)



