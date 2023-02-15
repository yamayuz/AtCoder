

if __name__ == "__main__":
    n = int(input())
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    
    for i in range(n):
        print(x[i] + y[i])
