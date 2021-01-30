import flask
import os
import json
import jsonify
from flask import render_template



app = flask.Flask(__name__,template_folder='./templates/')
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')
	#"<h1>Distant Reading Archive</h1><p>BADADA This site is a prototype API for distant reading of science fiction novels.</p><p><a href=/gabaritos>AQUI</a></p>"
	#flask.render_template(index.html)
    #
    #return ""

@app.route('/gabarito/', methods=['GET'])
def api_all():
    return render_template('gabarito.html') 
    #jsonify(gabaritos)

@app.route('/cadastro_aluno/', methods=['GET'])
def cad_aluno():
    return render_template('cadastro_aluno.html') 

@app.route('/resultado_aluno/', methods=['GET'])
def result_aluno():
    return render_template('resultado_aluno.html') 

@app.route('/aprovados/', methods=['GET'])
def approved():
    return render_template('aprovados.html') 

@app.route('/gab_host/', methods=['GET'])
def hoster():
	return "<h1>teste</h1><p><a href=http://localhost:2112>Home</a></p>"


app.run(host='localhost', port=2112)