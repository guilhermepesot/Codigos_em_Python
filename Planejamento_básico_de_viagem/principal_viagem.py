import funcoes_viagem as fv

valor_base = float(input("Digite o valor da passagem: "))
bagagem = float(input("Digite o valor da bagagem: "))

valor_diaria = float(input("Digite o valor da diária do hotel: "))
dias = int(input("Digite quantos dias ficou hospedado: "))
taxa_extra = float(input("Digite o valor da taxa extra: "))

duracao_viagem = int(input("Digite duração total da viagem em horas: "))

valor_alimentacao = float(input("Digite o valor do gasto com alimentação: "))

valor_passagem = fv.calcular_passagem(valor_base, bagagem)
valor_hospedagem = fv.calcular_hospedagem(valor_diaria, dias, taxa_extra)
dias, horas = fv.converter_duracao(duracao_viagem)
custo_fixo, custo_extra, custo_tot = fv.calcular_orcamento(valor_passagem, valor_hospedagem, valor_alimentacao )

print(f'O valor final da passagem é de R${valor_passagem:.2f}')
print(f'O valor final da hospedagem é de R${valor_hospedagem:.2f}')
print(f'A duração convertida em dias e horas {dias} dias {horas} horas')
print(f'O custo fixo para a viagem é de R${custo_fixo:.2f}')
print(f'O custo extra para a viagem é de R${custo_extra:.2f}')
print(f'O custo total para a viagem é de R${custo_tot:.2f}')