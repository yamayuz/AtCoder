# ABC 289 A - flip
# https://atcoder.jp/contests/abc289/tasks/abc289_a
# 

if __name__ == "__main__":
    s = list(input())
    
    for idx, i in enumerate(s):
        if i == '0':
            s[idx] = '1'
        else:
            s[idx] = '0'

    print(''.join(s))