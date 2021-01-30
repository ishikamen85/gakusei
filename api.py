import flask
import os
import json
import jsonify
import requests
from flask import Flask, render_template, jsonify



app = flask.Flask(__name__,template_folder='./templates/')
app.config["DEBUG"] = True

###Chave dos gabaritos
gabaritos = [
	{'id':0,
	'disciplina': 'Matemática',
	'data':'25.01.2021',
	'respostas':[
	{    "1": "b",
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
	{    "1": "a",
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
	{    "1": "d",
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
	{    "1": "a",
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

@app.route('/gabaritos_available/', methods=['GET'])
def hoster():
	return jsonify(gabaritos)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')



@app.route('/gabarito/', methods=['GET','POST'])
def api_all():
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



if __name__=="__main__":
	app.run(host='localhost', port=2112)