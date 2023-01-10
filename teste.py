arquivo = open('pokemon.csv', 'r')
texto = arquivo.read()
linhas = texto.split('\n')

print(linhas)