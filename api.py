import flask
import os
import json
import jsonify
import requests
from flask import Flask, render_template, jsonify
from pprint import pprint
from flask import request


app = flask.Flask(__name__,template_folder='./templates/')
app.config["DEBUG"] = True

###Chave dos gabaritos
gabaritos = [
	{'id':0,
	'disciplina': 'Matemática',
	'data':'25.01.2021',
	'respostas':[
	{	"1": "b",
	"2": "d",
	"3": "a",
	"4": "d",
	"5": "a",
	"6": "a",
	"7": "a",
	"8": "a",
	"9": "c",
	"10": "a"}]
	},
	{'id':1,
	'disciplina': 'Português',
	'data':'25.01.2021',
	'respostas':[
	{	"1": "a",
	"2": "e",
	"3": "e",
	"4": "d",
	"5": "b",
	"6": "a",
	"7": "d",
	"8": "a",
	"9": "e",
	"10": "a"}]

	},
	{'id':2,
	'disciplina': 'Geografia',
	'data':'26.01.2021',
	'respostas':[
	{	"1": "d",
	"2": "d",
	"3": "a",
	"4": "c",
	"5": "a",
	"6": "b",
	"7": "a",
	"8": "a",
	"9": "e",
	"10": "e"}]

	},
	{'id':3,
	'disciplina': 'História',
	'data':'26.01.2021',
	'respostas':[
	{	"1": "a",
	"2": "a",
	"3": "d",
	"4": "e",
	"5": "e",
	"6": "a",
	"7": "b",
	"8": "a",
	"9": "c",
	"10": "a"
}]

	},
]

#with open(os.path.join(os.path.dirname(__file__), "alunos", "alunos.json")) as file:
 #   alunojson = json.load(file)
#alunos = json.load(alunojson)
alunos = alunos = [
	{'id':0,
	'nome':'Lucas',
	'disciplina': 'Matemática',
	'data':'25.01.2021',
	'respostas':[
	{	"1": "b",
	"2": "d",
	"3": "a",
	"4": "d",
	"5": "a",
	"6": "a",
	"7": "a",
	"8": "a",
	"9": "c",
	"10": "a"
	}]
	},
	{'id':1,
	'nome':'Lucas',
	'disciplina': 'Português',
	'data':'25.01.2021',
	'respostas':[
	{	"1": "a",
	"2": "e",
	"3": "e",
	"4": "d",
	"5": "b",
	"6": "a",
	"7": "d",
	"8": "a",
	"9": "e",
	"10": "a"
	}]

	},
	{'id':2,
	'nome':'Lucas',
	'disciplina': 'Geografia',
	'data':'26.01.2021',
	'respostas':[
	{	"1": "d",
	"2": "d",
	"3": "a",
	"4": "c",
	"5": "a",
	"6": "b",
	"7": "a",
	"8": "a",
	"9": "e",
	"10": "e"
	}]

	},
	{'id':3,
	'nome':'Lucas',
	'disciplina': 'História',
	'data':'26.01.2021',
	'respostas':[
	{	"1": "a",
	"2": "a",
	"3": "d",
	"4": "e",
	"5": "e",
	"6": "a",
	"7": "b",
	"8": "a",
	"9": "c",
	"10": "a"
	}]
	},
	{'id':4,
	'nome':'Maria',
	'disciplina': 'Matemática',
	'data':'25.01.2021',
	'respostas':[
	{	"1": "b",
	"2": "d",
	"3": "a",
	"4": "d",
	"5": "a",
	"6": "a",
	"7": "a",
	"8": "a",
	"9": "c",
	"10": "a"
	}]
	},
	{'id':5,
	'nome':'Maria',
	'disciplina': 'Português',
	'data':'25.01.2021',
	'respostas':[
	{	"1": "a",
	"2": "e",
	"3": "e",
	"4": "d",
	"5": "b",
	"6": "a",
	"7": "d",
	"8": "a",
	"9": "e",
	"10": "a"
	}]

	},
	{'id':6,
	'nome':'Maria',
	'disciplina': 'Geografia',
	'data':'26.01.2021',
	'respostas':[
	{	"1": "d",
	"2": "d",
	"3": "a",
	"4": "c",
	"5": "a",
	"6": "b",
	"7": "a",
	"8": "a",
	"9": "e",
	"10": "e"
	}]

	},
	{'id':7,
	'nome':'Maria',
	'disciplina': 'História',
	'data':'26.01.2021',
	'respostas':[
	{	"1": "a",
	"2": "a",
	"3": "d",
	"4": "e",
	"5": "e",
	"6": "a",
	"7": "b",
	"8": "a",
	"9": "c",
	"10": "a"
}]
	},
]

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/gabarito/all', methods=['GET'])
def api_gab_all():
	return jsonify(gabaritos)

@app.route('/gabarito/gabarito', methods=['GET', 'POST'])
def api_gab_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return render_template('erro.html')
	results = []
	for gabarito in gabaritos:
		if gabarito['id'] == id:
			results.append(gabarito)
	return jsonify(results)

@app.route('/gabarito/', methods=['GET','POST'])
def api_gabarito():
	request.form.get('disciplina')
	return render_template('gabarito.html') 
	
@app.route('/cadastro_aluno/', methods=['GET','POST'])
def cad_aluno():
	return render_template('cadastro_aluno.html') 

@app.route('/resultado_aluno/', methods=['GET'])
def result_aluno():
	return render_template('resultado_aluno.html') 

@app.route('/aprovados/', methods=['GET'])
def approved():
	return render_template('aprovados.html') 


@app.route('/aluno_gab/aluno/all', methods=['GET'])
def api_alunos():
    return jsonify(alunos)

@app.route('/aluno_gab/aluno/', methods=['GET'])
def aluno_gab_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return render_template('erro.html')
	results = []
	for aluno in alunos:
		if aluno['id'] == id:
			results.append(aluno)
	return jsonify(results)

@app.route('/aluno_gab/nome/', methods=['GET'])
def api_nome():
	if 'nome' in request.args:
		nome = str(request.args['nome'])
	else:
		#return "<h1>ERRO</h1><p>ALUNO não encontrado.</p>Tente novamente</p>"
		return render_template('erro.html')
	results = []
	for nome in nomes:
		if nome['nome'] == nome:
			results.append(nome)
	return jsonify(results)
	

if __name__=="__main__":
	app.run(host='localhost', port=2112)