nota_1 = int(input("Escreva a sua nota 1: "))
nota_2= int(input("Escreva a sua nota 2: "))
media = (nota_1 + nota_2)/2
if ( nota_1 < 0 or nota_2 < 0):    # aqui confere se OU a nota 1 OU a nota 2 é < 0, impossivel ter essa nota;
    print("Inváldo")
else:
    print("Sua média é: {:.2f}".format(media))  #duas casas após a virgula;
