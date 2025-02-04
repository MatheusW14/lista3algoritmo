def nome_cinco_letras():
    """
    Solicita ao usuário uma lista de nomes separados por vírgula, filtra e retorna os nomes que possuem
    cinco ou mais letras.
    Returns:
        list: Uma lista contendo os nomes que possuem cinco ou mais letras.
    """

    entrada = input("Digite uma lista de nomes separados por uma virgula: ")

    nomes_lista = [nome.strip() for nome in entrada.split(",")]

    nomes_filtrados = list(filter(lambda x: len(x) >= 5, nomes_lista))

    return nomes_filtrados


nomes = nome_cinco_letras()
print(f"Os nomes com cinco letras ou mais são: {nomes}")
