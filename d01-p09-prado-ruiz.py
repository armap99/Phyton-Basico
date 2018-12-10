#practica09
#prado nuñez luis armando
#ruiz rodriguez jorge missael

print("Practica 09");
print("Luis Aramando Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-");

def e1():#entrada al teatro
        conE=[1]
        costEntra=50
        conPer=0
        try:
                print("Bienvenido al teatro inserte la edad del comprador para dejar de insertar valores inserte un valor menor 0 o uno mayor a 123 el costo del voleto es 50");
                for e in (conE):
                        conE+=[2]
                        edadEn=int(input("Inserte edad del comprador "));
                        if(0<edadEn<5):
                                print("No tiene edad para entrar al teatro");
                        elif(5<=edadEn<=14):
                                perP=costEntra*0.35
                                conPer+=perP
                                print("Deja de persibir -> ",perP);
                        elif(15<=edadEn<=19):
                                perS=costEntra*0.25
                                conPer+=perS
                                print("Deja de persibir -> ",perS);
                        elif(20<=edadEn<=45):
                                perT=costEntra*0.10
                                conPer+=perT
                                print("Deja de persibir -> ",perT);
                        elif(46<=edadEn<=65):
                                perC=costEntra*0.25
                                conPer+=perC
                                print("Deja de persibir -> ",perC);
                        elif(66<=edadEn<=122):
                                perQ=costEntra*0.35
                                conPer+=perQ
                                print("Deja de persibir -> ",perQ);
                        elif(edadEn<1 or edadEn>=123):
                                print("Cerrando caja... El teatro dejo de percibir el dia de hoy ",conPer);
                                rMenu=int(input("Si quiere regresar al menu inserte 1 , si quiere continuar 2 y si no inserte cualquier numero "));
                                if(rMenu==1):
                                        return menu()
                                elif(rMenu<=0 or rMenu>=3):
                                        return("Adios");
                                elif(rMenu==2):
                                        pass
        except:
                print("Valor no valido");
                return e1()
                        
def e2():#masa de aire
        try:
                con=[1]
                contMsA=0
                contMsM=0
                contA=0
                contM=0
                for i in (con):
                        con+=[2]
                        vei=int(input("Que clase de vehiculo se le calculara la masa \nAutomovil=1 \nMotocicleta=2 \nMenu y promedio de la masas=3\nDejar de ejecutar=4\n"));
                        if (vei<1 and vei>3):
                                print ("valor no valido");
                                vei=float(input("Que clase de vehiculo se le calculara la masa \nautomovil=1 \nmotocicleta=2 \nmenu=3\n"));
                        if (vei==1):
                                contA+=1
                                pres=float(input("Cual es la presion "));
                                if (pres<=0):
                                        print ("valor no valido");
                                        pres=float(input("Cual es la presion "));
                                vol=float(input("cual es el volumen "));
                                if (pres<=0):
                                        print ("Valor no valido");
                                        vol=float(input("cual es el volumen "));
                                tem=float(input("cuale es la temperatura "));
                                if (tem<=0):
                                        print ("Valor no valido");
                                        tem=float(input("cuale es la temperatura "));
                                masacA=(pres*vol)/(0.37*(tem+460))*(4)
                                contMsA=contMsA+masacA
                                print("La masa de las 4 llantas es de",masacA);
                                print("");
                        if (vei==2):
                                contM+=1
                                pres=float(input("Cual es la presion "));
                                if (pres<=0):
                                        print ("valor no valido");
                                        pres=float(input("Cual es la presion "));
                                vol=float(input("cual es el volumen "));
                                if (pres<=0):
                                        print ("Valor no valido");
                                        vol=float(input("cual es el volumen "));
                                tem=float(input("cuale es la temperatura "));
                                if (tem<=0):
                                        print ("Valor no valido");
                                        tem=float(input("cuale es la temperatura "));
                                masacM=(pres*vol)/(0.37*(tem+460))*(2)
                                contMsM=contMsM+masacM
                                print("La masa de las 2 llantas es de",masacM);
                                print("");
                        porM=(contMsA+contMsM)/(contA+contM)
                        if (vei==3):
                                print ("El promedio de la masa total es de",porM);
                                return menu()
                        if (vei==4):
                                return("Adios")
        except:
                print("Valor no valido");
                return e2()
              

def e3():#precio de huevo por calidad
        try:
                conH=[1]
                for h in (conH):
                        conH+=[2]
                        pGalli=float(input("Intrudusca peso de la gallina " ));
                        if (pGalli>6 or pGalli<0):
                                print("valor no valido tine que ser mayor de 0 y menor de 6")
                                return e3()
                        aGalli=float(input("Introdusca altura de la gallina "));
                        if (aGalli<0 or  aGalli>45):
                                print("POR FAVOR inserte valores validos tine que ser mayor a 0 y menor a 45");
                                return e3()
                        hGalli=int(input("Cuantos huevos pone "));
                        if (hGalli<0 or hGalli>8):
                                print ("valor no valido tiene que ser mayor a 0 y menor a 7");
                                return e3()
                        cali=pGalli*aGalli/hGalli
                        if (cali>=15):
                                costoK=cali*1.2
                                print("El kilo de huevo de esta gallina se vendera en ",costoK);
                                menup=int(input("Quiere regrear al menu inserte 1, salir 2 y continuar cualquier otro numero "));
                                if (menup==1):
                                        return menu()
                                elif (menup==2):
                                        return ("Adios");
                                elif (1>menup>2):
                                        pass
                        elif (8<cali<15):
                                costoK=cali*1.00
                                print("El kilo de huevo de esta gallina se vendera en ",costoK);
                                menup=int(input("Quiere regrear al menu inserte 1, salir 2 y continuar cualquier otro numero "));
                                if (menup==1):
                                        return menu()
                                elif (menup==2):
                                        return ("Adios");
                                elif (1>menup>2):
                                        pass
                        elif (cali<=8):
                                costoK=cali*0.80
                                print("El kilo de huevo de esta gallina se vendera en ",costoK);
                                menup=int(input("Quiere regrear al menu inserte 1, continuar cualquier numero y 2 "));
                                if (menup==1):
                                        return menu()
                                elif (menup==2):
                                        return ("Adios");
                                elif (1>menup>2):
                                        pass
                        
        except:
                print("Valor no valido ");
                return e3()
def e4():#Diputados
        try:
                contF=0
                contE=0
                contA=0
                conD=[1]
                for d in (conD):
                        conD+=[2]
                        vot=int(input("De la siguiente opciones elija \n1=Estas a favor del tratado \n2=Estas en contra del tratado \n3=Te abstienes de votar \n4=Terminar y dar resultados\n"));
                        if (vot==1):
                                contF=contF+1
                        if (vot==2):
                                contE=contE+1
                        if (vot==3):
                                contA=contA+1
                        if (vot==4):
                                vott=contF+contE+contA
                                porF=(contF*100)/vott
                                porE=(contE*100)/vott
                                porA=(contA*100)/vott
                                print ("");
                                print ("El total de votos a facor es de",contF,"y el porcentaje es de",porF,"%");
                                print ("El total de votos encontra es de",contE,"y el porcentaje es de",porE,"%");
                                print ("El tatal de abtinencia es de",contA,"y el porcentaje es de",porA,"%");
                                print ("");
                                back=int(input("Si desea hacer otra encuenta = 1 \nSi desea regresar al menu = 2 \nSi desea dejar de ejecutar = cualquier otro numero \n"));
                                if (back==1):
                                        return e4()
                                if (back==2):
                                        return menu()
                                if 1 > back or back > 2:
                                        return ("Adios");
        except:
                print("Valor no valido");
                return e4()
        

def e5():#suma de 100
    c=0
    for x in range(100, 0, -2):
        c+=x
        print(x,end="+");
    print("0=",c);
    print(c);
    menus=int(input("Si quiere regresar al menu inerte 1 si no es asi inserte cualquier numero"));
    if (menus==1):
            return menu()
    else:
            print("Adios");
        
def e6():#Calificaciones alumnos
        conA=[1]
        p=0
        v=0
        c2=0
        try:
            print ("Para dejar de insertar valores ponga el codigo de alumno negativo ");    
            for a in  (conA):
                    conA+=[2]
                    codigo=int(input("Inserte su codigo "));
                    if (codigo<0):
                        print("El alumno que tuvo mayor promedio fue")
                        print(v);
                        print ("Y empato con el alumno ")
                        print(c2);
                        print("Con un promedio de ",p)
                        print("Cerrando... ");
                        rMenu=int(input("Si quiere regresar al menu inserte 1, si quiere volver a ejecutar 2 y si no inserte cualquier numero "));
                        if(rMenu==1):
                            return menu()
                        elif(rMenu<=0 or rMenu>=3):
                            return("Adios");
                        elif(rMenu==2):
                                return e6()
                    cali1=float(input("inserte primera calificacion "));
                    if(cali1<0 or cali1>100):
                            print("valor no valido");
                            print(" ");
                            return e6()
                    cali2=float(input("inserte segunda calificacion "));
                    if(cali2<0 or cali2>100):
                            print("valor no valido");
                            print(" ");
                            return e6()
                    cali3=float(input("inserte tercera calificacion "));
                    if(cali3<0 or cali3>100):
                            print("valor no valido");
                            print(" ");
                            return e6()
                    
                    prom=(cali1+cali2+cali3)/3           
                    if (p<prom):
                         v=codigo
                         p=prom
                    elif (p==prom):
                        c2=codigo
                        if (c2==v):
                            print("El codigo no puede ser igual");
                            print(" ");
                            return e6()
        except:
            print ("Valor no valido");
            return e6()
        
def e7():#Tienda
        try:
                acoTo=500
                conT=[1]
                for i in (conT):
                        conT+=[2]
                        ven=int(input("1 = Hacer venta \n2 = Cerrar caja y regresar al menu\n3 = Dejar de ejecutar \n"));
                        print ("");
                        if (ven==1):
                                venM=float(input("Costo de producto "));
                                if (venM<=0 or ven>=4):
                                        print ("Error");
                                        return e7()
                                iva=venM*0.16
                                print ("IVA ",iva);
                                to=iva+venM
                                print ("Total a pagar ",to);
                                acoTo=acoTo+to
                                pag=float(input("Dinero recibido? "));
                                if (pag<to):
                                        print ("No se fia");
                                        return e7()
                                cam=pag-to
                                acoTo=acoTo-cam
                                if (cam>acoTo):
                                        print ("No ahy dinero para el cambio");
                                        return e7()
                                elif (cam<acoTo):
                                    print ("Gracias por su compra \nSu cambio es de ",cam);
                                    pass
                        if (ven==2):
                                print ("Caja cerrada su ganancia es de ",acoTo);
                                print ("");
                                return menu()
                        elif (ven==3):
                                return ("Adios")
        except:
                print ("Valor no valido");
                return e7()
                        
def menu():#menu de for
        try:
                conM=1
                for m in range (conM):
                        print("Esto es el menu, si desea acceder al ejercicio1(entrada de teatro) inserte 1, al ejercicio2(Llantera) inserte 2, al ejercicio3(Calidad de huevo) inserte 3, al ejercicio4(Camara de diputados) inserte 4, al ejercicio5(suma de 100) inserte 5, al ejercicio6(calificacion de alumnos) inserte 6, al ejercicio7(tienda) inserte 7 y si ya no nesesita nuestros servicio inserte 8")
                        print("");
                        nEjercicio=int(input("Introduce el nuemero de ejercio ->"));
                        if(nEjercicio==1):
                                return e1()
                        elif(nEjercicio==2):
                                return e2()
                        elif(nEjercicio==3):
                                return e3()
                        elif(nEjercicio==4):
                                return e4()
                        elif(nEjercicio==5):
                                return e5()
                        elif(nEjercicio==6):
                                return e6()
                        elif(nEjercicio==7):
                                return e7()
                        elif(nEjercicio==8):
                                return("Gracias por su preferencia ");
                        elif(nEjercicio>8 or nEjercicio<1):
                                print("valor no valido");
                                return menu()
        except:
                print ("Valor no valido");
                return menu()
