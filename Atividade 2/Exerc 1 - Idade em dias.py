
def converter_idade_em_dias(dias_totais):
    anos = dias_totais // 365
    dias_restantes = dias_totais % 365
    meses = dias_restantes // 30
    dias = dias_restantes % 30
    return anos, meses, dias


idade_em_dias = int(input("Digite sua idade em dias: "))


anos, meses, dias = converter_idade_em_dias(idade_em_dias)
print(f"Sua idade é {anos} anos, {meses} meses e {dias} dias.")
