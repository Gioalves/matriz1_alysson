matriz = []

for i in range(10):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    matriz.append([nome, idade])

pessoa_mais_nova = matriz[0]

for pessoa in matriz:
    if pessoa[1] < pessoa_mais_nova[1]:
        pessoa_mais_nova = pessoa

print("A pessoa mais nova é:", pessoa_mais_nova[0])