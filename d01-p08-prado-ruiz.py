#practica 08
#prado núñez luis armando
#ruiz rodriguez jorge missael


print("Practica 08");
print("Luis Armnado Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-");


def e01():#Area de una esfera
    radio=float(input("Introdusca el radio de la esfera "));
    if(radio>0):
        aEsfera=4*3.1416*(radio**2)
        print("El area de una esfera de radio %i es: "%radio,aEsfera);
    while(radio<=0):
        print("Error:El radio debe ser mayor que cero");
        radio=float(input("Introdusca el radio de la esfera "));
    print("");
    return menu()

def e02():#Volumen de una Arista
    cont_vol=1
    ari=float(input("Anota la arista del cubo "));
    while (ari > 0):
        vol=ari*3
        cont_vol=cont_vol+1
        print ("El volumen del cubo de arista",ari,"es:",vol);
        ari=int(input("Anota la arista del cubo "));
        print("Volumen calculados",cont_vol);
    print ("La arista tiene que ser positiva");
    print("");
    return menu()
        
def e03():#Tablas de multiplicar
    nTabla=int(input("Introdusca el numero de tabla que necesita "));
    tTabla=int(input("Introdusca el tope de la tabla "));
    contador03=1
    while(tTabla>0):
     rTabla=nTabla*contador03
     print(nTabla,"*",contador03,"=",rTabla);
     tTabla=tTabla-1
     contador03=contador03+1
     print("");
     return menu()

def e04():#Numeros negativos a positivos
    Num_u=float(input("Dijite su primer numero negativo "));
    while (Num_u >=0):
        print("Valor no valido");
        Num_u=int(input("El numero tiene que ser negativo"));
    Num_p1=Num_u*-1
    
    Num_d=float(input("Dijite su segundo numero negativo "));
    while (Num_d >=0):
        print("Valor no valido");
        Num_d=int(input("El numero tiene que ser negativo"));
    Num_p2=Num_d*-1

    Num_t=float(input("Dijite su tercer numero negativo "));
    while (Num_t >=0):
        print("Valor no valido");
        Num_t=int(input("El numero tiene que ser negativo"));
    Num_p3=Num_t*-1

    Num_c=float(input("Dijite su cuarto numero negativo"));
    while (Num_c >=0):
        print("Valor no valido");
        Num_c=int(input("El numero tiene que ser negativo"));
    Num_p4=Num_c*-1

    Num_ci=float(input("Dijite su quinto numero negattivo "));
    while (Num_ci >=0):
        print("Valor no valido");
        Num_ci=int(input("El numero tiene que ser negativo"));
    Num_p5=Num_ci*-1

    print("Sus numeros en positivo son ",Num_p1,"",Num_p2,"",Num_p3,"",Num_p4,"",Num_p5);
    print("");
    return menu()

def e05(): #Calificaciones de 5 alumnos
    cali1=float(input("introdusca calificacion de primer alumno "));
    while(cali1<0 or cali1>100):
        print("ERROR:introdusca la calificacion correctamente");
        cali1=float(input("introdusca calificacion de primer alumno "));
    cali2=float(input("introdusca calificacion de segundo alumno "));
    while(cali2<0 or cali2>100):
        print("ERROR:introdusca la calificacion correctamente");
        cali2=float(input("introdusca calificacion de segundo alumno "));
    cali3=float(input("introdusca calificacion de tercer alumno "));
    while(cali3<0 or cali3>100):
        print("ERROR:introdusca la calificacion correctamente");
        cali3=float(input("introdusca calificacion de tercer alumno "));
    cali4=float(input("introdusca calificacion de cuarto alumno "));
    while(cali4<0 or cali4>100):
        print("ERROR:introdusca la calificacion correctamente");
        cali4=float(input("introdusca calificacion de cuarto alumno "));
    cali5=float(input("introdusca calificacion de quinto alumno "));
    while(cali5<0 or cali5>100):
        print("ERROR:introdusca la calificacion correctamente");
        cali5=float(input("introdusca calificacion de quinto alumno "));
    calit=(cali1+cali2+cali3+cali4+cali5)/5
    print("");
    print("La media feu ",calit);
    if(cali1<cali2 and cali1<cali3 and cali1<cali4 and cali1<cali5):
        print("El primer alumno tiene la menor calificacion que es %i"%cali1);
    elif(cali2<cali1 and cali2<cali3 and cali2<cali4 and cali2<cali5):
        print("El segundo alumno tiene la menor calificacion que es %i"%cali2);
    elif(cali3<cali1 and cali3<cali2 and cali3<cali4 and cali3<cali5):
        print("El tercer alumno tiene la menor calificacion que es %i"%cali3);
    elif(cali4<cali1 and cali4<cali2 and cali4<cali3 and cali1<cali5):
        print("El cuarto alumno tiene la menor calificacion que es %i"%cali4);
    elif(cali5<cali1 and cali5<cali2 and cali1<cali3 and cali1<cali4):
        print("El quinto alumno tiene la menor calificacion que es %i"%cali5);
    print("");
    return menu()

def e06(): #Calcular equiqueta de placa
    contrillo=0
    contosa=0
    contoja=0
    conterde=0
    contul=0
    ini=1
    while(ini+1):
        placa=str(input("inserte su nùmero de placa -> "));
        ini+1
        if(placa[-1]=="1" or placa[-1]=="2"):
            print("Tu calcaminoia sera amarilla");
            contrillo=contrillo+1
        elif(placa[-1]=="3" or placa[-1]=="4"):
            print("Tu calcaminoia sera rosa");
            contosa=contosa+1
        elif(placa[-1]=="5" or placa[-1]=="6"):
            print("Tu calcaminoia sera roja");
            contoja=contoja+1
        elif(placa[-1]=="7" or placa[-1]=="8"):
            print("Tu calcaminoia sera verde");
            conterde=conterde+1
        elif(placa[-1]=="9" or placa[-1]=="0"):
            print("Tu calcaminoia sera azul");
            contul=contul+1
        elif (placa[-1]=="a"):
            return menu()
        print("Entraron %f amarillos"%contrillo);
        print("Entraron %f rosa"%contosa);
        print("Entraron %f roja"%contoja);
        print("Entraron %f verde"%conterde);
        print("Entraron %f azul"%contul);
        print("");
        print("si ya no desea continuar ponga a");                  
                    

def menu():
  print("Esto es el menu, si desea acceder al ejercicio 1 inserte 1, al ejercicio 2 inserte 2, al ejercicio 3 inserte 3, al ejercicio 4 inserte 4, al ejercicio 5 inserte 5, al ejercicio 6 inserte 6 y si ya no nesesita nuestros servio inserte 7")
  print("");
  nEjercicio=int(input("Introduce el nuemero de ejercio ->"));
  while(nEjercicio>7 or nEjercicio<0):
    print("ERROR: Valor no valido inserte nuevamente ");
    nEjercicio=int(input("Introduce el nuemero de ejercio ->"));
  if(nEjercicio==1):
      return e01()
  elif(nEjercicio==2):
      return e02()
  elif(nEjercicio==3):
      return e03()
  elif(nEjercicio==4):
      return e04()
  elif(nEjercicio==5):
      return e05()
  elif(nEjercicio==6):
      return e06()
  elif(nEjercicio==7):
      print("Gracias por su preferencia ");                   

    
   
