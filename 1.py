import random
import string
import re
import os




def TirarDados(): 
   a=0;b=6;d=0
   print("\n-----------------------------------------------------------------")
   for j in range (2):
       c=random.randint(0,6)
       print("\nEste es el numero que arrojo el dados  : ",c)
       d+=c
   print("\nEste es el acumulado de los numeros arrojado por los dado : " , d)
   print("\n-----------------------------------------------------------------\n")

def Jugar():
    Num=""
    while Num!="-1":
      TirarDados()   
      print("\n¿Desea tirar los dados?,ingrese cualquier numero para seguir jugando")
      Num=input("De lo contrario puede ingresar el numero -1 ola mundo como estas: ")
      
      
Jugar()



