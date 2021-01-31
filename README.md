# gakusei

Descrição
-----------

Esta API tem como principal função atender as necessidades dentro de instituições de ensino relacionadas à avaliações.
Aqui é possível cadastrar gabaritos, registrar as respostas de cada aluno, realizar cálculos das notas obtidas nas avaliações e informar se os alunos foram aprovados ou não em cada avaliação.

Essa API é totalmente desenvolvida em Python, tendo Flask como framework.

Requisitos
-------------

Python 3

Para realizar o setup do Backend/Frontend
----------

	- Entrar na pasta gakusei,
	- Executar o script startup_script.bat, em sistemas Windows.

	- O script irá realizar a instalação dos módulos necessários, bem como
	também iniciará o serviço.

Utilização do site
-------------
Acesse o endereço http://localhost:2112.

No menu principal, selecione a opção desejada e proceda com as operações de cada função.

API
---------
	api_gab_all:
	- GET
	--Lista todos gabaritos já postados.

	api_gab_id:
	- GET
	--Lista os gabaritos pelo ID.

	api_alunos
	- GET
	--Lista os gabaritos de todos os alunos que já foram enviados

	result_aluno_all
	- GET
	-- Lista o resultado de todos os alunos

	approved
	- GET
	-- Lista os alunos aprovados, a cada acesso ele gera uma lista atualizada, gerada pelo script resultados.py

	
 