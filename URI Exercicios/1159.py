while True:
    X = int(input())
    if X == 0:
        break
    X = list(range(X + 1, X + (5 * 2), 2)) if (X % 2 == 1) else list(range(X, X + (5 * 2), 2))
    print(sum(X))