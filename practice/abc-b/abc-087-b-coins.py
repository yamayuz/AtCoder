# ABC 087 B - Coins
# https://atcoder.jp/contests/abc087/tasks/abc087_b
# 

if __name__ == "__main__":
    a, b, c, x = [int(input()) for i in range(4)]
    res = 0

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if (500*i + 100*j + 50*k) == x:
                    res += 1

    print(res)