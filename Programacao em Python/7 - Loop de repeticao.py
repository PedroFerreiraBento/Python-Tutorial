# 7 - Loops

# FOR - Para cada elemento execute os seguintes comandos
lista = ["A", "B", "C"]

for i in lista:
    print(i, end=",") 

"""
    1 loop - A,
    2 loop - A,B,
    3 loop - A,B,C,
"""

for i in range(3):
    print(i, end=",") 

"""
    1 loop - 0,
    2 loop - 0,1,
    3 loop - 0,1,2,
"""

# WHILE - Execute os comando ENQUANTO a condicao for verdadeira
x = 3
while x > 0:
    print(x)
    x -= 1 

"""
    1 loop - 3
    2 loop - 2
    3 loop - 1
"""