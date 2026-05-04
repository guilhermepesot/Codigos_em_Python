import funcoes_evento as fe

for i in range(2):
    nome = input("Digite seu nome: ")
    tipo_ingresso = input("Qual o tipo do ingresso?(estudante/vip/regular): ")
    oficinas = int(input("Digite a quantidade de oficinas extras que vai participar: "))
    material_extra = input("Deseja material extra?(True/False): ")
    cupom = int(input("Digite o valor percentual do desconto: "))
    valor_base, valor_ofcina, valor_material, desconto, valor_taxa, valor_final, classificacao = fe.gerar_relatorio_participante(nome, tipo_ingresso, 120, oficinas, material_extra, cupom)
    print(f'Nome do participante: {nome}\nTipo de ingresso: {tipo_ingresso}\nValor base do ingresso: {valor_base:.2f}\nValor total das oficinas extras: {valor_ofcina}\nValor do material extra: {valor_material:.2f}\nValor do desconto aplicado: {desconto}\nValor da taxa administrativa: {valor_taxa:.2f}\nValor final da inscrição: {valor_final}\n Classificação da inscrição: {classificacao}')