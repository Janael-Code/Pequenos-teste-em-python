from funçoes import add, ler, nome_quantidade


while True:
  valor = input("Escolha uma das opções abaixo para para adiconar ou ler os nomes dos alunos:\n 1°) Adicionar nomes\n 2°) Ler nomes\n 3°) Sair do programa\n")
  
  if valor == "1":
    nome_quantidade()

  elif valor == "2":
    print(f"\n{ler()}")

  elif valor == "3":
    print("Fim do programa")
    break

