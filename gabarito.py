import json
import time


#dicionário gabarito em branco
gabarito_dict = {}


print ("\nQual a disciplina desta avaliação?")
#Registra qual disciplina da avaliação
key = "Disciplina"
item=input("\nDisciplina: ").split()
gab_disciplina = {}
gab_disciplina.update({key:item})

timestr = time.strftime("%Y.%m.%d-%H.%M.%S")
disciplina_tag = gab_disciplina.get('item')
filename1 = timestr
filename2 = " - gabarito.txt"

res = None
if key in set(gab_disciplina).intersection(gab_disciplina):
	res = gab_disciplina[key]

#print(str(res))

filename_full = filename1+" - "+str(res)+filename2
print(filename_full.replace("'",''))

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

print("\n--- Gabarito pronto ---")
#print(disciplina)

#for disciplina in gab_disciplina.keys():
print(gab_disciplina)
for pergunta, resposta in gabarito_dict.items():
	print(pergunta + ":" + resposta)
	gab_disciplina.update(gabarito_dict)
	with open(filename_full, 'w') as json_file: json.dump(gab_disciplina, json_file, ensure_ascii=False)
	
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