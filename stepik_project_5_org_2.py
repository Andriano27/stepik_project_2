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



