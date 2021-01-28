import json
import time
from pathlib import Path
import os.path

print("###################")
print("#Cadastro de notas#")
print("###################")

def sgr():
#print("1. Visualizar lista de alunos")
	print("2. Cadastro de notas dos alunos")
	print("3. Resultado por aluno")
	print("4. Lista de aprovados")
	print( )

	sgr_opt = ""
	while not sgr_opt:
		print("Escolha uma das opções acima: ")
		sgr_opt = input() 
	#int(input("Escolha uma das opções acima: "))
	sgr_opt=int(sgr_opt)

	sr_opt_1 = sgr_opt == 1
	sr_opt_2 = sgr_opt ==  2
	sr_opt_3 = sgr_opt ==  3
	sr_opt_4 = sgr_opt ==  4
	wrn_opt_1 =  sgr_opt == 0
	wrn_opt_2 =  sgr_opt > 4


	if (wrn_opt_1):
		print()
		print("#### ATENÇÃO !!! ###")
		print("Item fora da lista, favor escolha uma das opções abaixo: ")
		print()
		sgr()
	elif (wrn_opt_2):
		print()
		print("#### ATENÇÃO !!! ###")
		print("Item fora da lista, favor escolha uma das opções abaixo: ")
		print()
		sgr()
		
	elif (sr_opt_1):
		print("opção 01")
		nome_aluno = input("Qual o nome do aluno? ")
	elif (sr_opt_2):
			print("katiau")
	elif (sr_opt_3):
			print("Three")
	elif (sr_opt_4):
			print("yon")
sgr()



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