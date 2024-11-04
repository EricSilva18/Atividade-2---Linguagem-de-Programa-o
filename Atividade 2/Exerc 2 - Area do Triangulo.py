import math

# Função para verificar se os valores formam um triângulo


def forma_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

# Função para calcular a área de um triângulo usando a fórmula de Herão


def calcula_area(a, b, c):
    s = (a + b + c) / 2  # semiperímetro
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


if forma_triangulo(a, b, c):
    area = calcula_area(a, b, c)
    print(f"Os valores formam um triângulo e a área é: {area:.2f}")
else:
    print(f"Os valores {a}, {b} e {c} não formam um triângulo.")
