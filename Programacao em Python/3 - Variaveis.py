# Variaveis
# Nomeacao - Nao pode:
#   - Iniciar com numeros ou caracteres especiais, com excessao do "_". 
#       Ex: 1Nome, 25Idade, *Cidade, ...
#
#   - Possuir qualquer caractere especial com excessao do "_" (Underline)
#       Ex: nome!Completo, cidade&pais, ...
#
#   - Ter espacos
#       Ex: Nome e Sobrenome, Aniversario do cliente, ...
#
#   - Ser uma das 'Palavras reservadas' da linguagem
#       Ex: print, int, str, sum, True, ...


# Tipos de variaveis
# Inteiro: int
variavel = 10

# Ponto flutuante: float
variavel = 12.5

# Texto(String): str
variavel = "Nome"
variavel = 'Nome'

# Boolean(Verdadeiro ou Falso): bool 
variavel = True
variavel = False

# Nulo: NoneType
variavel = None

# Array/Lista: list
variavel = [1, 2, "Nome"]
variavel = [[1, 2, 3], ["a", "b", "c"]] # Matriz

# Tuplas: tuple
variavel = ("batata", 1, 2, 3) # OBS: Nao alteravel

# Dicionario: dict
variavel = {"nome": "Victor", "idade": 18}

# Verificar o tipo da variavel: type()
print(type(variavel))

# Conversoes
int(variavel) # Converter para Inteiro
float(variavel) # Converter para Float
str(variavel) # Converter para String
bool(variavel) # Converter para Boolean
list(variavel) # Converter para Lista
tuple(variavel) # Converter para Tupla
dict(variavel) # Converter para Dicionario

# Excluir variavel
del variavel