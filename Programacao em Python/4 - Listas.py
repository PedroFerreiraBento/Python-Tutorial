# Listas

"""
Posicoes de uma lista
Pra frente: 0,  1,  2,  3,  4,  5
Pra tras:   6, -5, -4, -3, -2, -1

Ex: 
lista = ["A", "B", "C", "D", "E", "F"]

lista[0] -> Resultado: A
lista[-1] -> Resultado: F
"""

# Declaracao inicial
variavel = [1, 2, 3]

# Adcionar um elemento ao final da lista
variavel.append(6) # [1, 2, 3, 6]

# Adcionar um elemento na posicao informada
variavel.insert(2, 10) # [1, 2, 10, 3, 6]

# Inverter a lista
variavel.reverse() # [6, 3, 10, 2, 1]

# Ordena a lista
variavel.sort() # [1, 2, 3, 6, 10]

# Posicao de um elemento
variavel.index(6) # 3

# Mesclar listas
variavel += [1, 2, 3] # [1, 2, 3, 6, 10, 1, 2, 3]
variavel.extend(["A", "B", "C"]) # [1, 2, 3, 6, 10, 1, 2, 3, "a", "b", "c"]

# Contar elementos em uma lista
variavel.count(3) # 2

# Limpa a lista
variavel.clear() # []