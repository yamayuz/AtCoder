# ABC 081 A - Placing Marbles
# https://atcoder.jp/contests/abc081/tasks/abc081_a
# 


def solution_1():
    a = [input() for i in range(2)]
    b = list(map(int, a[1].split()))
    num = 0
    is_even = True

    for i in b:
        if i % 2 == 1: is_even = False
    
    while is_even:
        for idx, i in enumerate(b):
            b[idx] = i // 2
            if b[idx] % 2 == 1:
                is_even = False
                break
        num += 1

    print(num)


def solution_2():
    a = [input() for i in range(2)]
    b = list(map(int, a[1].split()))
    num = 0

    while True:
        exist_odd = False
        for i in b:
            if i % 2 == 1: exist_odd = True

        if exist_odd: break

        for idx, i in enumerate(b):
            b[idx] = i // 2

        num += 1
    print(num)


if __name__ == "__main__":
    solution_2()



    