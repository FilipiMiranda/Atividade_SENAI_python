nota1 = float(input("digite sua nota: "))
nota2 = float(input("digite sua nota: "))
nota3 = float(input("digite sua nota: "))

resultado = (nota1 + nota2 + nota3 / 3)

if resultado >= 7:
    print("Aprovado")
else:
    print("Reprovado")