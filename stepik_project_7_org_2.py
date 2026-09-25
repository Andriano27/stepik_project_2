# На вход программе подаются строка текста, содержащая символы, и число n.
# Из данной строки формируется список. Напишите программу, которая разделяет список
# на вложенные подсписки так, что n последовательных элементов принадлежат разным подспискам.
# На вход программе подаются строка текста, содержащая символы, отделенные символом пробела, и число
# n на отдельной строке.
string = input().split(' ')
n = int(input())
sublist = [[string[i] for i in range(j, len(string), n)] for j in range(n)]
print(sublist)


string = input().split(' ')
n = int(input())
sublist = [string[j::n] for j in range(n)]  # старт с текущего номера списка j, по всему списку, поэтому
# стоп не нужен, ::, шаг равен общему количеству подсписков n, [string[j::n]] - срез автоматически забирает
# нужные элементы по кругу. Внешний цикл for j in range(n) создает n подсписков, внутри каждого подсписка
# мы берем срез исходной строки с шагом n.
print(sublist)


symbols = input().split()
n = int(input())
result = [[] for _ in range(n)]
for i in range(len(symbols)):
    result[i % n].append(symbols[i])
print(result)


s = input().split()
n = int(input())
res = []
for i in range(n):
    res.append(s[i::n])
print(res)

# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы
# матрицы. Программа должна вывести одно число — максимальный элемент в заштрихованной области
# квадратной матрицы. Элементы побочной диагонали также учитываются.
n = int(input())
matrix = [[int(num) for num in input().split()] for i in range(n)]
count = float('-inf')
for i in range(n):
    for j in range(n):
        if (i >= j and i > n - 1 - j) or (i <= j and i >= n - 1 - j):
            count = max(count, matrix[i][j])
            if count < matrix[i][j]:
                count = matrix[i][j]
print(count)


n = int(input())
matrix = [[int(num) for num in input().split()] for i in range(n)]
count = float('-inf')
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            if matrix[i][j] > count:
                count = matrix[i][j]
print(count)


#  берем размер матрицы
n = int(input())
#  выпиливаем матрицу из входных данных
matrix = [[int(x) for x in input().split()] for i in range(n)]
#  вычисляем больший (элемент) из больших (элементов) в бегущем срезе
answer = max(max(matrix[i][n-i-1:]) for i in range(n))
#  закидываем результат
print(answer)


# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы
# матрицы. Программа должна вывести транспонированную матрицу. Транспонированная матрица — матрица,
# полученная из исходной матрицы заменой строк на столбцы.
n = int(input())
matrix = [[int(num) for num in input().split()] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()


n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for row in matrix:
    print(*row)

n = int(input())
old_matrix = [input().split() for _ in range(n)]
new_matrix = []
for j in range(n):
    cur_row = []
    for i in range(n):
        cur_row.append(old_matrix[i][j])
    new_matrix.append(cur_row)
for row in new_matrix:
    print(*row)


# На вход программе подается нечетное натуральное число n, (n≥3) — количество строк и столбцов в матрице.
# Напишите программу, которая создает матрицу размером n×n заполнив её символами '.' . Затем заполните
# символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.
n = int(input())
matrix = [['.'] * n for _ in range(n)]
for i in range(n):
    # для главной диагонали
    matrix[i][i] = "*"
    # для побочной диагонали
    matrix[i][n - 1 - i] = "*"
    # для средней строки
    matrix[n // 2][i] = "*"
    # для среднего столбца
    matrix[i][n // 2] = "*"
for row in matrix:
    print(*row)


n = int(input())
mat = [['.'] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            mat[i][j] = '*'
        elif i + j == n - 1:
            mat[i][j] = '*'
        elif i == n//2:
            mat[i][j] = '*'
        elif j == n//2:
            mat[i][j] = '*'
for row in mat:
    print(*row)


n = int(input())
matrix = [['.'] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            matrix[i][j] = '*'
        elif i == j or i + j + 1 == n:
            matrix[i][j] = '*'
for row in matrix:
    print(*row)


# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали. На вход
# программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.
# Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
n = int(input())
mtr = [[int(ch) for ch in input().split()] for _ in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if mtr[i][j] != mtr[n - 1 - j][n - 1 - i]:
            flag = False
if flag:
    print('YES')
else:
    print('NO')


def is_symmetric(matrix):
    for i in range(n):
        for j in range(n - i - 1):
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                return "NO"
    return "YES"
n = int(input())
matrix = [input().split() for _ in range(n)]
print(is_symmetric(matrix))


# Латинским квадратом порядка n называется квадратная матрица размером n×n, каждая строка и каждый столбец
# которой содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная
# квадратная матрица латинским квадратом. На вход программе подаётся натуральное число n — количество строк
# и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.
# Программа должна вывести YES, если матрица является латинским квадратом, или NO в противном случае.
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix1 = [[matrix[j][i] for j in range(n)] for i in range(n)]  # транспонированная матрица
flag = True
for i in range(n):
    for j in range(n):
        if j + 1 not in matrix[i] or j + 1 not in matrix1[i]:
            flag = False
if flag:
    print('YES')
else:
    print('NO')


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix_r = [[matrix[j][i] for j in range(n)] for i in range(n)]
def is_latin(matrix):
    for i in range(n):
        for j in range(n):
            if j + 1 not in matrix[i] or j + 1 not in matrix_r[i]:
                return 'NO'
    return 'YES'
print(is_latin(matrix))


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'
for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break
print(result)


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
    if sorted(matrix[i]) != list(range(1, n + 1)) or sorted([matrix[j][i] for j in range(n)]) != list(range(1, n + 1)):
        print('NO')
        break
else:
    print('YES')


# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
# Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
# остальные клетки заполните точками. На вход программе подаются координаты ферзя на шахматной доске
# в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева
# направо), затем номер строки (цифра от 1 до 8, снизу вверх)). Программа должна вывести на экран
# изображение доски, разделяя элементы пробелами.
xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
board = [['.' for _ in range(8)] for _ in range(8)]
# ставим ферзя
board[y][x] = 'Q'
# заполняем клетки, которые бьет ферзь
for i in range(8):
    for j in range(8):
        # если клетка на одной прямой или диагонали с ферзем:
        if i == y or j == x or abs(i - y) == abs(j - x):
            board[i][j] = '*'
board[y][x] = 'Q'
for row in board:
    print(*row)


x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
for i in range(n):
    for j in range(n):
        if i == y or j == x:
            board[i][j] = '*'
        elif abs(i - y) == abs(j - x):
            board[i][j] = '*'
board[y][x] = 'Q'
for row in board:
    print(*row)


# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n
# и заполняет её по следующему правилу: на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, – число 1; на следующих двух диагоналях – число 2, и т.д. На
# вход программе подается натуральное число n — количество строк и столбцов в матрице.
n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # значение элемента - это расстояние от главной диагонали
        matrix[i][j] = abs(i - j)
for row in matrix:
    print(*row)


n = int(input())
matrix = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in matrix:
    print(*row)

