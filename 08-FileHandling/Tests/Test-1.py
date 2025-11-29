plik = open('abc.txt', 'r')
content = plik.read()
plik.close()

with open('abc.txt', 'r') as plik:
    content = plik.read()