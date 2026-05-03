import funcoes_treino as ft

calorias_base = int(input("Digite a quantidade base de calorias gastas em um treino: "))
bonus = int(input("Digite a quantidade de calorias bonus gastas em atividade complementar: "))

tempo_principal = int(input("Digite qunto tempo gasto no treino: "))
aquecimento = int(input("Digite qunto tempo gasto no aquecimento: "))

meta_semanal = int(input("Digite sua meta semanal: "))

gasto_tot = ft.calcular_calorias(calorias_base, bonus)
tempo_tot = ft.calcular_tempo_treino(tempo_principal, aquecimento)
horas, minutos = ft.analisar_desempenho(tempo_tot)
diferenca_cal, atingiu, mensagem = ft.consolidar_treino(gasto_tot, tempo_tot, meta_semanal)

print(f"Calorias totais: {gasto_tot}")
print(f"Tempo total: {tempo_tot} minutos ({horas}h {minutos}min)")
print(f"Diferença para a meta: {diferenca_cal}")
print(f"Meta atingida: {atingiu}")
print(f"Resumo: {mensagem}")