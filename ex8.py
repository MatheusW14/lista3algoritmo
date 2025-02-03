from functools import reduce


def contar_letras():
    """
    Solicita ao usuário uma sequência de palavras separadas por vírgula,
    remove os espaços em branco ao redor de cada palavra, e calcula a soma
    do número de letras de todas as palavras.
    Returns:
        int: A soma do número de letras de todas as palavras fornecidas.
    """

    entrada = input("Digite uma sequencia de palavras separadas por vírgula:")

    nomes_lista = [nome.strip() for nome in entrada.split(",")]

    soma_letras = reduce(lambda x, y: x + y, map(len, nomes_lista))

    return soma_letras


soma_letras = contar_letras()
print(f"A soma das letras corresponde a:{soma_letras}")
