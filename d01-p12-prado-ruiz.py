#practica12
#prado nuñez luis armando
#ruiz rodriguez jorge missael
print("Practica 12");
print("Luis Aramando Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n");

def e1(_m,_n,_q):#Apariciones de palabras
    try:
        import time;
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        final={}
        w=0
        c=1
        c2=1
        ven(100,15)
        print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte cadena -> "));
        cad=str(input());
        cade=str.lower(cad);
        caden=str.split(cade);
        for i in (caden):
            if(i not in final):
                    final[i]=[c]
            elif(i in final):
                c2+=1
                final[i]=[c2]
        #for para mostrar los resultados
        hh = 0;
        for j in (final):
            if (hh % 2 == 0):
                print(str.lower(j) + " " + str(final[j]),end=",");
            else:
                print(str.upper(j) + " " + str(final[j]),end=",");
            hh = hh + 1;   
        input();    
        time.sleep(5)
        print("\033[2J\033[1;1F")
        return menu(w,_m,_n,_q)
    
    except:
        w+=1
        print("Valor no valido")
        print("\033[2J\033[1;1F")
        return menu(w,_m,_n,_q)
            
        
def e2(_q,_w):#Agenda
    try:
        import time;
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        m=0
        n=0
        ne=[1]
        ag={}
        ven(100,15)
        for i in (ne):
            ne+=[2]
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para salir inserte *"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte el nombre"));
            nom=str(input());
            print(Cursor.POS(2,5)+Back.WHITE+(" ")*98,Cursor.POS(1,5)+Back.MAGENTA+(" "));
            if(nom in ag):
                print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"El numero actual es {ag[nom]}"))
                print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Si desea modificar el numero inserte S "));
                no=str(input());
                if(no=="S"):
                    print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte el numero de telefono         "));
                    num=int(input());
                    print(Cursor.POS(2,7)+Back.WHITE+(" ")*98,Cursor.POS(1,7)+Back.MAGENTA+(" "));
                    print(Cursor.POS(2,6)+Back.WHITE+(" ")*98,Cursor.POS(1,6)+Back.MAGENTA+(" "));
                    print(Cursor.POS(2,5)+Back.WHITE+(" ")*98,Cursor.POS(1,5)+Back.MAGENTA+(" "));
                    if(num>=0):
                        ag[nom]=num
                    elif(num<0):
                        n+=1
                        print("\033[2J\033[1;1F")
                        return menu(m,n,_q,_w)
            elif(nom=="*"):
                print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Agenda: {ag}"))
                time.sleep(25)
                print("\033[2J\033[1;1F")
                return menu(m,n,_q,_w)
                
            else:
                print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte el numero de telefono"));
                num=int(input());
                print(Cursor.POS(2,7)+Back.WHITE+(" ")*98,Cursor.POS(1,7)+Back.MAGENTA+(" "));
                print(Cursor.POS(2,6)+Back.WHITE+(" ")*98,Cursor.POS(1,6)+Back.MAGENTA+(" "));
                if(num>=0):
                        ag[nom]=[num]
                elif(num<0):
                    n+=1
                    print("\033[2J\033[1;1F")
                    return menu(m,n,_q,_w)
    except:
        m+=1
        print("Valor no valido")
        print("\033[2J\033[1;1F")
        return menu(m,n,_q,_w)

    input()                
 
def e3(_m,_n,_w):#Cadena mas corta para cada caracter
    try:
        import time;
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        ven(100,12)
        q=0
        dic={}
        print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Igrese su cadena: "));
        a=input()
        print(Cursor.POS(2,4)+Back.WHITE+(" ")*98,Cursor.POS(1,4)+Back.MAGENTA+(" "));
        a=a.split(" ")
        cad=sorted(a, key=len,reverse= True)
        for x in range(len(cad)):
            for i in (cad[x]):
                dic[i]=cad[x]
        print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Las cadenas mas chicas son {dic}"))
        time.sleep(25)
        print("\033[2J\033[1;1F")
        return menu(q,_n,_m,_w)
        
    except:
        q+=1
        print("Valor no valido")
        print("\033[2J\033[1;1F")
        return menu(q,_n,_m,_w)
    input()    
            
        

def menu(_n,_m,_q,_w):#menu de for
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        conM=1
        n=_n
        m=_m
        b=n+m
        w=_w
        q=_q
        for m in range (conM):
            print(Back.MAGENTA+("                                         --[]X\n "),Fore.CYAN+Back.WHITE+Style.BRIGHT+("Esto es el menu                           "),Back.MAGENTA+(" \n "),Back.WHITE+("                                          "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"1-Cuantas veces esta la palabra:{w}         "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"2-Contactos error:{b}                       "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"3-Para cada letra la mas corta errores:{q}  "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+("4-Salir                                   "),Back.MAGENTA+(" \n "),Back.WHITE+("                                          "),Back.MAGENTA+(" \n                                              ")); 
            print("");
            nEjercicio=int(input("Introduce el numero de ejercio ->"));
            if(nEjercicio==1):
                print("\033[2J\033[1;1F")
                return e1(n,m,q)
            elif(nEjercicio==2):
                print("\033[2J\033[1;1F")
                return e2(q,w)
            elif(nEjercicio==3):
                print("\033[2J\033[1;1F")
                return e3(n,m,w)
            elif(nEjercicio==4):
                return("Gracias por su preferencia ");
            elif(nEjercicio>5 or nEjercicio<1):
                print("valor no valido");
                print("\033[2J\033[1;1F")
                return menu(n,m,q,w)
            input()
    except:
        print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"));
        print("\033[2J\033[1;1F")
        return menu(n,m,q,w)
    

def ven(x,y):#ventana con for
    from colorama import init,Back,Fore;
    init(autoreset=True)
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x-3)+("--[]X"));
    for i in range(y):
        print(Back.MAGENTA+(" ")+Back.WHITE+(" ")*x+Back.MAGENTA+(" "));
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x+2));

menu(0,0,0,0)
