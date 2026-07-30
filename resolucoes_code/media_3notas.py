# Calculando a média de três notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")

# Exemplo

Digite a primeira nota: 8
Digite a segunda nota: 7
Digite a terceira nota: 9

Média: 8.00
Aluno aprovado!
