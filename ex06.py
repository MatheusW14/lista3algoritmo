def lista_pares_impares():
    """
    Solicita ao usuário uma sequência de números inteiros separados por vírgula,
    separa os números em pares e ímpares, e retorna um dicionário contendo duas listas:
    uma com os números pares e outra com os números ímpares.
    Returns:
        dict: Um dicionário com duas chaves:
            - "pares": lista de números pares.
            - "impares": lista de números ímpares.
    """

    numeros = []  # Lista para armazenar os números

    entrada = input("Digite uma sequencia de numeros inteiros separados por virgula:")
    numeros = list(map(int, entrada.split(",")))

    pares = list(filter(lambda x: x % 2 == 0, numeros))
    impares = list(filter(lambda x: x % 2 != 0, numeros))

    return {"pares": pares, "impares": impares}


resultado = lista_pares_impares()
print(f"Os numeros digitados foram: {resultado}")
