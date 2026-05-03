def calcular_calorias(calorias_base, bonus=0):
    calorias_final = calorias_base + bonus
    return calorias_final


def calcular_tempo_treino(tempo_principal, aquecimento=10):
    tempo_total = tempo_principal + aquecimento
    return tempo_total


def analisar_desempenho(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return horas, minutos 

def consolidar_treino(calorias, tempo, meta=300):
    atingiu = False
    mensagem = "Meta não atingida"
    diferenca_cal = calorias - meta
    if calorias >= meta:
        atingiu = True
        mensagem = "Meta atingida"
        return diferenca_cal, atingiu, mensagem
    return diferenca_cal, atingiu, mensagem
