from classParente import *
from classPerguntas import *

se = Parente()
pergunta = Pergunta()

while se.probabilidade() != 100:
	string = pergunta.texto()
	se.pergunta(string[0],string[1])
	if se.probabilidade() == 100:
		print('Parente pensado foi: ',se.resultado[0])
	
