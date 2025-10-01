from pprint import pprint  # importação para imprimir dicionários de forma melhor (recuso cosmético apenas)

# Dicionário (lista de elementos com índices não-inteiros)
# é declarado entre chaves, tem cada par índice-elemento seaparado por víruglas
# e o índice e o elemnto são separados por ":" (dois pontos)
dicio = {
    "string": "Oi Pessoal",
    "inteiro": 42,
    "flutuante": 42.24,
    "lista": ["Oi Pessoal", 42, 42.24]
}

pprint(dicio)