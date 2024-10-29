Al_ap = int(input('Digite a quantidade de alunos aprovados: '))

Al_rp = int(input('Digite a quantidade de alunos reprovados: '))

total_de_alunos = Al_ap + Al_rp

Pct_al_ap = Al_ap /total_de_alunos *100

print(f"A porcentagem de alunos aprovados foi de {Pct_al_ap:.2f}%")