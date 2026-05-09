def ler_matriz(tam, numero):
    matriz = []
    for i in range(tam):
        linha = []
        for j in range(tam):
            N = int(input(f"Digite o numero pra posição {i}x{j} da matriz {numero}: "))
            linha.append(N)
        matriz.append(linha)
    return matriz

tam = int(input("Digite o tamanho da matriz quadrada: "))

matriz_1 = ler_matriz(tam, 1)
matriz_2 = ler_matriz(tam, 2)

for i in range(tam):
    for j in range(tam):
        print(matriz_1[i][j] + matriz_2[i][j], end=" ")
    print()