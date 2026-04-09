n = int(input())        # на вход дается одно число, если оно нечетное, при делении
people = (n + 1) // 2   # пополам должно получаться число на единицу больше половины.

# Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2
# и возвращающую значение True если число num1 делится без остатка на число num2 и False в противном случае.
# Результатом вывода программы должно быть "делится" (если функция func() вернула True) или "не делится"
# (если функция func() вернула False).

# объявление функции
def func(num1, num2):
    return num1 % num2 == 0
# считываем данные
num1, num2 = int(input()), int(input())
# вызываем функцию
if func(num1, num2):
    print('делится')
else:
    print('не делится')

n = 3
list1 = []
for _ in range(n):
    row = input().split()
    list1.extend(row)
print(list1)

my_list = [[1], [2, 3], [4, 5, 6]]
total = 0
for row in my_list:
    total += sum(row)
print(total)

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
maximum = my_list[0][0]
minimum = my_list[0][0]
for row in my_list:
    maxi = max(row)
    mini = min(row)
print(maximum + minimum)

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
maximum = my_list[0][0]
minimum = my_list[0][0]
for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)
print(maximum + minimum)

# На вход программе подается число n. Напишите программу, которая создает и выводит построчно список,
# состоящий из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
n = int(input())
for _ in range(n):
    print(list(range(1, n + 1)))

n = int(input())
result = []
for _ in range(n):
    result.append(list(range(1, n + 1)))
print(*result, sep='\n')

# На вход программе подается число n. Напишите программу, которая создает и выводит построчно вложенный
# список, состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
n = int(input())
my_list = [list(range(1, i+1)) for i in range(1, n + 1)]
for row in my_list:
    print(row)

n = int(input())
result = []
for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))
print(*result, sep='\n')

[print(list(range(1, x + 2))) for x in range(int(input()))]

n = int(input())
for i in range(1, n + 1):
    print(list(range(1, i + 1)))

# Треугольник Паскаля – бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом
# треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним
# чисел.
# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....
#
#
# На вход программе подается число n. Напишите программу, которая возвращает указанную строку
# треугольника Паскаля в виде списка (нумерация строк начинается с нуля).
def pascal(n):
    row = [1]
    for i in range(n):
        new_row = [1]
        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])
        new_row.append(1)
        row = new_row
    return row
n = int(input())
print(pascal(n))

n = int(input())
li = [1]
for i in range(n):
    for j in range(len(li) - 1):
        li[j] = li[j] + li[j + 1]
    li.insert(0, 1)
print(li)


from math import factorial
n = int(input())
b = []
for i in range(n+1):
    b.append(int((factorial(n))/(factorial(i)*factorial(n-i))))
print(b)

# На вход программе подается натуральное число n. Напишите программу, которая выводит первые
# n строк треугольника Паскаля.
from math import *
n = int(input())
for i in range(n):
    my_list = []
    for j in range(n):
        if i < j:
            break
        else:
            my_list.append(int(factorial(i)//(factorial(j) * factorial(i - j))))
    print(*my_list)


def pascal(n):
    # результирующая таблица
    seq = [[1]]
    # начальная строка
    cur_seq = [1]
    for _ in range(n - 1):
        # добавляем нули по бокам к текущей строке строке
        cur_seq = [0] + cur_seq + [0]
        # тут будет храниться новая строка
        new_seq = []
        for i in range(len(cur_seq) - 1):
            # добавляем в новую строку сумму соседних элементов текущей строки
            new_seq.append(cur_seq[i] + cur_seq[i + 1])
        # теперь новая строка становится нашей текущей строкой
        cur_seq = new_seq
        # добавляем текущую строку в результирующую таблицу
        seq.append(cur_seq)
    return seq
n = int(input())
seq = pascal(n)
# выводим таблицу по строкам
for s in seq:
    print(*s)

def pascal(n):
    pas, pas2 = [1], [1, 1]
    print(*pas)
    for i in range(1, n):
        pas, pas2 = pas2, [1,1]
        for j in range(1, len(pas)):
            pas2.insert(1, pas[j] + pas[j - 1])
        print(*pas)
pascal(int(input()))

# На вход программе подается строка текста, содержащая символы. Напишите программу, которая
# упаковывает последовательности одинаковых символов заданной строки в подсписки.
s = input()
st = s.split()
my_list = []
for c in st:
    if not my_list or c != my_list[-1][0]:  # если список пуст или символ отличается от последнего символа в последнем вложенном списке
        my_list.append([c])  # создаем новый вложенный список
    else:
        my_list[-1].append(c)  # добавляем к существующему вложенному списку, если повтор
print(my_list)

s = input().split()
# кидаем первый символ в наш список, также удалив его из входного списка
seq = [[s.pop(0)]]
for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])
print(seq)

s = ''.join(input().split())    # входные данные переводим в строку
lst_in = [s[0]]                 # первый элемент строки
lst = [lst_in]                  # создаем вложенный список
for i in range(1, len(s)):      # пробегаем по строке со второго символа
    if s[i] in lst_in:          # если символ во вложенном списке, добавляем
        lst_in.append(s[i])
    else:                       # если нет, то
        lst_in = [s[i]]         # создаем вложенный список из нового символа
        lst.append(lst_in)      # добавляем во внешний список новый вложенный
print(lst)


