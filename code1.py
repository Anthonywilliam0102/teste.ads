def subtrair(a, b):
    return a - b

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = subtrair(num1, num2)
    print(f"O resultado da subtração de {num1} - {num2} é: {resultado}")
except ValueError:
    print("Por favor, insira números válidos.")
