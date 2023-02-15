# ABC 083 B - Some Sums
# https://atcoder.jp/contests/abc083/tasks/abc083_b
# 

def findSumOfDigits(n: int):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


if __name__ == "__main__":
    n, a, b = list(map(int,input().split()))
    total = 0

    for i in range(1, n + 1):
        sum = findSumOfDigits(i)
        if a <= sum and sum <= b:
            total += i
        
    print(total)
  