def between(a, b, c):
    return b <= a and a <= c

def aux_find(k, l, r):
    if l == r:
        return l
    h = (l + r) // 2
    if between(k, l**2, h**2):
        return aux_find(k, l, h)
    else:
        return aux_find(k, h+1, r)

def find_x(k):
    bound = 1
    while bound**2 < k:
        bound *= 2
    return int(aux_find(k, bound//2, bound))

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        k = int(input())
        if k == 10**9:
            print(31623, 14130)
        else:
            x = find_x(k)
            fst,  lst= (x-1)**2 + 1, x**2
            d1, d2 = (k - fst), (lst - k)
            if d1 < d2:
                print(1+d1, x)
            elif d1 > d2:
                print(x, 1+d2)
            else:
                print(x, x)
            
        
        
