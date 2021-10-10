
# Metodo 3
# X = list(X+1, X+(6*2), 2) if (X % 2 == 0) else list(X, X+(6*2), 2)
# X = "\n".join(X)
# print(X)

# Metodo 2
# if X % 2 == 0:
#     X = list(range(X+1, X+(6*2), 2)) # [9, 11, 13, 15, 17]
# for i in X:
#     print(i)


# Metodo 1
# if X % 2 == 0:
#     X+=1
#     print(X)
# for i in range(0,5):
#     X+=2
#     print(X)
# -----------------------------------------------------

X = int(input()) # 8
if X % 2 == 0: # Par
    X += 1
print(X)
i = 1
while i <=5:
    X += 2
    print(X)
    i +=1