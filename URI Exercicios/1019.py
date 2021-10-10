N = int(input())

tempo = [n//60**2, (n%60**2)//60, n%60]
    
print("%d:%d:%d" % (tempo[0], tempo[1], tempo[2]))