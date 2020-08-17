def sum(n1,n2):
	print(f'{n1} + {n2} = {round(n1+n2,2)}')
def subtraction(n1,n2):
	print(f'{n1} - {n2} = {round(n1-n2,2)}')
def multiplication(n1,n2):
	print(f'{n1} * {n2} = {round(n1*n2,2)}')
def division(n1,n2):
	print(f'{n1} / {n2} = {round(n1/n2,2)}')

counter = 's'

while counter == 's' :
	operation = input('Qual operação deseja fazer?\n'
	'#Soma digite + \n'
	'#Subtração digite -\n'
	'#Multiplicação digite * \n'
	'#Divisão digite / \n')

	number1 = float(input('digite um numero\n'))
	number2 = float(input('digite um numero\n'))

	if operation == '+':
		print('#### SOMA ####\n')
		sum(number1,number2)
		counter = input('\ndeseja realizar mais algum calculo? s para sim n para nao\n').lower()

	elif operation == '-':
		print('#### SUBTRAÇÃO ####\n')
		subtraction(number1,number2)
		counter = input('\ndeseja realizar mais algum calculo? s para sim n para nao\n').lower()

	elif operation == '*':
		print('#### MULTIPLICAÇÃO ####\n')
		multiplication(number1,number2)
		counter = input('\ndeseja realizar mais algum calculo? s para sim n para nao\n').lower()

	elif operation == '/':
		print('#### DIVISÃO ####\n')
		division(number1,number2)
		counter = input('\ndeseja realizar mais algum calculo? s para sim n para nao\n').lower()
	else:
		print('\ndesculpe, essa opção não existe, por favor digite alguma de nossas opções\n')
		counter = 's'
