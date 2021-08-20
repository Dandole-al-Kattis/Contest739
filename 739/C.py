if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        k = int(input())
        a, x, i = 1, 1, 1
        while(k >= x + a):
            x += a
            a += 2
            i += 1
        m = k-x+1
        if m <= i:
            print(m, i)
        else:
            print(i, (i-(m-i)))
            
        
        
