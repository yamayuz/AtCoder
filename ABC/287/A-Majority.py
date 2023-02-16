
if __name__ == "__main__":
    n = int(input())
    a = [input() for i in range(n)]
    agreement = 0

    for i in a:
        if i == 'For':
            agreement += 1
        else:
            agreement -= 1

    if agreement > 0:
        print('Yes')
    else:
        print('No')