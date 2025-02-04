def tuplas_media_maior_5():
    """
    Solicita ao usuário uma sequência de tuplas separadas por ponto e vírgula,
    calcula a média de cada tupla e retorna uma lista com as tuplas cuja média
    é maior ou igual a 5.

    Returns:
        list: Lista de tuplas cuja média dos elementos é maior ou igual a 5.
    """
    entrada = input("Digite uma sequência de tuplas separadas por ponto e vírgula: ")

    # Converte a entrada para uma lista de tuplas de inteiros
    tuplas = [tuple(map(int, grupo.split(","))) for grupo in entrada.split(";")]

    # Filtra as tuplas cuja média seja maior ou igual a 5
    resultado = list(filter(lambda numeros: sum(numeros) / len(numeros) >= 5, tuplas))

    return resultado


tuplas_media = tuplas_media_maior_5()

print(f"Tuplas com média maior ou igual a 5: {tuplas_media}")
