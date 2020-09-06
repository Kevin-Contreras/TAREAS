print ("colocar las palabras")
palabras = input()
def automata ():
  letras=[];
  numeroletras = 0
  contador =0;
  contador2 =0;
  for letra in palabras:
    letras.append(letra)
    numeroletras+=1
    if(letra == "_"):
      print("si pertenece a la sintaxis-----" + letra)
    else:
      if(letra.isalpha()==True):
        if(contador2==0):
          contador2=1
          print("pertenece a la sintaxis ---- "+ letra)
        else:
          print("no pertenece a la sintaxis----- " + letra)
      else:  
        if(letra.isnumeric()):
            if(contador==0):
              contador=1
              print("el numero pertenece a la sintaxis---- "+ letra)
            else:
               print("el numero  no pertenece a la sintaxis---- "+ letra)    
  print("*******************Sintaxis error********************")
def automata2():
  letras=[];
  numeroletras = 0
  contador =0;
  contador2 =0;
  y=0;
  for letra in palabras:
    if(letra.isalpha()):
      print ("la sintaxis es correcta---" + letra)
    else:
        if(y == 0):
          print("sintaxis no reconcocida---" + letra)
          y=1
        else:
          if(letra.isnumeric()):
            print("sintaxis reconocida")
  print("**********************Sintaxis error*********************")

print("-------------------camino 1----------------------------")           
automata() 
print("-------------------camino 2---------------------------")
automata2()