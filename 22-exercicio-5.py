valor1 = int(input("Digite o primeiro valor: "))
op = input("Digite a operacao matematica: ")
valor2 = int(input("Digite o segundo valor: "))

if op == "+":
    resultado = valor1 + valor2
elif op == "-":
    resultado = valor1 - valor2
elif op == "*":
    resultado = valor1 * valor2
elif op == "/":
    resultado = valor1 / valor2
else:
    print("Sinal invalido")
print(resultado)