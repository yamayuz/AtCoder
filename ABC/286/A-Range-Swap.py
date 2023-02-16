
def solution_1():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))

    j = r - 1
    for i in range(p-1, q):
        t = a[i]
        a[i] = a[j]
        a[j] = t
        j += 1

    print(*a)


def solution_2():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(p-1, q):
        a[i], a[r-p+i] = a[r-p+i], a[i]

    print(*a)


if __name__ == "__main__":
    solution_1()
