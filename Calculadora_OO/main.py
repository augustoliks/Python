from fonteCalculadora import CalculadoraClass
from fonteCalculadora import MediaClass
#   "fonteCalculadora" é codigo fonte onde está as classes
#   "MediaClass" é a classe dentro do codigo fonte
#   do arquivo "fonteCalculadora", pegar a classe "CalculadoraClass"

var = CalculadoraClass(10,10)
#   assumi os atributos e métodos da classe "CalculadoraClass"

var2 = MediaClass(10,8,4)
#   assumi os atributos e métodos da classe "MediaClass"

print("Soma: ", var.soma() )
#   imprimirá: ('Soma: ', 20)

print("Media: ", var2.media() )
#   imprimirá: ('Media: ', 7)
