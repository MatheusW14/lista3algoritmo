from functools import reduce


def soma_numeros():
    """
    Solicita ao usuário uma sequência de números inteiros separados por vírgula,
    soma todos os números da sequência e retorna o resultado.
    Returns:
        int: A soma de todos os números inteiros fornecidos pelo usuário.
    """

    numeros = []  # Lista para armazenar os números
    entrada = input("Digite uma sequencia de numeros inteiros separados por virgula: ")

    numeros = list(map(int, entrada.split(",")))

    resultado = reduce(lambda x, y: x + y, numeros)

    return resultado


soma = soma_numeros()

print(f"A soma dos números é: {soma}")
