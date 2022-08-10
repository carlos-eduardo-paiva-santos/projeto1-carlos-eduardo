# Crie um script que leia dois numeros e tente mostrar a soma entre eles

#tipos de primitivos

# int = numeros inteiros tipo 1 2 2 4 ... ( inteiros )
# float = numeros com ponto tipo 1.5 2.4 ... ( Flutuantes )
# bool = numeros true false ( Boleanos )
# str = Palavras em aspas 'Ola' '2.7' '' ( string )

#variaveis 

from tkinter.filedialog import askopenfilename


one = int (input ('Qual primeiro numero?'))
two = int (input ('Qual segundo numero?'))
asoma = (one)
com = (two)

#variavel pronta

soma = one+two

#escrever mensagem

#para escrever mensagem em print com variavel e so colocar a mensagem em aspas simples e variaveis fora com virgula

#print 

print ('A soma de {} + {} é = {}.'.format(asoma, com, soma))

