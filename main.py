import json
import requests




print("#############")
print("###gakusei###")
print("#############")
print( )


def listas():
	print("1. Cadastro de gabarito")
	print("2. Cadastro de notas")
	print("3. Resultado por aluno")
	print("4. Lista de aprovados")
	print( )

	choose_opt = ""
	while not choose_opt:
		print("Escolha uma das opções acima: ")
		choose_opt = input() 
	#int(input("Escolha uma das opções acima: "))
	choose_opt=int(choose_opt)

	main_opt_1 = choose_opt == 1
	main_opt_2 = choose_opt ==  2
	main_opt_3 = choose_opt ==  3
	main_opt_4 = choose_opt ==  4
	wrong_opt_1 =  choose_opt == 0
	wrong_opt_2 =  choose_opt >4




	if (wrong_opt_1):
		print()
		print("#### ATENÇÃO !!! ###")
		print("Item fora da lista, favor escolha uma das opções abaixo: ")
		print()
		listas()
	elif (wrong_opt_2):
		print()
		print("#### ATENÇÃO !!! ###")
		print("Item fora da lista, favor escolha uma das opções abaixo: ")
		print()
		listas()
			
	elif (main_opt_1):
		import gabarito
		
	elif (main_opt_2):
		import sgr
			
	elif (main_opt_3):
			print("Three")
	elif (main_opt_4):
			print("yon")

	if __name__ == "__listas_":
		listas()

	

listas()


