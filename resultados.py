import json
import time
from pathlib import Path
import os.path
import diff
import datetime



#boletim
#def compare_gab():
#boletim_reg = True

#while boletim_reg:
ref_gabarito_path = "./gabaritos/"
ref_gab_aluno = "./gabaritos_alunos/"

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

for entry in os.listdir(ref_gabarito_path):
	if os.path.isfile(os.path.join(ref_gabarito_path, entry)):
		print(entry)

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
