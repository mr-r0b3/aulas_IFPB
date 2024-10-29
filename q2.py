nmraulas = int(input('Digite a quantidade de aulas: '))

freq = int(input("Digite a quantidade de faltas: "))

qntf = ((nmraulas - freq) / nmraulas) *100

print(f"A frequência do aluno é de {qntf}%")