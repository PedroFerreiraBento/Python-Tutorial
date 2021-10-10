X = int(input()) 
X = list(X + 1, X + (6 * 2), 2) if (X % 2 == 0) else list(X, X + (6 * 2), 2)
X = "\n".join(X)
print(X)