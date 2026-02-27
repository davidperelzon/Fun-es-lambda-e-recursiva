# 1. Dobro dos Números
numeros = [5, 12, 7, 15, 10]
quadrados = list(map(lambda x: x ** 2, numeros))
print("Quadrados dos números:", quadrados)

# 2. Filtragem de Strings Curtas
nomes = ["Ana", "Beatriz", "Caio", "Daniela", "Edu"]
nomes_curtos = list(filter(lambda nome: len(nome) <= 3, nomes))
print("Nomes com 3 letras ou menos:", nomes_curtos)

# 3. Ordenação Personalizada
produtos = [("Teclado", 150), ("Mouse", 80), ("Monitor", 900)]
produtos_ordenados = sorted(produtos, key=lambda produto: produto[1])
print("Produtos ordenados pelo preço:", produtos_ordenados)

# 4. Soma de Lista
def soma_lista(lista):
    if not lista:  
        return 0
    return lista[0] + soma_lista(lista[1:]) 

numeros = [5, 12, 7, 15, 10]
soma = soma_lista(numeros)
print("Soma dos números da lista:", soma)

# 5. Contagem Regressiva
def contagem_regressiva(n):
    if n < 0:  
        return
    print(n)
    contagem_regressiva(n - 1) 

print("Contagem regressiva:")
contagem_regressiva(5)

# 6. Sequência de Fibonacci
def fibonacci(n):
    if n == 0:  
        return 0
    elif n == 1:  
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
print(f"{n} termo da sequência de Fibonacci:", fibonacci(n))