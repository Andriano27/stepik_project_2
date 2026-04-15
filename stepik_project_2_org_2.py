



def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    m = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    length = [0, 1, 2, 4]
    score = [0, 1, 3, 5]

    for i in range(n - 1):
        if a[i] + length[b[i]] >= a[i + 1]:
            print(0)
            return

    res = 0

    for i in range(n):
        start = a[i]
        end = a[i] + length[b[i]]

        ok = False
        for j in range(m):
            if x[j] <= start and x[j] + y[j] >= end:
                ok = True
                break

        if ok:
            res += score[b[i]]
        else:
            res -= 1

    print(max(0, res))


# 👇 ВАЖНО
solve()

############################################################

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

    # 2. Подготовка прыжков
    jumps = [(x[i], x[i] + y[i]) for i in range(m)]
    jumps.sort()  # сортируем по началу

    res = 0
    j = 0
    max_right = -1

    # 3. Обработка платформ
    for i in range(n):
        start = a[i]
        end = a[i] + length[b[i]]

        # добавляем все прыжки, которые начинаются до start
        while j < m and jumps[j][0] <= start:
            max_right = max(max_right, jumps[j][1])
            j += 1

        if max_right >= end:
            res += score[b[i]]
        else:
            res -= 1

    print(max(0, res))


if __name__ == "__main__":
    solve()


