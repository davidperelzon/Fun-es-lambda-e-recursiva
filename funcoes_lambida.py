#função para calcular o reajuste de um produto em 30%

def calcular_reajuste(valor):
    return valor * 1.3


print(f"Preço: {calcular_reajuste(67)}")

#função lambida
reajuste = lambda x: x * 1.3
print(reajuste(1000))

#converter uma string em maiuscula

nome_lambda = lambda nome: nome.upper()
print(nome_lambda('juca'))

lista = ['ana', 'maria', 'carlos', 'pedro']
print(list(map(lambda nome: nome.upper(), lista)))

#retornar gerar uma lista só com valores pares

numeros = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, numeros)))