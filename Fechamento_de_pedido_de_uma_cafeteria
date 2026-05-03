import funcoes_cafeteria as fc

nome = input("Digite o nome do café: ")
preco_base = float(input("Digite o preço do café: "))
tam = input("Digite o tamanho do café (P/M/G): ")
if tam == 'p' or tam == 'P':
    acrescimo = 2.0
elif  tam == 'm' or tam == 'M':
    acrescimo = 4.0
elif  tam == 'g' or tam == 'G':
    acrescimo = 6.0
else:
    acrescimo = 0.0

nome_acomp = input("Digite o nome do acompanhamento: ")
preco_acomp = float(input("Digite o valor do acompanhamento: "))
desconto_acomp = int(input("Digite o desconto do acompanhamento em percentual: "))
taxa_servico = int(input("Digite a taxa de serviço em percentual: "))

final_cafe = fc.calcular_preco_cafe(preco_base,acrescimo)
print(fc.resumo_item ( nome , final_cafe )) 

final_acomp = fc.calcular_acompanhamento( preco_acomp , desconto_acomp )
print(fc.resumo_item( nome_acomp , final_acomp ))

subtotal, valor_taxa, valor_final = fc.calcular_totais(final_cafe,final_acomp,taxa_servico)
print(f'Subtotal: {subtotal}, valor da taxa: {valor_taxa} , Valor final da compra: {valor_final}')
