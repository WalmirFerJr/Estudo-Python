# Pode ser instanciado assim:
lista = list()
# ou assim:
lista = []

# ".append" adiciona um elemento no final de uma lista
lista.append("Python")
lista.append(42)
lista.append(( "Um", "exemplo", "de", "tupla" ))
lista.append(22.34)
lista # vários tipos de dados num mesmo lugar!

print(lista[1])

# Podemos usar os índices normalmente
print(lista[0], lista[1], lista[2], sep=" - ")

# Mas existem também índices negativos! (a contagem é feita de traz para frente)
# -1 -> Último item da lista, -2 -> Penúltimo, -3 -> Antepenúltimo, etc...
print(lista[-1], lista[-2], lista[-3], sep=" - ")