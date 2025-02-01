def nome_cinco_letras():

    entrada = input("Digite uma lista de nomes separados por uma virgula: ")

    nomes = [nome.strip() for nome in entrada.split(",")]

    nomes_filtrados = list(filter(lambda x: len(x) >= 5, nomes))

    return nomes_filtrados


nomes = nome_cinco_letras()
print(f"Os nomes com cinco letras ou mais são: {nomes}")
