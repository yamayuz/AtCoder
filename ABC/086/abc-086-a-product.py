# ABC 086 A - Product
# https://atcoder.jp/contests/abc086/tasks/abc086_a
# 

if __name__ == "__main__":
    a, b = map(int, input().split())
    c = a * b

    if (c % 2 == 0):
        print('Even')
    else:
        print('Odd')
