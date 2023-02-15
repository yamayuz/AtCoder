# ABC 088 B - Card Game for Two
# https://atcoder.jp/contests/abc088/tasks/abc088_b
# 

def solution_1():
    n = int(input())
    a = list(map(int, input().split()))
    alice = 0
    bob = 0

    for i in range(n):
        if i % 2 == 0:
            alice += a.pop(a.index(max(a)))
        else:
            bob += a.pop(a.index(max(a)))

    print(alice - bob)


def solution_2():
    n = int(input())
    a = list(map(int, input().split()))
    alice = 0
    bob = 0

    a.sort(reverse=True)
    print(sum(a[::2]) - sum(a[1::2]))


if __name__ == "__main__":
    solution_2()