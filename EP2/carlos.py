global posição
posição = 0
def desenho(posição):
	boneco = ['''
	+-------------------+
			    |
			    |
			    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
			    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|		    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|\		    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|\		    |
       / 		    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|\		    |
       / \		    |
			    |
			    |
			    |
			    |
====================================''']
	print (boneco[posição])


def jogar_novamente():
	alternativa = input('Deseja jogar novamente? [S/n] ')
	while alternativa.lower() != "s" and  alternativa.lower() != "n": 
		alternativa = input('Digite um valor válido por favor [S/n]: ')
	if alternativa.lower() == 's':
		return jogo()
	elif alternativa.lower() == 'n':
		return print('fim de jogo!')

def escolhe():

	import urllib.request
	pagina = urllib.request.urlopen('https://www.ime.usp.br/~pf/dicios/br')
	texto = pagina.read().decode('iso8859')
	listona = texto.split('\n')

	from random import randint
	return listona[randint(0,int (len (listona)))]
	
def chute(letras):

	while len (letras)!= 1:
		letras = input ("\nDigite APENAS UMA letra: ")
	while letras not in 'abcdefghijklmnopqrstuvwxyzáàãâéèêẽíìôóòôúùç':
		letras = input ("\nDigite uma LETRA: ")
	return letras 


def jogo():

	pos=0

	palavra_aleatoria=escolhe()
	palavra_aleatoria=list(palavra_aleatoria)
	sublinhados = '_'*len(palavra_aleatoria)
	sublinhados=list(sublinhados)
	ja_digitou=[]

	while True:
		desenho(pos)
		

		print ("Sua palavra tem %d LETRAS " %(len(palavra_aleatoria)) )

		print (" ".join(sublinhados))

		if len (ja_digitou) > 0:
			print ("Você já digitou: ","-".join(ja_digitou) )
		
		letra = input ("Digite uma Letra: ")
		letra_validada=chute(letra)
		
		if letra_validada in ja_digitou:
			print ("Essa letra você já digitou")
		else:
			ja_digitou.append(letra_validada)

			k=0
			while k < len (palavra_aleatoria):
				if letra_validada == palavra_aleatoria[k]:
			
					sublinhados[k]=letra_validada
					print("ACERTOU a letra '%s' na posição %d" %(letra_validada,k+1) )	
				k+=1
			

			if letra_validada not in palavra_aleatoria:
				print("ERROU!!!")
				pos+=1
				desenho(pos)

			if sublinhados==palavra_aleatoria:
				print ("PARABÉNS!!!, Você acertou a palavra: ", "".join(palavra_aleatoria))
				break
			if pos==5:
				print ("Você PERDEU, a palavra era: ", "".join(palavra_aleatoria))
				break
jogo()
jogar_novamente()
