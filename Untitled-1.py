# explicação do codigo 
'''
Esse codigo ele nescessita que   todas as operações que serao realizada deva abaixo ter dois novos conjuntos para funcionar.
lerar um aquirvo txt.
E na primeira linha do aquivo txt ele determinará a quantidade de operações do codigo.
Assim ele cria uma variavel chama acao e tranforma ela em um numero inteiro, apartir disso ,faço ele rodar dentro de um for i in range eliminando o 0 dele.
Assim dependendo do valor do I ele vai criar 2 (dois) conjuntos,que dependendo do numero vai pegar de um determinado conjunto dentro do arquivo txt, e uma variavel de posição para saber qual operação sera realizada.
Assim eu crio uma nova variavel chamada "operacoes_realizada" que vai pegar a posição no txt e descobrir a operação que vai ser realizada.

Dentro das proprias funções ele vai ser impreso o resultado da operação.

'''

# definição das funçoes

def Uniao(set1, set2):
  Uniao = set1.union(set2)
  print("\no resultado vai ser\n")
  print(f"Uniao = primeiro conjunto = {set1} segundo conjunto ={set2}\n resultado da operação = {Uniao}")
  return Uniao

def Intersecao(set1, set2):
  intersecao = set1.intersection(set2)
  print("\no resultado vai ser\n")
  print(
      f" Interseção =o primeiro conjunto = {set1} segundo conjunto ={set2} resultado da operação = {intersecao}"
  )
  return intersecao

def diferenca(set1, set2):
  diferenca = set1 - set2
  print("\no resultado vai ser\n")
  print(
      f" Diferença  =o primeiro conjunto = {set1} segundo conjunto ={set2} resultado da operação = {diferenca}"
  )
  return diferenca
  
def cartesiano(set1, set2):
  cartesiano = set()
  for i in set1:
    for j in set2:
      par_ordenado = (i, j)
      cartesiano.add(par_ordenado)
  print("\nO resultado do produto cartesiano é\n")
  print(
      f"\n Cartesiano = Conjunto 1 = {set1} Conjunto 2 = {set2}\n\nResultado = "
  )
  for par in sorted(cartesiano):
    print(par)
  return cartesiano
# ler um aquivo txt
with open("teste.txt", "r", encoding="UTF-8") as arquivo:
  linhas = arquivo.readlines()
#trasformar acao em falor interiro
acao = int(linhas[0].strip())
#variavez usada 
posicao=0
set1 = set()
set2 = set()
for i in range(1, acao + 1):
  if acao <= 4:
    if i == 1:
      set1 = set(linhas[2].strip().split(","))
      set2 = set(linhas[3].strip().split(","))
      posicao = 1
    elif i == 2:
      set1 = set(linhas[5].strip().split(","))
      set2 = set(linhas[6].strip().split(","))
      posicao = 4
    elif i == 3:
      set1 = set(linhas[8].strip().split(","))
      set2 = set(linhas[9].strip().split(","))
      posicao = 7
    elif i == 4:
      set1 = set(linhas[11].strip().split(","))
      set2 = set(linhas[12].strip().split(","))
      posicao = 10

    operacoes_realizada = linhas[posicao].split()
    if "U" in operacoes_realizada:
      Uniao(set1, set2)
    elif "I" in operacoes_realizada:
      Intersecao(set1, set2)
    elif "D" in operacoes_realizada:
      diferenca(set1, set2)
    elif "C" in operacoes_realizada:
      cartesiano(set1, set2)

  else:
    print("por favor coloque um numero de (1 a 4)")
    break

print("\n fim do programa ")
