# 9 - Classes

class Calculadora: # Nome inicia com um letra maiuscula
    # Definicao de atributos
    a = 0
    b = 0

    # Inicializador da classe: __init__
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Definicao de Metodos
    def somar(self):
        print(self.a + self.b)

    def subtrair(self):
        print(self.a - self.b)
        
    def multiplicar(self):
        print(self.a * self.b)
        
    def dividir(self):
        print(self.a / self.b)

# Instanciar Objeto
variavel = Calculadora(10, 5)

# Executar um metodo da classe
variavel.somar()

# Alterar atributos
variavel.a = 20
variavel.multiplicar()
