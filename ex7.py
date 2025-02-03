def agrupar_numeros():

    numeros = []

    entrada = input("Digite uma sequencia de numeros inteiros separados por virgula:")
    numeros = list(map(int, entrada.split(",")))

    positivos = list(filter(lambda x: x > 0, numeros))
    negativos = list(filter(lambda x: x < 0, numeros))
    zeros = list(filter(lambda x: x == 0, numeros))

    return {"positivos": positivos, "negativos": negativos, "zeros": zeros}


resultado = agrupar_numeros()
print(f"{resultado}")
