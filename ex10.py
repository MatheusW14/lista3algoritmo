from functools import reduce


def calcular_media_ponderada(dicionario):
    """
    Calcula a média ponderada de cada aluno em um dicionário.

    Args:
        dicionario (dict): Chaves são nomes dos alunos e valores são listas de notas (a última posição é o peso).

    Returns:
        dict: Novo dicionário com os alunos e suas médias ponderadas.
    """
    return dict(
        map(
            lambda item: (
                item[0],  # Nome do aluno
                round(
                    reduce(lambda acc, nota: acc + nota * item[1][-1], item[1][:-1], 0)
                    / (len(item[1]) - 1)
                    / item[1][-1],
                    1,
                ),
            ),
            dicionario.items(),
        )
    )


# Função para capturar entrada do usuário
def obter_dados():
    """
    Solicita ao usuário a entrada de dados no formato de alunos e suas notas,
    e retorna um dicionário com os nomes dos alunos como chaves e uma lista de
    suas notas como valores.

    A entrada deve ser no formato:
    "nome:nota1,nota2,...,peso;nome2:nota1,nota2,...,peso2;..."

    Returns:
        dict: Um dicionário onde as chaves são os nomes dos alunos (str) e os
        valores são listas de inteiros representando as notas dos alunos.
    """
    dicionario = dict(
        map(
            lambda entrada: (entrada[0], list(map(float, entrada[1].split(",")))),
            map(
                lambda x: x.split(":"),
                input(
                    "Digite os alunos e suas notas (nome:nota1,nota2,...,peso) separados por ponto e vírgula: "
                ).split(";"),
            ),
        )
    )
    return dicionario


dados_alunos = obter_dados()


medias = calcular_media_ponderada(dados_alunos)


print("\nMédias ponderadas:")
print(medias)
