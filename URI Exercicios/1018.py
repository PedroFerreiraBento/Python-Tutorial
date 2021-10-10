N = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print(N)
for i in notas:
    print("%d nota(s) de R$ %d,00" % (N // i, i))
    N %= i 