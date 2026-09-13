def print_matrix(n, a):
    """Выводит матрицу на экран, обеспечивая выравнивание столбцов."""
    width = len(str(n * n))
    for row in a:
        print(" ".join(str(x).ljust(2) for x in row))


def ij(n, a):
    """Возвращает исходную матрицу без изменений."""
    print("a[i][j]" "Исходная матрица")
    return [[a[i][j] for j in range(n)] for i in range(n)]


def ji(n, a):
    """Возвращает транспонированную матрицу."""
    print("a[j][i]", "Транспонирование матрицы")
    return [[a[j][i] for j in range(n)] for i in range(n)]  # a[j][i] = i * n + j + 1


def rotate_90_clockwise(n, a):
    """Возвращает матрицу, повернутую на 90 градусов по часовой стрелке."""
    print("a[n - j - 1][i]" "Поворот на 90 градусов по часовой стрелке")
    return [[a[n - j - 1][i] for j in range(n)] for i in range(n)]


def rotate_90_counterclockwise(n, a):
    """Возвращает матрицу, повернутую на 90 градусов против часовой стрелки."""
    print("a[j][i]" "Поворот на 90 градусов против часовой стрелки")
    return [[a[j][i] for i in range(n)] for j in range(n)]


def rotate_180(n, a):
    """Возвращает матрицу, повернутую на 180 градусов."""
    print("a[n - i - 1][n - j - 1]", "Поворот на 180 градусов")
    return [[a[n - i - 1][n - j - 1] for j in range(n)] for i in range(n)]


def rotate_270(n, a):
    """Возвращает матрицу, повернутую на 270 градусов."""
    print("a[j][n - i - 1]" "Поворот на 270 градусов")
    return [[a[j][n - i - 1] for j in range(n)] for i in range(n)]


def reflect_horizontal(n, a):
    """Возвращает матрицу, отраженную по горизонтальной оси."""
    print("Зеркальное отражение по горизонтали:")
    new_matrix = [row[:] for row in a]
    for i in range(n // 2):
        for j in range(n):
            new_matrix[i][j], new_matrix[n - i - 1][j] = new_matrix[n - i - 1][j], new_matrix[i][j]
    return new_matrix


def swap_diagonal_elements(n, a):
    """Возвращает матрицу, в которой поменяли местами элементы главной и побочной диагонали."""
    print("Поменяли местами элементы на главной и побочной диагоналях:")
    new_matrix = [row[:] for row in a]
    for i in range(n):
        new_matrix[i][i], new_matrix[n - i - 1][i] = new_matrix[n - i - 1][i], new_matrix[i][i]
    return new_matrix


def swap_columns_1_and_2(n, a):
    """Возвращает матрицу, в которой поменяли местами столбцы 1 и 2."""
    print("Поменяли местами столбцы 1 и 2:")
    new_matrix = [row[:] for row in a]
    if n > 2:
        for i in range(n):
            new_matrix[i][1], new_matrix[i][2] = new_matrix[i][2], new_matrix[i][1]
    return new_matrix


def matrix_addition(n, a, b):
    """Возвращает сумму двух матриц."""
    print("Сложение матриц: a + b")
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Матрицы должны быть одинакового размера для сложения.")
        return None
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def matrix_multiplication(n, a, b):
    """Возвращает произведение двух матриц."""
    print("Умножение матриц: a * b")
    if len(a[0]) != len(b):
        print(
            "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице для умножения.")
        return None
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


def is_square_matrix(a):
    """Проверяет, является ли матрица квадратной."""
    rows = len(a)
    if rows == 0:
        return False
    cols = len(a[0])
    return rows == cols


def print_diagonals(n, a):
    """Выводит главную и побочную диагонали матрицы."""
    print("Главная диагональ:")
    for i in range(n):
        print(a[i][i], end=" ")
    print()

    print("Побочная диагональ:")
    for i in range(n):
        print(a[i][n - i - 1], end=" ")
    print()


def create_identity_matrix(n, c):
    """Создание шахматной доски."""
    print("Щахматная доска")
    new_matrix = [row[:] for row in c]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                new_matrix[i][j] = '.'
            else:
                new_matrix[i][j] = '*'
    return new_matrix


def nacij(n, c):
    """Возвращает матрицу с числами на побочной диагонали равными 1, числами, стоящими ниже этой диагонали, равными 2."""
    print("a[n - i - 1][j]", "Побочная диагональ и числа ниже нее")
    new_matrix = [row[:] for row in c]
    for i in range(n):
        for j in range(n):
            if j == n - i - 1:  # Побочная диагональ
                new_matrix[i][j] = 1
            elif j < n - i - 1:  # Выше побочной диагонали
                new_matrix[i][j] = 0
            elif j > n - i - 1:  # Ниже побочной диагонали
                new_matrix[i][j] = 2
    return new_matrix


def spiral(n, c):
    """Выводит матрицу в виде спирали."""
    print("Вывод матрицы в виде спирали:")
    new_matrix = [row[:] for row in c]
    """new_matrix = [[i for i in range(row * y + 1, (row + 1) * y + 1)] for row in range(x)]
        if x == 1 or y == 1:
            return new_matrix"""
    top, bottom, left, right, num = 0, n - 1, 0, n - 1, 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            new_matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            new_matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            new_matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            new_matrix[i][left] = num
            num += 1
        left += 1
    return new_matrix


def plusij(n, c):
    """Возвращает матрицу, в которой элементы ниже главной диагонали равны разности индексов."""
    print("a[i][j]", "Элементы ниже главной диагонали равны разности индексов")
    new_matrix = [row[:] for row in c]
    for i in range(n):
        for j in range(n):
            if i < j:
                new_matrix[i][j] = j - i
            elif i > j:
                new_matrix[i][j] = i - j
    return new_matrix


# Напишите программу для вычисления суммы двух матриц. На вход программе подаются два натуральных числа
# n и m – количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка,
# далее следуют элементы второй матрицы. Программа должна вывести результирующую матрицу, разделяя
# элементы символом пробела.
n, m = map(int, input().split())
# input() — считывает с клавиатуры всю строку целиком, .split() — режет эту строку по пробелам на список
# строк, map(int, ...) — превращает каждую строчку в списке в целое число.
matrix1 = []  # пустой список matrix1, в который мы будем складывать строки первой матрицы.
for i in range(n):  # Запускает цикл, который повторится ровно n раз (столько, сколько у нас строк
    # в матрице)
    row = list(map(int, input().split()))  # Внутри цикла считывает очередную строку чисел через пробел.
    # Превращает её в список чисел с помощью list(...)
    matrix1.append(row)  # Добавляет полученный список чисел (строку) внутрь общего списка matrix1.
    # В итоге получается список списков (двумерный массив).
input()  # Программа просто считывает пустую строку, которая разделяет матрицы, и ничего с ней не делает.
# Это нужно, чтобы каретка ввода перешла на вторую матрицу.
matrix2 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)
result_matrix = []  # пустой список result_matrix, где будет храниться итоговая матрица после сложения.
for i in range(n):  # Внешний цикл. Перебирает индексы строк от 0 до n - 1. Переменная i — это номер
    # текущей строки.
    row = []  # Создает пустой список row, в который мы будем по одному складывать результаты сложения
    # элементов текущей строки.
    for k in range(m):  # Внутренний цикл. Перебирает индексы столбцов от 0 до m - 1. Переменная j — это
        # номер текущего столбца.
        sum_element = matrix1[i][k] + matrix2[i][k]  # Берет элемент из первой матрицы на позиции [i][j]
        # (строка i, столбец j), берет элемент из второй матрицы на той же позиции,
        # складывает их и записывает в sum_element.
        row.append(sum_element)  # Добавляет сумму в текущую строчку row.
    result_matrix.append(row)  # Когда внутренний цикл закончил складывать элементы для всей строки i,
    # эта готовая строка добавляется в результирующую матрицу result_matrix.
for row in result_matrix:  # Перебирает каждую строчку из итоговой матрицы.
    # На каждой итерации переменная row является списком чисел
    print(*row)


n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
input()
matrix2 = [list(map(int, input().split())) for _ in range(n)]
matrix3 = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
for row in matrix3:
    print(*row)


n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB = [[int(i) for i in input().split()] for _ in range(n)]
matrixC = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
for row in matrixC:
    print(*row)


n, m = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(n)]
input()
B = [[int(x) for x in input().split()] for _ in range(n)]
C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
for x in C:
    print(*x)



# На вход программе подаются два натуральных числа n и m – количество строк и столбцов в первой матрице,
# затем элементы первой матрицы, затем пустая строка. Далее следуют числа m и k – количество строк и
# столбцов второй матрицы затем элементы второй матрицы. Программа должна вывести результирующую матрицу,
# разделяя элементы символом пробела. Умножение матрицы на матрицу.
n, m = map(int, input().split())
matrix1 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)
input()
m, k = map(int, input().split())
matrix2 = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix2.append(row)
result_matrix = []
for i in range(n):
    row = []
    for j in range(k):
        s = 0  # Обнуляет сумму перед расчетом нового элемента. Каждый элемент итоговой матрицы — это
        # сумма произведений элементов строки первой матрицы на элементы столбца второй.
        for p in range(m):  # Запускает цикл по элементам текущей строки первой матрицы и текущего столбца
            # второй матрицы. Длина строки первой матрицы равна высоте столбца второй и равна m.
            # Строка первой матрицы считается по количеству столбцов m, также и столбцы второй матрицы
            # считаются по количеству строк m.
            s += matrix1[i][p] * matrix2[p][j]  # Умножает элемент из \(i\)-й строки первой матрицы на
            # элемент из \(j\)-го столбца второй матрицы и прибавляет результат к общей сумме s.
            # Индекс p двигается по строке вправо, а по столбцу — вниз.
        row.append(s)  # После завершения цикла по p готовое число s (финальный элемент новой матрицы с
        # индексами \(i, j\)) добавляется в конец текущей формируемой строки row.
    result_matrix.append(row)  # Когда внутренний цикл for j полностью заполнил строку row элементами,
    # эта строка добавляется в финальный список result_matrix.
for row in result_matrix:
    print(*row)


n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(n)]
input()
x, k = [int(i) for i in input().split()]
b = [[int(i) for i in input().split()] for _ in range(x)]
c = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        c[i][j] = sum(a[i][y] * b[y][j] for y in range(m))
for row in c:
    print(*row)


n1, m1 = map(int, input().split())
matrix1 = [list(map(int, input().split()))for i in range(n1)]
input()
n2, m2 = map(int, input().split())
matrix2 = [list(map(int, input().split()))for i in range(n2)]
matrix3 = [[sum([matrix1[i][k] * matrix2[k][j] for k in range(m1)])for j in range(m2)]for i in range(n1)]
for i in matrix3:
    print(*i)


rows1, cols1 = map(int, input().split())
matr1 = [list(map(int, input().split())) for _ in range(n)]
input()
_, cols2 = map(int, input().split())
matr2 = [list(map(int, input().split())) for _ in range(cols1)]
matr3 = [[0] * k for _ in range(n)]
for i in range(n):  # по строкам первой матрицы
    for j in range(k):  # по столбцам второй матрицы
        for l in range(cols1):  # по столбцам первой и строкам второй матрицы
            matr3[i][j] = matr3[i][j] + (matr1[i][l] * matr2[l][j])
[print(*s, sep=' ') for s in matr3]


# Напишите программу, которая возводит квадратную матрицу в m-ую степень. На вход программе подается
# натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное
# число m. Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
def multiply(A, B, n):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for p in range(n):
                s += A[i][p] * B[p][j]
            res[i][j] = s
    return res
# Считываем размер матрицы n
n = int(input())
# Считываем элементы матрицы
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
# Считываем степень m
m = int(input())
# Создаем единичную матрицу
result_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# Умножаем result_matrix на исходную матрицу m раз
for _ in range(m):
    result_matrix = multiply(result_matrix, matrix, n)
# Выводим результат
for row in result_matrix:
    print(*row)


# Считываем размер матрицы
n = int(input())
# Считываем саму матрицу
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
# Считываем степень m
m = int(input())
# Создаем единичную матрицу (результат для m=0)
result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # Мы создаем квадратную единичную
# матрицу размера \(n \times n\). Если индекс строки i равен индексу столбца j (главная диагональ),
# ставится 1, иначе 0. Если степень \(m=0\), программа сразу выдаст её как правильный ответ.
# Цикл возведения в степень m раз
for _ in range(m):  # Этот цикл заставляет внутренний алгоритм умножения выполниться ровно \(m\) раз.
    # Знак _ используется вместо переменной, так как сам номер итерации нам внутри цикла не нужен.
    # Создаем пустую временную матрицу размера n x n
    mat0 = [[0] * n for _ in range(n)]  # мы сначала накапливаем всю новую матрицу во временную переменную mat0
    # Классическое умножение матриц: result * matrix
    for i in range(n):
        for j in range(n):
            s = 0
            for p in range(n):
                s += result[i][p] * matrix[p][j]
            mat0[i][j] = s
    # Обновляем текущий результат
    result = mat0  #  срабатывает только после того, как вся матрица полностью умножилась
# Выводим итоговую матрицу
for row in result:
    print(*row)


