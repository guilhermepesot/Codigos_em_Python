def calcular_valor_base(tipo_ingresso, valor_padrao=120):
    if tipo_ingresso == 'estudante':
        return valor_padrao * 0.6
    elif tipo_ingresso == 'vip':
        return valor_padrao * 1.5
    else:
        return valor_padrao
        
def calcular_extras(valor_base, oficinas=0, material_extra=False):
    valor_ofcina = oficinas * 30
    if material_extra:
        valor_material = 20
    else:
        valor_material = 0
    valor_parcial = valor_base + valor_ofcina + valor_material
    return valor_ofcina, valor_material, valor_parcial

def aplicar_desconto(valor_parcial, cupom=0, taxa_admin=5):
    desconto = valor_parcial * cupom/100
    valor_descontado = valor_parcial - desconto
    valor_taxa = valor_descontado * (taxa_admin/100)
    valor_final = valor_descontado + valor_taxa
    return desconto, valor_taxa, valor_final 

def classificar_participacao(oficinas, material_extra, total_final):
    if oficinas >= 2 or material_extra:
        return 'Inscrição completa'
    elif oficinas > 0:
        return 'Inscrição intermediária'
    else:
        return 'Inscrição básica'
    
def gerar_relatorio_participante(nome, tipo_ingresso, valor_padrao, oficinas, material_extra, cupom=0):
    valor_base = calcular_valor_base(tipo_ingresso, valor_padrao)
    valor_ofcina, valor_material, valor_parcial = calcular_extras(valor_base, oficinas, material_extra)
    desconto, valor_taxa, valor_final = aplicar_desconto(valor_parcial, cupom)
    classificacao = classificar_participacao(oficinas, material_extra, valor_final)
    return valor_base, valor_ofcina, valor_material, desconto, valor_taxa, valor_final, classificacao
