#definiendo función que me dice si una fecha es valida. 
def ValidarFecha(d,m,a):
# El año existe 
  if a<1 or a>2022:   # No existe el año
      print("Tu año aun no existe oficialmente y no hay certeza de que existira.")
      return (False)    
  elif a>1 or a<2022:  #El año existe
    #El mes existe
    if m > 12 or m<1:  #No existe el mes
      print("Tu mes no existe oficialmente.")
      return(False)
    elif m < 12 or m>1:  #El mes existe
      if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12: #Para meses de 31 días
        if d<1 or d>31:  #No existe el día
          print ("El día",d,"No existe para el mes que seleccionaste")
          return (False)
        elif d>1 and d<=31: #El día existe
          return (True)
      elif m==4 or m==6 or m==9 or m==11:#Para meses de 30 días
        if d<1 or d>30:  #No existe el día
          print ("El día",d,"No existe para el mes que seleccionaste")
          return (False)
        elif d>1 and d<=30: #El día existe
          return (True)
      else:           # Para Febrero
        if d<1 or d>29:     # No existe el día
          print ("El día",d,"No existe para el mes de Febrero")
          return (False)
        elif d<=28:     # El día existe
          return (True)
        elif d>28:      # El día existe solo si es bisiesto
          bisiesto = int(input("¿Es tu año bisiesto? 1. Sí , 2. No"))
          if bisiesto == 1:
            if d== 29:
              return (True)
          elif bisiesto == 2:
              print ("El día",d,"No existe para el mes de Febrero en año NO bisiesto")
              return (False)
          else:       # No se como llegar aquí
            print("Saliste fuera del límite de las opciones. ¡ADIOS!")
            Break

 # Solicitar por entrada la fecha pidiendo día, mes y año
año = int(input("Ingresa tu año:"))
mes = int(input("Ingresa tu mes(númericamente):"))
dia = int(input("Ingresa tu día:"))

#Llamando a la función
resultado = ValidarFecha(dia,mes,año)

#El resultado fue Verdadero. La fecha existe
if resultado == True: 
   print ("Tu fecha existe. yehi!")
#El resultado fue Falso. La fecha no existe.
elif resultado == False: 
   print("Por lo tanto, concluyo que: NO EXISTE TU FECHA.")
#Solo por precaución por si se sale de los limites. 
else:
  print ("Intenta nuevamente con otra fecha.")


student = {
    "name": "Ángela Teposte",
    "edad": 27 ,
    "Temas": "Nose",
    "Menores de edad": False,
}
