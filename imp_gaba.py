#imp_gaba
#Este módulo importa o gabarito do aluno para o módulo sgr, de modo a realizar posteriormente o cálculo.
import json
import time
from pathlib import Path
import os

def input_aluno():
	gabarito_alunos = './gabaritos_alunos/'

	aluno_nome = input("Favor informar o nome do aluno: ")
	id_avaliacao = input("Informe o ID da avaliação: ")
	id_caller_ava = aluno_nome+"_"+id_avaliacao+".json"

	file_gaba = os.path.join(gabarito_alunos, id_caller_ava)

	with open(file_gaba) as json_file:
		gab_up = json_file.read()
	print(gab_up)

try:
	input_aluno()
except:
	print()
	print("Arquivo não existe")
	input("Retornando ao menu anterior...")
	print()
	import sgr




