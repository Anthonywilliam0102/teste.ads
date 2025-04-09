def somar(a, b):
    return a + b

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = somar(num1, num2)
    print(f"O resultado da soma de {num1} + {num2} é: {resultado}")
except ValueError:
    print("Por favor, insira números válidos.")
