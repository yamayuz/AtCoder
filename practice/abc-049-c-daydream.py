# ABC 049 C - Daydream 
# https://atcoder.jp/contests/abc049/tasks/arc065_a
# 

if __name__ == "__main__":
    s = input()

    while s:
        for query in ("erase", "eraser", "dream", "dreamer"):
            if s.endswith(query):
                s = s[:-len(query)]
                break
        else:
            print('NO')
            exit()

    print('YES')