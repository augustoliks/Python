class CalculadoraClass():

    def __init__(self, a, b):
        self.a = a
        self.b = b
#   __init__ inicializa valores aos atributos dentro da classe, funcionamento parecido com um constructor em java
#   "self", indica a variavel de referencia de forma genérica
#   se eu instanciar "var = CalculadoraClass(10,5)", significa que "var" será "self"
#   "a", "b" são argumentos, no exemplo, "a" receberá "10", "b" receberá "5"
    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

class MediaClass():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def media(self):
        return (self.a+self.b+self.c)/3
