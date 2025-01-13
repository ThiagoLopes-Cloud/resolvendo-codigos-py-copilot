#Vamos testar se uma palavra é um palíndromo?!
def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')