arquivo = open('arquivo.txt', 'r', encoding="utf-8")
print(arquivo.read())
arquivo.seek(25)
print(arquivo.read())
