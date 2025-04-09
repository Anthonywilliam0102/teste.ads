def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

try:
    num1 = float(input("Digite o primeiro número (dividendo): "))
    num2 = float(input("Digite o segundo número (divisor): "))
    resultado = dividir(num1, num2)
    print(f"O resultado da divisão de {num1} / {num2} é: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
