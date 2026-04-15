# На вход программе подаются две строки: на одной – символы, на другой – число n.
# Из первой строки формируется список. Реализуйте функцию chunked(), которая принимает на вход
# список и число, задающее размер чанка (куска), а возвращает список из чанков (кусков) указанной длины.

string = input().split()
n = int(input())

def chunked(lst, size):
    result = []
    # Идем по списку с шагом size
    for i in range(0, len(lst), size):  # цикл от начала по длине списка, с шагом на количество
        # элементов в списке

        result.append(lst[i: i + size])   # Отрезаем кусочек от текущего индекса до (текущий + size),
        # от начала среза до начала среза прибавить число элементов
    return result

print(chunked(string, n))



def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result
symbols = input().split()
n = int(input())
print(chunked(symbols, n))


def chunked(sp, n):
    return [sp[x:x + n] for x in range(0, len(sp), n)]
s = input().split()
n = int(input())
print(chunked(s, n))



def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    m = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    length = [0, 1, 2, 4]
    score = [0, 1, 3, 5]

    # 1. Проверка трассы
    for i in range(n - 1):
        if a[i] + length[b[i]] >= a[i + 1]:
            print(0)
            return

    # 2. Фильтрация прыжков (нельзя в воздухе)
    valid_jumps = []
    for i in range(m):
        if not valid_jumps:
            valid_jumps.append((x[i], y[i]))
        else:
            last_x, last_y = valid_jumps[-1]
            if x[i] >= last_x + last_y:
                valid_jumps.append((x[i], y[i]))

    # 3. Подсчёт очков
    res = 0
    j = 0

    for i in range(n):
        start = a[i]
        end = a[i] + length[b[i]]

        # сдвигаем прыжки
        while j < len(valid_jumps) and valid_jumps[j][0] + valid_jumps[j][1] < start:
            j += 1

        ok = False
        if j < len(valid_jumps):
            jump_start, jump_len = valid_jumps[j]
            if jump_start <= start and jump_start + jump_len >= end:
                ok = True

        if ok:
            res += score[b[i]]
        else:
            res -= 1

    print(max(0, res))




J = input()
S = input()
count = 0
for c in J:
    if c in S:
        count += 1
print(len(J) + count)

A, B = map(int, input().split())
print(A + B)

print('hello world!')

print('Hello, Yandex!')

numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1)
print(res)



import sys


def ask(indices):
    print("CHECK", len(indices), *indices)
    sys.stdout.flush()
    return list(map(int, sys.stdin.readline().split()))


def main():
    n = int(sys.stdin.readline())

    LOG = 9  # достаточно для n <= 500

    # mask[pos] = код части, стоящей на позиции pos
    mask = [0] * (n + 1)

    for bit in range(LOG):
        query = []
        for i in range(1, n + 1):
            if (i >> bit) & 1:
                query.append(i)

        if not query:
            continue

        response = ask(query)

        for pos in response:
            mask[pos] |= (1 << bit)

    # формируем ответ
    result = [0] * (n + 1)
    for pos in range(1, n + 1):
        result[pos] = mask[pos]

    print("RESULT", *result[1:])
    sys.stdout.flush()


if __name__ == "__main__":
    main()







def ask(indices):
    print("CHECK", len(indices), *indices)
    sys.stdout.flush()
    return list(map(int, sys.stdin.readline().split()))


def main():
    n = int(sys.stdin.readline())

    LOG = 9  # достаточно для n <= 500

    # mask[pos] = код части, стоящей на позиции pos
    mask = [0] * (n + 1)

    for bit in range(LOG):
        query = []
        for i in range(1, n + 1):
            if (i >> bit) & 1:
                query.append(i)

        if not query:
            continue

        response = ask(query)

        # response — список позиций, куда попали эти части
        for pos in response:
            mask[pos] |= (1 << bit)

    # формируем ответ: piece на позиции pos
    result = [0] * (n + 1)
    for pos in range(1, n + 1):
        result[pos] = mask[pos]

    print("RESULT", *result[1:])
    sys.stdout.flush()


if __name__ == "__main__":
    main()

