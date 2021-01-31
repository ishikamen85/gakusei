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

	# {'id':8,
	# 'nome':'Luiza',
	# 'disciplina': 'História',
	# 'data':'26.01.2021',
	# 'nota':9
	
	# },
]

#def approved_list():

timestr = time.strftime("%Y%m%d-%H.%M.%S")
filenam1 = "resultado.txt"
resultado_file = timestr+" - "+filenam1
directory = './alunos'

for s in range(len(notas)):
	if notas[s]["nota"] >= 7:
		with open(os.path.join(directory,resultado_file), 'a') as f:
			print("\n<li>{} foi aprovado com a nota {} em {}</li>".format(notas[s]["nome"],notas[s]["nota"],notas[s]["disciplina"]),file=f)
import glob
#import resultados
logdir = './alunos'
#last_result = sorted([ f for f in os.listdir(logdir) if f.endswith('resultado.txt')])
list_of_files = glob.glob('./alunos/*') 
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)	
	
