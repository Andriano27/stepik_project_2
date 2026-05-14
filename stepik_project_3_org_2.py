# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки. На вход программе подается натуральное число
# n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
# Программа должна вывести n чисел – для каждой строки количество элементов матрицы, больших среднего
# арифметического элементов данной строки.
n = int(input())
count = 0  # количество элементов в строке, которое больше среднего
mid = 0
matrix = []  # список, куда будем сохранять всю матрицу
for i in range(n):  # цикл выполняется n раз по количеству строк
    temp = [int(num) for num in input().split()]  # input().split() - считываем строку и разбиваем на
    # числа, [int(num) for num in ...] - превращаем каждое число в int, temp - это одна строка матрицы
    matrix.append(temp)  # добавляем temp в матрицу
for r in matrix:  # перебираем строки матрицы, r - одна строка, список чисел
    mid = sum(r)/len(r)  # среднее арифметическое строки
    for c in range(len(r)):  # идем по каждому элементу строки
        if r[c] > mid:  # если элемент больше среднего арифметического - добавляем в count
            count += 1
    print(count)
    count = 0  # сбрасываем значения перед следующей строкой
    total = 0


n = int(input())
matrix = [[int(num) for num in input().split()]for i in range(n)]  # создаем матрицу из n строк,
# заполненной числами num, for i in range(n) - цикл выполняется n раз по числу строк,
# input().split() - читаем строку и разбиваем ее на элементы,
# int(num) for num in... - превращаем каждый элемент в число
for i in range(n):  # проходим по каждой строке матрицы по индексам от 0 до n-1
    st = 0  # переменная-счетчик, сколько элементов в строке больше среднего
    mid = sum(matrix[i])/n  # среднее арифметическое строки, сумма элементов/на количество элементов
    for j in range(n):  # проходим по каждому элементу строки
        if matrix[i][j] > mid:  # проверка элемент больше среднего или нет
            st += 1
    print(st)


n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    avg = sum(lst) / len(lst)
    print(sum(i > avg for i in lst))


# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной
# матрицы(ниже главной диагонали).На вход программе подается натуральное число n – количество строк
# и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел. Программа должна
# вывести одно число – максимальный элемент в заштрихованной области квадратной матрицы.
# Элементы главной диагонали также учитываются.
n = int(input())
matrix = [[int(num) for num in input().split()] for i in range(n)]
count = float('-inf')  # вещественное число отрицательную бесконечность, чтобы любое число было больше
# начального значения
for i in range(n):
    for j in range(n):
        if i >= j:
            # count = max(count, matrix[i][j])
            if count < matrix[i][j]:
                count = matrix[i][j]
print(count)


n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
largest = matrix[0][0]
for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > largest:
            largest = matrix[i][j]
print(largest)


n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
a = []
for i in range(n):
    a.append(max(matrix[i][0:i+1]))
print(max(a))

# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# Правый и левый треугольники. На вход программе подается натуральное число n – количество строк и
# столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел. Программа должна
# вывести одно число – максимальный элемент в заштрихованной области квадратной матрицы. Элементы
# диагоналей также учитываются.
n = int(input())
matrix = [[int(num) for num in input().split()] for i in range(n)]
count = float('-inf')  # вещественное число отрицательную бесконечность, чтобы любое число было больше
# начального значения
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 - j):
            # count = max(count, matrix[i][j])
            if count < matrix[i][j]:
                count = matrix[i][j]
print(count)


n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
largest = matrix[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
print(largest)


n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
print(max(max(m[i][j], m[i][~j], m[~i][j], m[~i][~j]) for i in range(n // 2 + 1) for j in range(i + 1)))


n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
print(max(a[i][j] for i in range(n) for j in range(n) if j <= i <= n - j - 1 or j >= i >= n - j - 1))



