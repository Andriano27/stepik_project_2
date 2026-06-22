# На вход программе подаются два натуральных числа n и m – количество строк и столбцов в матрице.
# Создайте матрицу mult размером n×m и заполните ее таблицей умножения по формуле mult[i][j] = i * j.
# На вход программе на разных строках подаются два числа n и m – количество строк и столбцов в матрице.
# Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа
# (для этого используйте строковый метод ljust()).
n = int(input())
m = int(input())
for i in range(n):  # внешний цикл от 0 до n - 1
    mult = []  # новый пустой список для каждой строки(при i=0 - список первой строки, i=1 - список второй...)
    for j in range(m):  # перебираем столбцы от 0 до m - 1
        mult.append(str(i * j).ljust(3))  # число при произведении номера строки и столбца превращаем в
        # строку str(i * j), это нужно, потому что вызывается строковый метод .ljust(), он выравнивает
        # строку по левому краю и добавляет пробелы справа до длины 3 в данном случае
    print(*mult)


n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mult[i][j] = i * j
for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()


m, n = int(input()), int(input())
mult =[[i*j for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()


n, m = int(input()), int(input())
[print(*[str(i*j).ljust(3) for j in range(m)]) for i in range(n)]


# На вход программе подаются два натуральных числа n и m – количество строк и столбцов в матрице, затем n
# строк по m целых чисел в каждой, отделенных символом пробела. Напишите программу, которая находит индексы
# (строку и столбец) первого вхождения максимального элемента. На вход программе на разных строках подаются
# два числа n и m – количество строк и столбцов в матрице, затем сами элементы матрицы построчно через
# пробел. Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший
# элемент таблицы. Если таких элементов несколько, то выводится тот,у которого меньше номер строки,
# а если номера строк равны,тот, у которого меньше номер столбца. Нумерация строк и столбцов начинается
# с нуля.
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))  # создание матрицы(строка добавляется по количеству итераций
    # цикла, каждый раз новая).
    matrix.append(row)
max_value = matrix[0][0]
# max_value = float('-inf')
max_row = 0
max_col = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j
print(max_row, max_col)

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j
print(row, col)


n, m = int(input()), int(input())
matrix: list[list[int]] = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
print(matrix.index(max(matrix, key=max)), max(matrix, key=max).index(max(max(matrix, key=max))))


# Напишите программу, которая меняет местами столбцы в матрице. На вход программе на разных строках
# подаются два натуральных числа n и m – количество строк и столбцов в матрице, затем элементы матрицы
# построчно через пробел, затем целые неотрицательные числа i и j – номера столбцов, подлежащих обмену.
# Программа должна вывести указанную таблицу с замененными столбцами.
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]  # заполняем матрицу строчками
    matrix.append(temp)
i, k, j = input()
for r in range(n):
    for c in range(m):
        if c == int(i):
            print(matrix[r][int(j)],end=' ')
        if c == int(j):
            print(matrix[r][int(i)],end=' ')
        if c != int(i) and c != int(j):
            print(matrix[r][c], end=' ')
    print()


n, m = int(input()), int(input())  # вводим значения строк и столбцов
matrix = []
for _ in range(n):
    matrix.append(input().split())
col1, col2 = [int(i) for i in input().split()]  # вводим номера столбцов, подлежащих обмену,
# переменным поэлементно присваиваются значения из списка
for i in range(n):  # цикл по количеству строк, в нем заменяются индексы столбцов
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
for row in matrix:
    print(*row)


n, m = int(input()), int(input())
mult = [input().split() for _ in range(n)]
i, j = map(int, input().split())
for c in mult:
    c[i], c[j] = c[j], c[i]
    print(*c)


n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
res = [int(i) for i in input().split()]
for i in range(n):
    matrix[i][res[0]], matrix[i][res[1]] = matrix[i][res[1]], matrix[i][res[0]]
    print(*matrix[i])


# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
# На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы
# матрицы построчно через пробел. Программа должна вывести YES, если матрица симметрична относительно
# главной диагонали, или NO в противном случае.
n = int(input())
mtr = [[int(ch) for ch in input().split()] for _ in range(n)]
flag = True  # создаем переменную flag - предполагаем что матрица симметрична
for i in range(n):  # внешний цикл по строкам(i - номер строки)
    for j in range(n):  # внутренний цикл по столбцам(j - номер столбца)
        if mtr[i][j] != mtr[j][i]:  # для симметричной матрицы элементы должны быть равны - матрица
            # зеркальна относительно главной диагонали
            flag = False
if flag:
    print('YES')
else:
    print('NO')


# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной
# и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце
# нужно поменять местами элемент на главной диагонали и на побочной диагонали). На вход программе подается
# натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы построчно через
# пробел. Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися
# своими местами.
n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]  # обмен элементов:
    # главная диагональ - matrix[i][i], побочная диагональ: matrix[n - i - 1][i](главное свойство побочной
    # диагонали: строка + столбец = n - 1), столбец остается тем же - i, строка зеркально отражается,
    # элемент главной диагонали меняется местами с элементом побочной диагонали в одном и том же столбце
for row in matrix:  # цикл по каждой строке матрицы
    print(*row)
# i - номер столбца, строка + i = n - 1 => строка = n - i - 1, когда столбец увеличивается, строка
# должна уменьшаться

# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы
# относительно горизонтальной оси симметрии. На вход программе подается натуральное число n – количество
# строк и столбцов в матрице, затем элементы матрицы построчно через пробел. Программа должна вывести
# матрицу, в которой зеркально отображены элементы относительно горизонтальной оси симметрии.
n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
for i in range(n // 2):  # цикл для перестановки строк, //2 показывает, сколько раз выполнится цикл,
    # сколько нужно провести замену строк(при n = 3, 1 раз, i = 0 - индекс заменяемой строки, на
    # n - 1 - i = 2 - индекс другой заменяемой строки)
    matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]  # строки меняются местами
for row in matrix:  # чтобы полностью распаковать список списков построчно, а не просто его части
    print(*row)


n = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
matrix.reverse()  # меняет порядок значений в списке на противоположный
for row in matrix:
    print(*row)


n = int(input())
res = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n - 1, -1, -1):
    print(*res[i])


matrix = [input().split() for _ in range(int(input()))]
[print(*r) for r in matrix[::-1]]


n = int(input())
res = [[int(x) for x in input().split()] for _ in range(n)]
for i in res[n::-1]:
    print(*res[j])


# Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке. На вход
# программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы
# построчно через пробел. Программа должна вывести результат на экран, числа должны быть разделены
# одним пробелом.
n = int(input())  # размер матрицы
matrix = [[int(num) for num in input().split()] for _ in range(n)]  # считываем матрицу
for j in range(n):  # идем по столбцам(строки становятся столбцами, столбцы становятся строками, новая
    # строка = старый столбец)
    for i in range(n - 1, - 1, - 1):  # идем по строкам снизу вверх(элементы берутся из столбца, но
        # читаются снизу вверх)
        print(matrix[i][j], end=' ')  # элемент на пересечении строки i и столбца j
    print()


n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[''] * n for _ in range(n)]  # создаем пустую матрицу такого же размера
for i in range(n):  # перебираем номера строк результирующей матрицы
    for j in range(n):  # перебираем номера столбцов
        result[i][j] = matrix[n - j - 1][i]  # элементы в позиции [i][j] новой матрицы берется из
        # позиции [n - j - 1][i] старой матрицы
for row in result:
    print(*row)


n = int(input())
matrix = [input().split() for i in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[::-1][j][i], end=' ')
    print()


[print(*r) for r in zip(*[list(map(int, input().split())) for _ in range(int(input()))][::-1])]




# На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и
# все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые
# бьет конь, отметьте символами *, остальные клетки заполните точками. На вход программе подаются
# координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается
# номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 1 до 8, снизу вверх)).
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
board = [['.' for _ in range(8)] for _ in range(8)]  # создаем пустую доску с точками
board[y][x] = 'N'  # ставим коня - в клетке коня стоит буква N
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]  # перемещения коня по
# горизонтали и вертикали списком
for dx, dy in moves:  # отмечаем клетки, где бьет конь
    nx = x + dx  # если dx = -1, dy = -2, х = 1, y = 2, nx = 0, ny = 0
    ny = y + dy  # клетка с индексом [0][0] - а8, поэтому ставим туда '*'
    if 0 <= nx < 8 and 0 <= ny < 8:  # это используется, чтобы не выйти за границы доски
        board[ny][nx] = '*'
board[y][x] = 'N'  # после цикла ставим коня на место
for row in board:  # выводим элементы доски через цикл
    print(*row)  # распаковываем список и печатаем элементы через пробел


coordinates = input()
matrix: list[list[str]] = []
for i in range(8):
    matrix.append(['.'] * 8)  # заполняем точками
# переводим шахматные координаты в индексы матрицы
x = 8 - int(coordinates[1])
t = abs(97 - ord(coordinates[0]))
matrix[x][t] = 'N'
# ищем возможные позиции
for i in range(8):
    for j in range(8):
        if abs((x - j) * (t - i)) == 2:
            matrix[j][i] = '*'
for row in matrix:
    print(*row)


# Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел
# 1,2,3, …, n ** 2так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны
# между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим
# квадратом. На вход программе подается натуральное число n – количество строк и столбцов в матрице,
# затем элементы матрицы: n строк, по n чисел в каждой, разделенные пробелами.
# Программа должна вывести YES, если матрица является магическим квадратом, или NO в противном случае.

n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

# 1. Проверяем, что матрица содержит все числа от 1 до n**2 без повторов
flat_list = [element for row in matrix for element in row]
expected_numbers = set(range(1, n ** 2 + 1))
if set(flat_list) != expected_numbers:
    print('NO')
else:
    # За эталон магической суммы берем сумму первой строки
    magic_sum = sum(matrix[0])
    is_magic = True
    # 2. Проверяем суммы всех строк
    for row in matrix:
        if sum(row) != magic_sum:
            is_magic = False
            break
    # 3. Проверяем суммы всех столбцов
    if is_magic:
        for col in range(n):
            col_sum = sum(matrix[row][col] for row in range(n))
            if col_sum != magic_sum:
                is_magic = False
                break
    # 4. Проверяем диагонали
    if is_magic:
        main_diagonal_sum = sum(matrix[i][i] for i in range(n))
        side_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))

        if main_diagonal_sum != magic_sum or side_diagonal_sum != magic_sum:
            is_magic = False
    # Выводим финальный вердикт
    if is_magic:
        print('YES')
    else:
        print('NO')


def is_magic_square(n, matrix):
    # создаем список для всех чисел правильной матрицы
    correct_nums = list(range(1, n ** 2 + 1))
    # создаем список для всех чисел нашей матрицы
    our_nums = []
    for row in matrix:
        our_nums.extend(row)
    # если эти списки не равны, значит наша матрица уже не состоит из всех чисел от 1 до n ** 2
    # значит, мы сразу можем вернуть "NO" и не продолжать дальнейшие проверки
    our_nums.sort()
    if our_nums != correct_nums:
        return "NO"
    # в самой матрице мы уже храним все ряды (строки)
    rows = matrix.copy()
    # создаем список для всех столбцов
    columns = []
    for j in range(n):
        cur_column = []
        for i in range(n):
            cur_column.append(matrix[i][j])
        columns.append(cur_column)
    # создаем список для диагоналей (с двумя пустыми подсписками)
    diagonals = [[], []]
    for i in range(n):
        diagonals[0].append(matrix[i][i])
        diagonals[1].append(matrix[i][n - 1 - i])
    # соединям все строки, столбцы и диагонали в один список
    all_lines = rows + columns + diagonals
    # инициализируем переменные для максимальной и минимальной суммы среди всех "линий"
    # за начальные значения возьмём сумму первой "линии"
    max_sum = sum(all_lines[0])
    min_sum = sum(all_lines[0])
    for line in all_lines:
        max_sum = max(max_sum, sum(line))
        min_sum = min(min_sum, sum(line))
    # теперь просто сравниваем максимальную и минимальную суммы
    # они должны быть равны, т.к. все суммы должны быть равны
    if max_sum != min_sum:
        return "NO"
    return "YES"
n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
print(is_magic_square(n, matrix))


n = int(input())
mat = []                                            # создаем матрицу
for _ in range(n):
  mat.append([int(i) for i in input().split()])
magic = True                                        # устанавливаем флаг
unique = []                                         # пустой список уникальных значений матрицы
for r in range(n):                                  # проверяем все элементы матрицы на уникальность и 0
  for c in range(n):
    if mat[r][c] in unique or mat[r][c] == 0:
      magic = False
      break
    else:
      unique.append(mat[r][c])
total = sum(mat[0])                                 # считаем сумму первой строки матрицы
d1 = 0
d2 = 0
for r in range(n):                                  # проверяем сумму значений главной и побочной диагонали
  for c in range(n):
    if r == c:
      d1 += mat[r][c]
    if r == n - 1 -c:
      d2 += mat[r][c]
if not d1 == d2 == total:
  magic = False
for i in mat:                                        # проверяем суммы всех строк матрицы
  if sum(i) != total:
    magic = False
    break
tran = [[0]*n for _ in range(n)]                     # создаем транспонированную матрицу
for r in range(n):
  for c in range(n):
    tran[r][c] = mat[c][r]
for j in tran:                                       # проверяем суммы строк(они же столбцы исходной матрицы)
  if sum(j) != total:
    magic = False
    break
if magic == True:
  print('YES')
else:
  print('NO')


def sum_matrix(n, total, matrix):
    total += sum(matrix[i][j] for j in range(n) for i in range(n)) # сумма строк
    total += sum(matrix[j][i] for j in range(n) for i in range(n)) # сумма столбцов
    total += sum(matrix[i][i] for i in range(n)) # сумма главной диагонали
    total += sum(matrix[i][n-i-1] for i in range(n)) # сумма второстепенной диагонали
    return total
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
total = 0
total = sum_matrix(n, total, matrix) / (n + n + 2) # сумма матрицы деленная на количество столбцов, строк и диаг
flag = False
l = [matrix[i][j] for j in range(n) for i in range(n)]
l.sort()
if l == [i for i in range(1, n ** 2 + 1)]:
    flag = True
print('YES' if total == sum(matrix[-1]) and flag == True else 'NO')