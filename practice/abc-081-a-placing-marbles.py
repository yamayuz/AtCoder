# ABC 081 A - Placing Marbles
# https://atcoder.jp/contests/abc081/tasks/abc081_a
# 

def solution_1():
    a = int(input())

    b = a // 100
    c = (a % 100) // 10
    d = ((a % 100) % 10) // 1
    print(b + c + d)


def solution_2():
    a = list(input())
    num = 0
    if (a[0] == '1'): num += 1
    if (a[1] == '1'): num += 1
    if (a[2] == '1'): num += 1
    print(num)


if __name__ == "__main__":
    solution_1()
    # solution_2()
