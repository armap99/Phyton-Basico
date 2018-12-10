#practica13
#prado nuñez luis armando
#ruiz rodriguez jorge missael
print("Practica 13");
print("Luis Aramando Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n");
    
def e1(_po,_error2,_error3):#Poema al reves,numero de caracteres y numero de palabras
    try:
        import os.path
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        p=0
        c=0
        po=_po
        error1=0
        ven(55,20)
        if(".txt" not in po):
            po=po+".txt"
        if(os.path.isfile(po)==False):
            error1+=1
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("El archivo no existe"));
            input()
            print("\033[2J\033[1;1F")
            return menu(error1,_error2,_error3)
        poe=open(po,mode="r",encoding="utf-8")
        poem=poe.read();
        poemr=poem[::-1]
        pal=str.split(poem)
        for o in (poem):
            c+=1
        for i in (pal):
            p+=1
        print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"El total de palabras fue {p}"));
        print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"El total de caracteres fue {c}"));
        print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"El {po} al reves es -> \n{poemr}"));
        poe.close()

        input()
        print("\033[2J\033[1;1F")
        return menu(error1,_error2,_error3)
    
    except:
        error1+=1
        print("Valor no valido");
        print("\033[2J\033[1;1F")
        return menu(error1,_error2,_error3)

def e2(_error1,_error3):#Creacion de arcvivos con el mismo contenido
    try:
        import os.path
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        infi=[1]
        final=[]
        fistr=""
        cc=0
        error2=0
        ven(55,10)
        for i in (infi):
            infi+=[2]
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para salir inserte *"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte el monbre del documento "));
            lop=str(input());
            print("\033[2J\033[1;1F")
            ven(110,20)
            if(lop=="*"):
                ya=open(lup,mode="r",encoding="utf-8")
                yo=ya.read();
                print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"{yo}"))
                ya.close()
                input()
                print("\033[2J\033[1;1F")
                return menu(_error1,error2,_error3)
            if(".txt" not in lop):
                lop=lop+".txt"
            if(os.path.isfile(lop)==False):
                error2+=1
                print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("El archivo no existe"));
                input()
                print("\033[2J\033[1;1F")
                return menu(_error1,error2,_error3)
            lope=open(lop,mode="r",encoding="utf-8")
            lopep=lope.read();
            slop=str.split(lopep)
            hh=0
            for j in (slop):
                if (hh % 2 == 0):
                    final.append(str.lower(j));
                else:
                    final.append(str.upper(j));
                hh = hh + 1;
            cc+=1
            fistr=" ".join(final)
            lup=lop.rstrip(".txt")
            lup=lup+f"({cc})"
            lope.close()
            archin=open(lup,mode="w",encoding="utf-8");
            archin.write(fistr)
            final=[]
            fistr=""
            archin.close()
            
    except:
        error2+=1
        print("Valor no valido")
        print("\033[2J\033[1;1F")
        return menu(_error1,error2,_error3)

        
def e3(_error1,_error2):#Busqueda de palabras en un archivo de texto
    try:
        import os.path
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        pa={}
        error3=0
        ven(55,20)
        print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte nombre del archivo -> "));
        tex=str(input());
        if(".txt" not in tex):
            tex=tex+".txt"
        if(os.path.isfile(tex)==False):
            text=open(tex,mode="w",encoding="utf-8")
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte contenido de texto "));
            con=str(input())
            text.write(con)
            text=open(tex,mode="r",encoding="utf-8")
            lec=text.read();
        else:
            text=open(tex,mode="r",encoding="utf-8")
            lec=text.read();
            
        print("\033[2J\033[1;1F")
        ven(55,20)
        print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Palabras que desea buscar -> "));
        bus=str(input())
        bu=bus.replace(","," ")
        bu=bu.split()
        lec=lec.split()
        a=""
        b=""
        c=""
        for i in lec:
            if (i in bu):
                b=(Back.RED+i)
                c=c+" "+b
            else:
                a=Back.RESET+i
                c=c+" "+a
        for e in (bu):
            rl=0
            for i in (lec):
                if(i==e):
                    rl+=1
                    pa[i]=[rl]

        print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"{c}"))
        print(pa)
        text.close()
        
        input()
        print("\033[2J\033[1;1F")
        return menu(_error1,_error2,error3)
    
    except:
        error3+=1
        print("Valor no valido");
        print("\033[2J\033[1;1F")
        return menu(_error1,_error2,error3)
        
    
def menu(_error1,_error2,_error3):#menu de for
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        error1=_error1
        error2=_error2
        error3=_error3
        conM=1
        ven(55,16)
        for m in range (conM):
            print(Cursor.POS(25,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("MENU"))
            print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"1-Texto al reves,palabras y caracteres. Errores:{error1}"));
            print(Cursor.POS(2,10)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"2-Creacion del mismo archivo. Errores:{error2}"));
            print(Cursor.POS(2,11)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"3-Busqueda de palabras en un archivo. Errores:{error3}"));
            print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("4-Salir"));
            print(Cursor.POS(2,13)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Introduce el numero de ejercio ->"));
            nEjercicio=int(input());
            if(nEjercicio==1):
                print(Cursor.POS(2,14)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Inserte nombre del archivo -> "));
                po=str(input());
                print("\033[2J\033[1;1F")
                return e1(po,error2,error3)
            elif(nEjercicio==2):
                print("\033[2J\033[1;1F")
                return e2(error1,error3)
            elif(nEjercicio==3):
                print("\033[2J\033[1;1F")
                return e3(error1,error2)
            elif(nEjercicio==4):
                return("Gracias por su preferencia ");
            elif(nEjercicio>4 or nEjercicio<1):
                print("valor no valido");
                print("\033[2J\033[1;1F")
                return menu(0,0,0)
            input()
    except:
        print (Back.YELLOW+("      --[]X\n "),("       "),Back.YELLOW+(" \n "),Back.BLACK+Fore.WHITE+Style.DIM+(" ERROR "),Back.YELLOW+(" \n "),("       "),Back.YELLOW+(" \n           \n"));
        print("\033[2J\033[1;1F")
        return menu(0,0,0)

def ven(x,y):#ventana con for
    from colorama import init,Back,Fore;
    init(autoreset=True)
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x-3)+("--[]X"));
    for i in range(y):
        print(Back.MAGENTA+(" ")+Back.WHITE+(" ")*x+Back.MAGENTA+(" "));
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x+2));

menu(0,0,0)
