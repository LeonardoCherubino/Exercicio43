## 4-3 Escreva um programa que leia três números e que imprima o maior e o menor

Num1 = int(input('Entre com o primeiro número. '))
Num2 = int(input('Entre com o segundo número. '))
Num3 = int(input('Enrte com o terceiro número. '))


if Num1 > Num2 and Num1 > Num3:
   Maior = Num1
if Num1 < Num2 and Num1 < Num3:
    Menor = Num1
if Num2 > Num1 and Num2 > Num3:
    Maior = Num2
if Num2 < Num1 and Num2 < Num3:
    Menor = Num2
if Num3 > Num1 and Num3 > Num2:
    Maior = Num3
if Num3 < Num1 and Num3 < Num2:
    Menor = Num3
# elif Num1 == Num2 or Num1 == Num3 or Num2 == Num3: 
    # print('Digite valores diferentes entre si. ')
print('O maior número é {}.'.format(Maior))
print('O menor número é {}'.format(Menor))