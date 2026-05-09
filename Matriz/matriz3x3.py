coluna = []
for i in range (3):
    linha = []
    for j in range(3):
        N = int(input(f"Digite o numero pra posição {i}x{j}: "))
        linha.append(N)
    coluna.append(linha)
for i in range (3):
    for j in range(3):
        print(coluna[i][j],end=" ")
    print()
  