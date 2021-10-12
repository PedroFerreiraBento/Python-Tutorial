# 5 - Fateamento (Strings e Listas)

# Lista/String[Inicio:Fim:Steps]

variavel = "Learn Python"
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Primeiro elemento
variavel[0]         # Resultado: L
lista[0]            # Resultado: 1

# Ultimo elemento
variavel[-1]        # Resultado: n
lista[-1]           # Resultado: 9

# Primeiros cinco elementos
variavel[: 5]       # Resultado: Learn
lista[: 5]          # Resultado: [1, 2, 3, 4, 5]

# Ultimos cinco elementos
variavel[-5  :]     # Resultado: ython
lista[-5 : ]        # Resultado: [5, 6, 7, 8, 9]

# Lista alternada
variavel[::2]       # Resultado: LanPto
lista[::2]          # Resultado: [1, 3, 5, 7, 9]

# Lista invertida
variavel[::-1]      # Resultado: nohtyP nraeL
lista[::-1]         # Resultado: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Separar String
variavel.split(" ") # Resultado: ["Learn", "Python"]

# Juntar listas
"-".join(lista) # Resultado: 1-2-3-4-5-6-7-8-9