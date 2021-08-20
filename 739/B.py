

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        a, b, c = list(map(int, input().split()))
        n = 2*abs(a-b)
        if a > n or b > n or c > n:
            print(-1)
        else:
            d = c + (n//2)
            while d > n:
                d -= n
            print(d)
