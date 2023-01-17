def add(lista_dos_alunos):
  with open("lista_alunos.txt","w") as add:
    for linha in lista_dos_alunos:
      add.writelines(f"{linha}\n")

def ler():
  with open("lista_alunos.txt", "r") as leitura:
    lista = leitura.read()
    return lista

def nome_quantidade():
  nomesAlunos = []
  qnt_de_alunos = int(input("Quantos alunos você quer adicionar? "))
  for i in range(qnt_de_alunos):
    nome = input(f"Digite o nome do {i+1}° aluno: ").title()
    nomesAlunos.append(nome)
    add(nomesAlunos)