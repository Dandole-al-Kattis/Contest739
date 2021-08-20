table = []

i = 1
while len(table) < 1000:
    if i % 3 != 0 and i % 10 != 3:
        table.append(i)
    i += 1

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        k = int(input())
        print(table[k-1])
