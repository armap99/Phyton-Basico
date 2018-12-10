#practica10
#prado nuñez luis armando
#ruiz rodriguez jorge missael
print("Practica 10");
print("Luis Aramando Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n");
def e1(_h,_j,_q,_w):#Estacionamiento para ricos  
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        c=1
        n=0
        ñ=0
        spup=0
        pdce=10000 #La caja siempre tiene dinero para dar cambio
        while(c>0):
            print(Fore.YELLOW+Style.DIM+("Para dejar de ejecutar inserte la hora de entrada negativa"));
            hEn=int(input("Hora de entrada en formato militar? "));
            if (hEn<0):
                salir=int(input("Si desea regresar al menu inserte 1 y si quiere salir cualquier numero "));
                if(salir==1):
                    return menu(n,ñ,_h,_j,_q,_w)
                else:
                    return "Adios"
            while(hEn>2500 or hEn<100):
                print(Fore.RED+Style.DIM+("Inserte las horas en formato militar"));
                ñ+=1
                hEn=int(input("Hora de entrada en formato militar? "));
                if (hEn<0):
                    salir=int(input("Si desea regresar al menu inserte 1 y si quiere salir cualquier numero "));
                    if(salir==1):
                        return menu(n,ñ,_h,_j,_q,_w)
                    else:
                        return "Adios"
            
            hSa=int(input("Hora de salida en formato militar? "));
            while(hSa>2500 or hSa<100):
                print(Fore.RED+Style.DIM+("Inserte las horas en formato militar"));
                ñ+=1
                hSa=int(input("Hora de salida en formato militar? "));
            hCo=hSa-hEn
            if (hCo==0):
                shup=14800
                print(Back.BLUE+("                      --[]X\n "),Back.WHITE+Fore.CYAN+Style.DIM+("Total a pagar : $14800 "),Back.BLUE+(" \n "),Back.WHITE+("                       "),Back.BLUE+(" \n                           "));
                dado=float(input("Dinero recibido "));
                while (dado<shup):
                    print(Fore.RED+Style.DIM+("Le falta dinero "));
                    ñ+=1
                    dado=float(input("Dinero recibido "));
                if (dado>shup):
                    pdce=10000+dado
                    cambioe=dado-shup
                    pdce=pdce-cambioe
                    print (Back.YELLOW+("                 --[]X\n "),Back.RED+("                  "),Back.YELLOW+(" \n "),Back.RED+Fore.WHITE+Style.DIM+(f"Su cambio :${cambioe} "),Back.YELLOW+(" \n "),Back.RED+("                  "),Back.YELLOW+(" \n                      \n"));
            elif(hCo<0):
                hCo=hCo*-1
                shup=(((((2400-hCo))-100)/100)*600)+1000
                print(Back.BLUE+("                          --[]X\n "),Back.WHITE+Fore.CYAN+Style.DIM+("Total a pagar $%i       "%shup),Back.BLUE+(" \n "),Back.WHITE+("                           "),Back.BLUE+(" \n                               "));
                dado=float(input("Dinero recibido "));
                while (dado<shup):
                    print(Fore.RED+Style.DIM+("Le falta dinero "));
                    ñ+=1
                    dado=float(input("Dinero recibido "));
                if (dado>shup):
                    pdce=10000+dado
                    cambioe=dado-shup
                    pdce=pdce-cambioe
                    print (Back.YELLOW+("                 --[]X\n "),Back.RED+("                  "),Back.YELLOW+(" \n "),Back.RED+Fore.WHITE+Style.DIM+(f"Su cambio :${cambioe} "),Back.YELLOW+(" \n "),Back.RED+("                  "),Back.YELLOW+(" \n                      \n"));
            elif(hCo<=199):
                shup=1000
                print(Back.BLUE+("                     --[]X\n "),Back.WHITE+Fore.CYAN+Style.DIM+("Total a pagar : $1000 "),Back.BLUE+(" \n "),Back.WHITE+("                      "),Back.BLUE+(" \n                          "));
                dado=float(input("Dinero recibido "));
                while (dado<shup):
                    print(Fore.RED+Style.DIM+("Le falta dinero "));
                    ñ+=1
                    dado=float(input("Dinero recibido "));
                if (dado>shup):
                    pdce=10000+dado
                    cambioe=dado-shup
                    pdce=pdce-cambioe
                    print (Back.YELLOW+("                 --[]X\n "),Back.RED+("                  "),Back.YELLOW+(" \n "),Back.RED+Fore.WHITE+Style.DIM+(f"Su cambio :${cambioe}"),Back.YELLOW+(" \n "),Back.RED+("                  "),Back.YELLOW+(" \n                      \n"));
            elif(hCo>100):
                shu=hCo-100
                shup=((shu/100)*600)+1000
                print(Back.BLUE+("                        --[]X\n "),Back.WHITE+Fore.CYAN+Style.DIM+("Total a pagar $%i      "%shup),Back.BLUE+(" \n "),Back.WHITE+("                         "),Back.BLUE+(" \n                             "),(" \n"));
                dado=float(input("Dinero recibido "));
                while (dado<shup):
                    print(Fore.RED+Style.DIM+("Le falta dinero "));
                    ñ+=1
                    dado=float(input("Dinero recibido "));
                if (dado>shup):
                    pdce=10000+dado
                    cambioe=dado-shup
                    pdce=pdce-cambioe
                    print (Back.YELLOW+("                 --[]X\n "),Back.RED+("                  "),Back.YELLOW+(" \n "),Back.RED+Fore.WHITE+Style.DIM+(f"Su cambio :${cambioe}"),Back.YELLOW+(" \n "),Back.RED+("                  "),Back.YELLOW+(" \n                      \n"));
                
    except:
        print (Back.YELLOW+("           \n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"));
        n+=1
        return menu(n,ñ,_h,_j,_q,_w)
    input()

def e2(_n,_ñ,_q,_w):#caja registradora
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        h=0
        j=0
        cp=[1]
        producto=[]
        precio=[]
        subtotal=0
        for t in (cp):
            print(Fore.BLUE+Style.DIM+("Para dejar de ejecutar inserte un codigo negativo\n"))
            cp+=[2]
            cod=int(input("Inserte codigo del producto "));
            if(cod>0):
                producto.append(cod)
            else:
                iva=subtotal*0.15
                total=subtotal+iva
                print(Back.RED+Fore.BLACK+Style.DIM+("                                                                                      --[]X\n "),"Los productos fueron: ",producto,"                                               ",Back.RED+(" \n "),"Los precios fueron ",precio,"                                                          ",Back.RED+(" \n "),Style.BRIGHT+(f"Subtotal= {subtotal}                                                                     "),Back.RED+(" \n "),Style.BRIGHT+(f"El iva es= {iva}                                                                "),Back.RED+(" \n "),Style.BRIGHT+(f"Total=${total}                                                                        "),Back.RED+(" \n                                                                                           \n"));
                salir=int(input("Si quieres regresar al menu inserte 1 y si quiere salir inserte cualquier numero"));
                if(salir==1):
                    return menu(_n,_ñ,h,j,_q,_w)
                else:
                    return "Adios"
            preP=float(input("Inserte precio del producto "));
            if(preP>0):
                precio.append(preP)
                subtotal+=preP
            if(preP<0):
                print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"))
                h+=1
                return menu(_n,_ñ,h,j,_q,_w)
                
                
    except:
        print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"))
        j+=1
        return menu(_n,_ñ,h,j,_q,_w)
    input()

def e3(_n,_ñ,_h,_j,_w):#calculo de años y meses
    conD=1
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        q=0
        while(conD>0):
            print(Style.BRIGHT+Fore.RED+("Para dejar de ejecutar inserte dias negativos\n"));
            dias=int(input("Inserte cantidad de dias "));
            if(dias<=0):
                salir=int(input("Si quieres regresar al menu inserte 1 y si quiere salir inserte cualquier numero"));
                if(salir==1):
                    return menu(_n,_ñ,_h,_j,q,_w)
                else:
                    return "Adios"
            if(dias<30):
                se=dias//7
                print(Back.GREEN+("                                --[]X\n "),Back.YELLOW+Fore.WHITE+(f"Solo hay {dias} dias y {se} semanas     "),Back.GREEN+(" \n "),Back.YELLOW+("                                 "),Back.GREEN+(" \n                                     "));
            elif(dias>=30 and dias<365):
                me=dias//30
                se=dias//7
                print(Back.GREEN+("                                   --[]X\n "),Back.YELLOW+Fore.WHITE+(f"Hay {dias} dias y {me} meses y {se} semanas "),Back.GREEN+(" \n "),Back.YELLOW+("                                    "),Back.GREEN+(" \n                                        "));
            elif(dias>=365):
                me=dias//30
                se=dias//7
                añ=dias//365
                print(Back.GREEN+("                                           --[]X\n "),Back.YELLOW+Fore.WHITE+(f"Hay {dias} dias y {se}semanas y {me} meses y {añ} años"),Back.GREEN+(" \n "),Back.YELLOW+("                                            "),Back.GREEN+(" \n                                                "),("\n"));
    except:
        print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"));
        q+=1
        return menu(_n,_ñ,_h,_j,q,_w)
    input()

def e4(_n,_ñ,_h,_j,_q):#No numeros repetidos
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        w=0
        c=1
        cc=0
        lNum=[]
        lNums=[]
        while(c>0):
            print(Fore.BLUE+("Para dejar de ejecutar inserte un numero negativo"));
            c+=1
            num=int(input("Inserte un numero "));
            if (num not in lNum and num>0):
                lNum.append(num)
                lNums.append(num)
            elif (num>0):
                lNums.append(-1)
                lNum.append(num)
                cc+=1
            if(num<=0):
                    print(Back.GREEN+Fore.CYAN+Style.BRIGHT+("                                                    --[]X\n "),Fore.MAGENTA+Back.BLACK+Style.BRIGHT+(f"Los numeros dados fueron {lNum}   "),Back.GREEN+(" \n "),Fore.MAGENTA+Back.BLACK+Style.BRIGHT+(f"Los nuevos números son {lNums}   "),Back.GREEN+(" \n "),Fore.MAGENTA+Back.BLACK+Style.BRIGHT+(f"Total de cambios {cc}                                   "),Back.GREEN+(" \n                                                         \n"),);
                    print;
                    salir=int(input("Si quieres regresar al menu inserte 1 y si quiere salir inserte cualquier numero"));
                    if(salir==1):
                        return menu(_n,_ñ,_h,_j,_q,w)
                    else:
                        return "Adios"
    except:
        print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"));
        w+=1
        return menu(_n,_ñ,_h,_j,_q,w)
    input()


def menu(_n,_ñ,_h,_j,_q,_w):#menu de for
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        conM=1
        n=_n
        ñ=_ñ
        h=_h
        j=_j
        b=n+ñ
        l=h+j
        q=_q
        w=_w
        for m in range (conM):
            
            print(Back.MAGENTA+("                                         --[]X\n "),Fore.CYAN+Back.WHITE+Style.BRIGHT+("Esto es el menu                           "),Back.MAGENTA+(" \n "),Back.WHITE+("                                          "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"1-Estacionamiento errores:{b}               "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"2-Caja registradora error:{l}               "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"3-Convertidora de dias errores:{q}          "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"4-Remplazo de numeros repetidos errores:{w} "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+("5-salir                                   "),Back.MAGENTA+(" \n "),Back.WHITE+("                                          "),Back.MAGENTA+(" \n                                              ")); 
            print("");
            nEjercicio=int(input("Introduce el numero de ejercio ->"));
            if(nEjercicio==1):
                return e1(h,j,q,w)
            elif(nEjercicio==2):
                return e2(n,ñ,q,w)
            elif(nEjercicio==3):
                return e3(n,ñ,h,j,w)
            elif(nEjercicio==4):
                return e4(n,ñ,h,j,q)
            elif(nEjercicio==5):
                return("Gracias por su preferencia ");
            elif(nEjercicio>5 or nEjercicio<1):
                print("valor no valido");
                return menu(n,ñ,h,j,q,w)
            input()
    except:
        print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"));
        return menu(n,ñ,h,j,q,w)

menu(0,0,0,0,0,0)
