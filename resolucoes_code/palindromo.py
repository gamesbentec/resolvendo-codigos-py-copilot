# Verificando se uma palavra é um palíndromo

palavra = input("Digite uma palavra: ").lower()

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')

# Exemplo 1

Digite uma palavra: arara
"arara" é um palíndromo.

# Exemplo 2

Digite uma palavra: python
"python" não é um palíndromo.
