#   5. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Indique um numero Inteiro: "))
n2 = int(input("Indique um numero Inteiro: "))
n3 = int(input("Indique um numero Inteiro: "))


if n1 > n2 and n1 > n3:
    print ("Maior valor inserido: %d \n" %n1)
elif n2 > n3 and n2 > n1:
    print ("Maior valor inserido: %d \n" %n2)
elif n3 > n2 and n3 > n1:
    print ("Maior valor inserido: %d \n" %n3)
elif n3 == n2 and n3 == n1:
    print ("Maior valor inserido: %d \n" %n3)
