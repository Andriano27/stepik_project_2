
# Подсписок – часть другого списка. Подсписок может содержать один элемент, несколько или
# даже ни одного. Например, [1], [2], [3] и [4] – подсписки списка [1, 2, 3, 4].
# Список [2, 3] – подсписок списка [1, 2, 3, 4], но список [2, 4] не подсписок списка [1, 2, 3, 4],
# так как элементы 2 и 4 во втором списке не смежные (они разрываются элементом 3).
# Пустой список – подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4]
# подсписок списка [1, 2, 3, 4]. На вход программе подается строка текста, содержащая символы.
# Из данной строки формируется список. Напишите программу, которая выводит список, содержащий все
# возможные подсписки списка, включая пустой список. На вход программе подается строка текста,
# содержащая символы, отделенные символом пробела. Программа должна вывести указанный список,
# содержащий все возможные подсписки, включая пустой список в соответствии с примерами.
s = input().split()  # ввод строки, разделяет на элементы и сохраняет в список s
sublist = [[]]  # список, который должен быть выведен в конце, уже содержит пустой список
result = []  # список, в который будут сохраняться промежуточные значения
for i in range(0, len(s)):  # цикл перебирает индексы элементов списка s.
    # i будет изменяться от 0 до len(s) - 1, включительно.
    for j in range(0, len(s)):  # внутренний цикл
        result = s[j:i + j + 1]  # result будет содержать подсписок с элементами от индекса j до
        # i + j включительно. Если s = ['a', 'b', 'c', 'd'], i = 2, j = 1: s[1:2+1] -> ['b', 'c']
        if len(result) == i + 1:  # условие выполняется, если длина подсписка равна текущему значению
            # внешнего индекса i + 1. i = 2 -> result = 3
            sublist.append(result)
print(sublist)


input_data = input().split()
n = len(input_data)  # сохраняем сюда длину входного списка
result = [[]]  # итоговый список(учитывая пустую подпоследовательность)
for s in range(1, n + 1):  # внешний цикл(длина подпоследовательности),
    # s это размер подсписков(подряд идущих элементов)
    cur_seq = []  # подсписок при проходе с захватом s элементов
    for i in range(n - s + 1):  # внутренний цикл(i - индекс, с которого начинается подсписок,
        # s - размер подсписка, сколько элементов подряд, +1 чтобы было включительно весь s)
        cur_seq.append(input_data[i:i + s])  # добавляем все куски списка длины s во временный список
    result.extend(cur_seq)  # добавляем все найденные подсписки
print(result)


def sublist(a):  # функция принимает один аргумент - список
    li = [[]]  # итоговый список с пустой подстрокой
    for i in range(len(a)):  # внешний цикл, i длина подсписка минус 1
        for j in range(len(a) - i):  # внутренний цикл, j начальный индекс подсписка, len(a) - i,
            # чтобы не выйти за границы списка
            li.append(a[j:j + i + 1])  # берется срез списка и добавляется в итоговый список
    return li
print(sublist(input().split()))


t = input()
t = t.split()
res = []
for i in range(len(t)+1):  # i - начальный индекс подсписка
    for j in range(i+1, len(t)+1):  # j - конечный индекс подсписка, не включительно
        res.append(t[i:j])  # добавляем срез списка t от i до j
res.append([])
print(res)


n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
#  1 2 3
#  4 5 6
#  7 8 9


n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()
#  1 4 7
#  2 5 8
#  3 6 9

n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for i in range(n):
    for j in range(n):
        print(a[n - i - 1][n - j - 1], end=' ')
    print()
#   9 8 7
#   6 5 4
#   3 2 1
# i,j = 0,0 a[3 - 0 - 1][3 - 0 - 1] = a[2][2] = '9', i,j = 0,1 a[3 - 0 - 1][3 - 1 - 1] = a[2][1] = '8'


n = 5
a = [[19, 21, 33, 78, 99],
     [41, 53, 66, 98, 76],
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]
maximum = -1
minimum = 100
for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]
print(minimum + maximum)
# максимум главной диагонали 90, минимум побочной диагонали 11


# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке – количество строк
# и столбцов в матрице. Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке;
# подряд идут элементы сначала первой строки, затем второй, и так далее.
# Напишите программу, которая сначала считывает элементы матрицы один за другим,
# затем выводит их в виде матрицы.
n = int(input())
m = int(input())
s = []
for c in range(n * m):
    s.append(input())
    if len(s) == m:
        print(*s)
        s.clear()

n, m = int(input()), int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]
for row in matrix:
    print(*row)

n, m = int(input()), int(input())
matrix = [[input() for word in range(m)] for _ in range(n)]
for row in matrix:
    print(*row)

def input_matrix(rows, cols):
    matrix = [[input() for _ in range(cols)] for _ in range(rows)]
    return matrix
def print_matrix(matrix):
    for r in range(len(matrix)):
        print(*matrix[r])
    return None
n, m = int(input()), int(input())
print_matrix(input_matrix(n, m))

n = int(input())                        # Ввод кол-ва строк.
m = int(input())                        # Ввод кол-ва столбцов.
matrix = []                             # Создаем пустой список
for i in range(n):                      # Запускаем цикл
    tempMatrix = []                     # Временный список
    for j in range(m):                  # Запускаем цикл для заполнения временного списка
        tempMatrix.append(input())      # Заполняем временный список
    matrix.append(tempMatrix)           # Заполняем созданый список временным списком
for i in range(n):                      # Запускаем цикл перебора строк
    for j in range(m):                  # Запускаем цикл перебора столбцов
        print(matrix[i][j],end=" ")     # Выводим на экран результат с разделителем " "
    print("")                           # Переход на следующую строку

n, m = int(input()), int(input())
a = [[input() for i in range(m)] for j in range(n)]
for x in a:
    print(*x)

# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк
# и столбцов в матрице. Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; подряд
# идут элементы сначала первой строки, затем второй, и так далее. Напишите программу, которая считывает
# элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, и снова ту же
# матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец,
# и так далее. На вход программе подаются два числа n и m – количество строк и столбцов в матрице,
# далее идут n×m слов, каждое на отдельной строке. Программа должна вывести считанную матрицу, за ней
# пустую строку и ту же матрицу, но поменяв местами строки со столбцами. Элементы матрицы разделять
# одним пробелом.
n, m = int(input()), int(input())
matrix = []  # матрица (список списков)
for i in range(n):  # цикл по строкам (всего n строк)
    row = []  # одна строка матрицы
    for j in range(m):  # перебираем элементы строки (всего m элементов)
        row.append(input())  # cчитываем слово и добавляем его в текущую строку
    matrix.append(row)  # добавляем строку в матрицу
# обычная матрица: matrix[i][j]
for i in range(n):  # Идём по строкам
    for j in range(m):  # Идём по элементам строки
        print(matrix[i][j],
              end=' ')  # matrix[i][j] — элемент в строке i, столбце j, end=' ' — чтобы элементы шли
        # через пробел
    print()  # Переход на новую строку после каждой строки матрицы
print()
# транспонированная матрица: matrix[j][i]
# но так как исходная матрица n × m, то индексы в циклах меняются местами:
for j in range(m):  # внешний цикл по m
    for i in range(n):  # внутренний цикл по n
        print(matrix[i][j], end=' ')
    print()


n, m = int(input()), int(input())
# создание матрицы n x m
a = [[0] * m for _ in range(n)]
# считывает элементы матрицы один за другим,
# затем выводит их в виде матрицы
for i in range(n):
    for j in range(m):
        a[i][j] = input()
        print(a[i][j], end=' ')
    print()
#выводит пустую строку
print()
#снова выводит ту же матрицу, но уже поменяв местами строки со столбцами
for i in range(m):
    for j in range(n):
        print(a[j][i], end=' ')
    print()


def print_matrix(matrix, rows, cols, width=1):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j].ljust(width), end=' ')
        print()
def print_transposed_matrix(matrix, rows, cols, width=1):
    for j in range(cols):
        for i in range(rows):
            print(matrix[i][j].ljust(width), end=' ')
        print()
n, m = int(input()), int(input())
matrix = [[input() for j in range(m)] for i in range(n)]
print_matrix(matrix, n, m)
print()
print_transposed_matrix(matrix, n, m)


n, m = [int(input()) for i in range(2)]
matrix = [[input() for i in range(m)] for j in range(n)]
new_matrix = [list(i) for i in zip(*matrix)]
[print(*mat) for mat in matrix]
print()
[print(*mat) for mat in new_matrix]

