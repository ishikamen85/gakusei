import json
import time
from pathlib import Path
import os.path
import diff
import datetime
import resultados


#boletim
#def compare_gab():
boletim_reg = True

while boletim_reg:
	ref_gabarito_path = "./gabaritos/"
	ref_gab_aluno = "./gabaritos_alunos/"

	#print("Informe a data no seguinte formato dd/mm/aaaa\nEx: 20/07/2020")
	ano_ava =  input("Em qual ano foi realizada a avaliação?\nEx: 2020  ")
	mes_ava = input("Em qual mês foi realizada a avaliação?\nEx: 04 ")
	data_ava = input("Em qual a data foi feita a avaliação?\nEx: 01 ")

	Nulo = ''
	if ano_ava is Nulo: 
		print("Período inválido!\nFavor informar a data corretamente.")
		#boletim_reg = False
		ano_ava
	complete_data_ava = ano_ava+mes_ava+data_ava

	#print(complete_data_ava)

	#fixed_data = (datetime.datetime.strptime(data_ava, "%d/%m/%Y").strftime("%Y.%m.%d"))

	disciplina = input("Qual a disciplina? ")
	#break

	for file_gab_ref in os.listdir(ref_gabarito_path):
		if complete_data_ava in file_gab_ref:
			print(file_gab_ref)
			boletim_reg = False
		else:
			print("Gabarito não existe, favor informar novamente as informações solicitadas.")
			boletim_reg = False
#Busca arquivo com informações específicas
