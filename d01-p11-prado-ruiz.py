#practica11
#prado nuñez luis armando
#ruiz rodriguez jorge missael
print("Practica 11");
print("Luis Aramando Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n");

def e1(_h,_j,_q,_w):#Tenminacion en determinada letra
    try:
        import time;
        import os;
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        p=[1]
        nombresL=[]
        ncl=[]
        n=0
        m=0
        ven(100,15)
        for i in (p):
            p+=[2]
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para dejar de ejecutar inserte N y S para salir al menu"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte el nombre"));
            nom=str(input());
            print(Cursor.POS(2,5)+Back.WHITE+(" ")*20,Cursor.POS(1,5)+Back.MAGENTA+(" "));
            while(nom.isalpha()==False):
                n+=1
                print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Solo letras joven y sin espacios"));
                print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte el nombre"))
                nom=str(input());
                print(Cursor.POS(2,5)+Back.WHITE+(" ")*20,Cursor.POS(1,4)+Back.MAGENTA+(" "))
            if(nom=="S"):
                print("\033[2J\033[1;1F")
                return menu(n,m,_h,_j,_q,_w)
            if(nom!="N"and nom!="S"):
                nombresL.append(nom)
            elif(nom=="N"):
                print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Letra que quiere buscar al final "));
                finl=str(input());
                while(finl.isalpha()==False):
                    n+=1
                    print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Solo letras joven"));
                    print(Cursor.POS(2,10)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Letra que quiere buscar al final "));
                    finl=str(input());
                    print(Cursor.POS(1,11)+Back.MAGENTA+(" "))
                for i in (nombresL):
                    if(i[-1]==finl):
                        ncl.append(i)
                ncl2=set(ncl)    
                print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Los nombres que terminan con {finl} son {ncl2}"));
                time.sleep(6)
                t=5
                for i in range (8):
                    t+=1
                    print(Cursor.POS(2,t)+Back.WHITE+(" ")*98,Cursor.POS(1,4)+Back.MAGENTA+(" "))
                
    except:
        print("Valor no valido")
        return menu(n,m,_h,_j,_q,_w)
        print("\033[2J\033[1;1F")
        m+=1

    input()

def e2(_n,_m,_h,_j,_w):#La mas larga
    try:
        import time;
        import os;
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        q=0
        la=[1]
        con=0
        li=[]
        lo=[]
        ven(80,10)
        for i in (la):
            la+=[2]
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para dejar de ejecutar inserte N y S para salir al menu"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte el texto deseado"));
            s=str(input());
            print(Cursor.POS(2,5)+Back.WHITE+(" ")*78,Cursor.POS(1,5)+Back.MAGENTA+(" "));
            if(s!="N"and s!="S"):
                li.append(s)
            if(s=="S"):
                print("\033[2J\033[1;1F")
                return menu(_n,_m,_h,_j,q,_w)
            if(s=="N"):
                c=0
                for i in (li):
                    x=len(i)
                    if(x>c):
                        x=x-c
                        c+=x
                        lo.append(i)
                    if(x==c):
                        lo.append(i)
                if(len(lo[-2])==len(lo[-1])):
                    print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"El  texto mas largo fue: {lo[-2]}"));
                    time.sleep(6)
                    li=[]
                    print(Cursor.POS(2,6)+Back.WHITE+(" ")*58);
                else:
                    print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"El texto mas largo es: {lo[-1]}"));
                    time.sleep(6)
                    li=[]
                    print(Cursor.POS(2,6)+Back.WHITE+(" ")*58);
    except:
        q+=1
        print("Valor no valido");
        print("\033[2J\033[1;1F")
        
    input()           
                
def e3(_n,_m,_h,_j,_q):#Prefijo comun mas largo
    import time;
    import os;
    from colorama import Cursor,init,Fore,Back,Style;
    init(autoreset=True)
    pl=[1]
    cade=[]
    w=0
    
    for i in (pl):
        pl+=[2]
        print("Para dejar de ejecutar inserte N ");
        texto=str(input("Inserte un texto "));
        while(texto.isalpha()==False):
            print("No insrete numeros o signos");
            texto=str(input("Inserte un texto "));
        if(texto!="N"):
            cade.append(texto)
        if(texto=="N"):
            print("cade")
        if(texto=="S"):
            print("\033[2J\033[1;1F")
            return menu(_n,_m,_h,_j,_q,w)

        input()
        
                

def e4(_n,_m,_q,_w):#subcadenas k
    try:
        import time;
        import os;
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        cs=0
        h=0
        j=0
        po=[1]
        la=[1]
        ven(110,10)
        for i in (la):
            la+=[2]
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para salir al menu inserte S"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte la cadena"));
            cad=str(input());
            if(cad=="S"):
                print("\033[2J\033[1;1F")
                return menu(_n,_m,h,j,_q,_w)
            print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Tamaño de sub cadena"));
            s=int(input());
            print(Cursor.POS(2,8)+Back.WHITE+(" ")*108,Cursor.POS(1,8)+Back.MAGENTA+(" "));
            while(1>len(cad)//s):
                j+=1
                print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte un valor mas pequeño"));
                time.sleep(2)
                print(Cursor.POS(2,8)+Back.WHITE+(" ")*108,Cursor.POS(1,8)+Back.MAGENTA+(" "));
                print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Tamaño de sub cadena"));
                s=int(input());
                print(Cursor.POS(2,8)+Back.WHITE+(" ")*108,Cursor.POS(1,8)+Back.MAGENTA+(" "));
            while(s<=0):
                j+=1
                print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte un valor mas grande que 0"));
                time.sleep(2)
                print(Cursor.POS(2,8)+Back.WHITE+(" ")*108,Cursor.POS(1,8)+Back.MAGENTA+(" "));
                print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Tamaño de sub cadena"));
                s=int(input());
                print(Cursor.POS(2,9)+Back.WHITE+(" ")*108,Cursor.POS(1,9)+Back.MAGENTA+(" "));
            cad=(" ")*(s-1)+cad
            for i in (cad):
                cs+=1
                if (cs==s):
                    print(',',i,end='');
                    cs=0
                    cad="S"
                            
                else:
                    print(i,end='');
                    cad="S"               
    except:
        print("Valor no valido");
        h=+1
        print("\033[2J\033[1;1F")
        return menu(_n,_m,h,j,_q,_w)

    input()    
        
def menu(_n,_m,_h,_j,_q,_w):#menu de for
    try:
        import os;
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        conM=1
        n=_n
        m=_m
        h=_h
        j=_j
        b=n+m
        l=h+j
        w=_w
        q=_q
        for m in range (conM):
            print(Back.MAGENTA+("                                         --[]X\n "),Fore.CYAN+Back.WHITE+Style.BRIGHT+("Esto es el menu                           "),Back.MAGENTA+(" \n "),Back.WHITE+("                                          "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"1-Busqueda de ultima letra errores:{b}      "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"2-La mas larga error:{q}                    "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"3-Prefijo comun mas largo errores:{w}       "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+(f"4-Subcadenas K errores:{l}                  "),Back.MAGENTA+(" \n "),Fore.BLUE+Back.WHITE+Style.BRIGHT+("5-salir                                   "),Back.MAGENTA+(" \n "),Back.WHITE+("                                          "),Back.MAGENTA+(" \n                                              ")); 
            print("");
            nEjercicio=int(input("Introduce el numero de ejercio ->"));
            if(nEjercicio==1):
                print("\033[2J\033[1;1F")
                return e1(h,j,q,w)
            elif(nEjercicio==2):
                print("\033[2J\033[1;1F")
                return e2(n,m,h,w,j)
            elif(nEjercicio==3):
                print("\033[2J\033[1;1F")
                return e3(n,m,h,j,q)
            elif(nEjercicio==4):
                print("\033[2J\033[1;1F")
                return e4(n,m,w,q)
            elif(nEjercicio==5):
                return("Gracias por su preferencia ");
            elif(nEjercicio>5 or nEjercicio<1):
                print("valor no valido");
                print("\033[2J\033[1;1F")
                return menu(n,m,h,j,q,w)
            input()
    except:
        print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"));
        os.system("cls")
        return menu(n,m,h,j,q,w)


def ven(x,y):#ventana con for
    from colorama import init,Back,Fore;
    init(autoreset=True)
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x-3)+("--[]X"));
    for i in range(y):
        print(Back.MAGENTA+(" ")+Back.WHITE+(" ")*x+Back.MAGENTA+(" "));
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x+2));


    
menu(0,0,0,0,0,0)        
