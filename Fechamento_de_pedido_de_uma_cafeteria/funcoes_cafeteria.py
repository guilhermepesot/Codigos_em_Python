def calcular_preco_cafe(preco_base, acrescimo=0):
    return preco_base + acrescimo

def calcular_acompanhamento(preco, desconto=0):
    if desconto != 0:
        return preco * (1-desconto/100)
    return preco

def resumo_item(nome, valor):
    return nome, f'R$ {valor:.2f}'

def calcular_totais(valor1, valor2, taxa_servico=10):
    subtotal = valor1 + valor2
    valor_taxa = subtotal*(taxa_servico/100)
    final = subtotal + valor_taxa
    return subtotal , valor_taxa , final

