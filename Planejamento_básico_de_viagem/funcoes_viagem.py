def calcular_passagem(valor_base, bagagem=0):
    valor_passagem = valor_base + bagagem
    return valor_passagem

def calcular_hospedagem(valor_diaria, dias=1, taxa_extra=0):
    valor_hospedagem = (valor_diaria * dias) + taxa_extra
    return valor_hospedagem
    
def converter_duracao(total_horas):
    dias = total_horas // 24
    horas = total_horas % 24
    return dias, horas

def calcular_orcamento(passagem, hospedagem, alimentacao=0):
    custo_fixo = passagem + hospedagem
    custo_extra = alimentacao
    custo_tot = custo_fixo + custo_extra
    return custo_fixo, custo_extra , custo_tot
