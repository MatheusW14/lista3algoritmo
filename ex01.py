def lista_numeros_int():
    """
    Solicita ao usuário uma sequência de números inteiros separados por espaço,
    multiplica cada número por 2 e retorna uma lista com os resultados.
    Returns:
        list: Lista contendo os números inteiros multiplicados por 2.
    """
    numeros = []  # Lista para armazenar os números
    entrada = input("Digite uma sequencia de numeros inteiros separados por espaço: ")

    numeros = list(
        map(int, entrada.split())
    )  # Multiplicar cada número por 2 usando map e lambda

    resultado = map(lambda x: x * 2, numeros)

    return list(resultado)  # Retorna o resultado como uma lista


numeros_dobrados = lista_numeros_int()

print(f"Os números dobrados são: {numeros_dobrados}")
