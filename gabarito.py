import json
import time
from pathlib import Path
import os.path


#dicionário gabarito em branco
gabarito_dict = {}


print ("\nQual a disciplina desta avaliação?")
#Registra qual disciplina da avaliação
key = "Disciplina"
item=input("\nDisciplina: ").split()
gab_disciplina = {}
gab_disciplina.update({key:item})

#Prepara o nome do arquivo com a data e hora e qual a disciplina que está sendo cadastrada
#timestr = time.strftime("%Y.%m.%d-%H.%M.%S")
timestr = time.strftime("%Y%m%d-%H.%M.%S")
disciplina_tag = gab_disciplina.get('item')
filename1 = timestr
filename2 = " - gabarito.json"
#Especificação da pasta onde ficarão os gabaritos cadastrados
directory = './gabaritos/'

res = None
if key in set(gab_disciplina).intersection(gab_disciplina):
	res = gab_disciplina[key]

filename_full = filename1+" - "+str(res)+filename2

#Abre o loop do registro de notas
gabarito_open = True

while gabarito_open:
	pergunta = input("\nQual o número da pergunta? ")
	resposta = input("Qual a resposta para esta pergunta? ")

	gabarito_dict[pergunta] = resposta

	repeat = input("\nDeseja registar mais uma questão? (s/n) ")

	if repeat == "n":
		gabarito_open = False

	if pergunta == None:
		lista()
	if pergunta is str:
		print("Favor inserir somente números")

print("\n--- Gabarito pronto ---")

#Testa se a pasta gabaritos existe, se não, ele a cria
if not os.path.isdir(directory):
    os.mkdir(directory)
#Exibe o gabarito
print(gab_disciplina)
for pergunta, resposta in gabarito_dict.items():
	print(pergunta + ":" + resposta)
	#mescla os dicionários para a chave
	gab_disciplina.update(gabarito_dict)
	with open(os.path.join(directory, filename_full), 'w') as json_file: json.dump(gab_disciplina, json_file, ensure_ascii=False, indent = 4)
	
print("Gabarito salvo como "+filename_full)
print()
finalization = input("Deseja voltar ao menu inicial? (S/N) ")

if finalization == "S":
	import main
elif finalization == "s":
	import main
elif finalization == "n":
	print("Cadastro finalizado.")
	exit
elif finalization == "N":
	print("Cadastro finalizado.")
	exit
#import main