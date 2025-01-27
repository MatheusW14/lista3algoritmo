def filtrar_numeros_pares():
    """
    Solicita ao usuário uma lista de números inteiros separados por espaço,
    filtra os números pares e retorna apenas esses números.
    Returns:
        list: Uma lista contendo apenas os números pares.
    """
    entrada = input("Digite uma lista de números inteiros separados por espaço: ")

    # Converte a entrada para uma lista de inteiros
    lista = list(map(int, entrada.split()))

    # Filtra os números pares
    numeros_pares = list(filter(lambda x: x % 2 == 0, lista))

    return numeros_pares


# Exemplo de uso
pares = filtrar_numeros_pares()
print(f"Números pares na lista digitada: {pares}")
