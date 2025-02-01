def elevar_ao_quadrado_ordenar():
    """
    Lê uma sequência de números inteiros separados por vírgula, eleva cada número ao quadrado,
    ordena os resultados em ordem crescente e retorna a lista ordenada.
    Returns:
        list: Lista de números inteiros elevados ao quadrado e ordenados em ordem crescente.
    """

    numeros = []  # Lista para armazenar os números

    entrada = input("Digite uma sequencia de numeros inteiros separados por virgula:")
    numeros = list(map(int, entrada.split(",")))
    resultado = map(lambda x: x**2, numeros)
    resultado = sorted(resultado)
    return resultado


numeros_ordenados = elevar_ao_quadrado_ordenar()
print(f"Os numeros elevados ao quadrado e ordenados são: {numeros_ordenados}")
