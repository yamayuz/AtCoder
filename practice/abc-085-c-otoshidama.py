# ABC 085 C - Otoshidama
# https://atcoder.jp/contests/abc085/tasks/abc085_c
# 

if __name__ == "__main__":
    n, y = map(int, input().split())

    result = [-1, -1, -1]
    for i in range(n+1):
        for j in range(n+1-i):
            k = n - i - j
            total = 10000*i + 5000*j + 1000*k
            if total == y:
                result = [i, j, k]

    print(f'{result[0]} {result[1]} {result[2]}')
