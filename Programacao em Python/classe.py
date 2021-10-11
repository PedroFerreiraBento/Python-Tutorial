class Calculadora:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def som(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b

l = [3,1,4,3]
print(l.count(3))