# Função para inverter letras de cada palavra em uma frase
def inverter_palavras(frase):
    palavras = frase.split()  # Divide a frase em palavras
    palavras_invertidas = [palavra[::-1]
                           for palavra in palavras]  # Inverte cada palavra
    # Junta as palavras invertidas em uma nova frase
    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase


# Exemplo de uso
frase = input("Digite uma frase: ")
frase_invertida = inverter_palavras(frase)
print(f"Frase com palavras invertidas: {frase_invertida}")
