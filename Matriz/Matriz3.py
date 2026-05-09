coluna = []
for i in range (3):
    linha = []
    for j in range(3):
        N = int(input(f"Digite o numero pra posição {i}x{j}: "))
        linha.append(N)
    coluna.append(linha)
multiplicador = int(input("Digite um número para multiplicar todos os elementos da matriz: "))
for i in range (3):
    for j in range(3):
        print(coluna[i][j] * multiplicador,end=" ")
    print()
  