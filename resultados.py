import json
import time
from pathlib import Path
import os.path
import diff
import datetime

notas = [
	{'id':0,
	'nome':'Lucas',
	'disciplina': 'Matemática',
	'data':'25.01.2021',
	'nota':5
	
	},
	{'id':1,
	'nome':'Lucas',
	'disciplina': 'Português',
	'data':'25.01.2021',
	'nota':6
	
	},
	{'id':2,
	'nome':'Lucas',
	'disciplina': 'Geografia',
	'data':'26.01.2021',
	'nota':7
	
	},
	{'id':3,
	'nome':'Lucas',
	'disciplina': 'História',
	'data':'26.01.2021',
	'nota':7
	
	},
	{'id':4,
	'nome':'Maria',
	'disciplina': 'Matemática',
	'data':'25.01.2021',
	'nota':8
	
	},
	{'id':5,
	'nome':'Maria',
	'disciplina': 'Português',
	'data':'25.01.2021',
	'nota':9
	
	},
	{'id':6,
	'nome':'Maria',
	'disciplina': 'Geografia',
	'data':'26.01.2021',
	'nota':10
	
	},
	{'id':7,
	'nome':'Maria',
	'disciplina': 'História',
	'data':'26.01.2021',
	'nota':9
	
	},
]

#def approved_list():

timestr = time.strftime("%Y%m%d-%H.%M.%S")
filenam1 = "resultado.txt"
resultado_file = timestr+" - "+filenam1
directory = './alunos'

for s in range(len(notas)):
	if notas[s]["nota"] >= 7:
		with open(os.path.join(directory,resultado_file), 'a') as f:
			print("{} foi aprovado com a nota {} em {}".format(notas[s]["nome"],notas[s]["nota"],notas[s]["disciplina"]),file=f)


#print(approved_list())
#if nota_final < 7:
	#for i in range(0, len(notas)):    
	#	print(notas[i]),  
#boletim
#def compare_gab():
#boletim_reg = True

#while boletim_reg:
#ref_gabarito_path = "./gabaritos/"
#ref_gab_aluno = "./gabaritos_alunos/"

#print("Informe a data no seguinte formato dd/mm/aaaa\nEx: 20/07/2020")
# Nulo = ""
# ano_ava =  input("Em qual ano foi realizada a avaliação?\nEx: 2020  ")
# if ano_ava is Nulo: 
# 	print("Período inválido!\nFavor informar a data corretamente.")
# 	break

# mes_ava = input("Em qual mês foi realizada a avaliação?\nEx: 04 ")
# if mes_ava is Nulo: 
# 	print("Período inválido!\nFavor informar a data corretamente.")
# 	break

# data_ava = input("Em qual a data foi feita a avaliação?\nEx: 01 ")
# if data_ava is Nulo: 
# 	print("Período inválido!\nFavor informar a data corretamente.")
# 	break

#for entry in os.listdir(ref_gabarito_path):
	#if os.path.isfile(os.path.join(ref_gabarito_path, entry)):
		#print(entry)

		#boletim_reg = False
		
	#if 
	#complete_data_ava = ano_ava+mes_ava+data_ava

	#print(complete_data_ava)

	#fixed_data = (datetime.datetime.strptime(data_ava, "%d/%m/%Y").strftime("%Y.%m.%d"))

	#disciplina = input("Qual a disciplina? ")
	#break

	# for file_gab_ref in os.listdir(ref_gabarito_path):
	# 	if complete_data_ava and disciplina in file_gab_ref:
	# 		print(file_gab_ref)
	# 		boletim_reg = False
	# 		break
	# 	else:
	# 		print("Gabarito não existe, favor informar novamente as informações solicitadas.")
	# 		boletim_reg = False
	# 		break
#Busca arquivo com informações específicas
