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

@app.route('/gabaritos/', methods=['GET'])
def api_all():
    return "<h1>Gabaritos</h1>" 
    #jsonify(gabaritos)



app.run()