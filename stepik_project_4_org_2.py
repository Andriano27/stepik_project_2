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
matrix = []
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
matrix = [input().split() for _ in range(n)]  # вводим элементы матрицы построчно
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


