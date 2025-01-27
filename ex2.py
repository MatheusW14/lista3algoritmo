def numero_par_na_lista():
    """
    Solicita ao usuário uma sequência de números inteiros separados por espaço,
    filtra os números pares e retorna uma lista contendo esses números pares.
    Returns:
        list: Uma lista de números inteiros pares.
    """

    entrada = input("Digite uma sequencia de numeros inteiros separados por espaço: ")

    pares = list(filter(lambda x: x % 2 == 0, map(int, entrada.split())))
    # map(int, entrada.split()): Converte os números da entrada (string) em inteiros.
    # # filter(lambda x: x % 2 == 0, ...): Filtra apenas os números pares.

    return pares


pares = numero_par_na_lista()

print(f"Os números pares na lista são: {pares}")
