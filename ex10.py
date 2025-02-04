from functools import reduce


def calcular_media_ponderada(dicionario):
    """
    Calcula a média ponderada de cada aluno em um dicionário.

    Args:
        dicionario (dict): Chaves são nomes dos alunos e valores são listas de notas (a última posição é o peso).

    Returns:
        dict: Novo dicionário com os alunos e suas médias ponderadas.
    """
    medias = {}

    for aluno, valores in dicionario.items():
        notas, peso = valores[:-1], valores[-1]  # Separa notas e peso

        soma_ponderada = reduce(
            lambda acc, nota: acc + nota * peso, notas, 0
        )  # Soma das notas ponderadas, acc (acumulador): Mantém a soma acumulada. Começa em 0 (valor inicial).
        media = soma_ponderada / (len(notas) * peso)  # Média ponderada

        medias[aluno] = round(media, 1)  # Armazena com 1 casa decimal

    return medias


medias = calcular_media_ponderada()
print(medias)
