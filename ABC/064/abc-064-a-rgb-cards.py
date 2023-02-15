# ABC 064 A - RGB Cards
# https://atcoder.jp/contests/abc064/tasks/abc064_a
# 


if __name__ == "__main__":
    r, g, b = map(int, input().split())
    
    num = r*100 + g*10 + b
    if num % 4 == 0:
        print('YES')
    else:
        print('NO')