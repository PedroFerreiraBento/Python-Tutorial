# 8 - Funcoes

# Funcao sem parametro e sem retorno
def hello_wolrd():
    print("Hello Wolrd")

hello_wolrd() # Resultado: Hello Wolrd

# Funcao com parametro e sem retorno
def bom_dia(nome):
    print("Bom dia:", nome)

bom_dia("Jorge") # Resultado: Bom dia: Jorge

# Funcao sem parametro e com retorno
def boa_noite():
    return "Boa Noite!"

print(boa_noite()) # Resultado: Boa Noite!

# Funcao com parametro e com retorno
def somar(a, b):
    return a + b

print(somar(10, 5)) # Resultado: 15
