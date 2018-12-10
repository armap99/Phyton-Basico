#practica 14
#prado nuñez luis armando
#ruiz rodriguez jorge missael
print("Practica 14");
print("Luis Aramando Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n");

def vender(_si):#Caja de la muerte
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        inf=[1]
        si=_si
        tiq={}#Diccionario del recibo
        totalap=0#Subtotal a pagar
        rl=0
        achii=open("inventario.txt",mode="r",encoding="utf-8")
        cance=achii.read();#Productos que se tiene la primera vez que se ejecuta por si cancela la compra
        achii.close()
        for t in (inf):
            inf+=[2]
            achir=open("registro_de_empresa.txt",mode="r",encoding="utf-8")
            nome=achir.readline();#Nombre de la empresa importante
            achir.close()
            achie=open("registro_de_empleados.txt",mode="r",encoding="utf-8")
            empl=achie.read();#Saca la lista de empleados
            achie.close()
            emple=""
            c=0
            for i in (empl):
                if(i=="'"):
                    c+=1
                else:
                    emple=emple+i
                    empl=emple
                    empl=empl.split(",")
            dempl={}#diccionario de empleados
            for empl in (empl):
                dempl[empl.split(":")[0]]=empl.split(":")[1]
            achii=open("inventario.txt",mode="r",encoding="utf-8")
            inv=achii.read();#Productos que se tiene
            achii.close()
            inve=""
            for i in (inv):#for para quitar '
                        if(i!="'"):
                            inve=inve+i
                        if(i=="'" or i==" "):
                            inve=inve+""
            inv=inve
            inv=inve.split("-")
            dinv={}#diccionario de productos
            for inv in (inv):
                dinv[inv.split(":")[0]]=inv.split(":")[1]
            #Falta pasar el codigo de quien esta usando el programa lo tamaras antes de ejecutar el menu !!!!!!!importante!!!!!!!
            ven(100,15)
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Bienvenido a {nome}"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para dejar de insertar productos inserte *"));
            print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Los productos de le podemos ofreser son:"))
            print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Los productos estan ordenados por codigo del producto,nombre,cantidad y presio"));
            print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"{dinv}"));
            print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Codigo del preoducto a comprar"));
            cpro=str(input());#codigo a buscar
            print("\033[2J\033[1;1F")
            if(cpro=="*"):
                yo=dempl.get(si)
                ven(100,17)
                print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"{nome}"));
                print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Fue atendido por -> {yo}"));
                print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Compró:\n{tiq}"));
                print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Subtotal:{totalap}"));
                print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Total:${(totalap*0.15)+totalap}"));
                print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para cancelar la compra inserte un numero negativo"));
                print(Cursor.POS(2,10)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Dinero recibido -> "));
                pdr=float(input())
                v=(totalap*0.15)+totalap
                if(pdr>=v):
                    achid=open("dinero_en_caja.txt",mode="r",encoding="utf-8")
                    dinero=achid.read()#Dinero que hay en la caja
                    achid.close()
                    a=float(dinero)
                    cambio=pdr-v#Cambio a dar
                    yt=a-cambio
                    if(yt<0):
                        print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("No hay suficiente dinero para dar cambio"));
                        achii=open("inventario.txt",mode="w",encoding="utf-8")
                        achii.write(cance);#Escribir productos originales
                        achii.close()
                        input()
                        print("\033[2J\033[1;1F")
                        return menu()
                    if(yt>-1):
                        v=(totalap*0.15)+totalap
                        print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Su cambio es ${cambio}"));
                        l=v+a
                        o=str(l)
                        achid=open("dinero_en_caja.txt",mode="w",encoding="utf-8")
                        achid.write(o);
                        achid.close()
                if(pdr<0):
                    print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Cancelando..."))
                    achii=open("inventario.txt",mode="w",encoding="utf-8")
                    achii.write(cance);#Escribir productos originales
                    achii.close()
                    return menu()
                while(pdr<v and pdr>-1):
                    print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"{nome}"));
                    print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Fue atendido por ->"));
                    print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Compró:\n{tiq}"));
                    print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Subtotal:{totalap}"));
                    print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Total:${(totalap*0.15)+totalap}"));
                    print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Para cancelar la compra inserte un numero negativo"));
                    print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Le falta dinero nuevamente ingrese el dinero recibido"));
                    print(Cursor.POS(2,10)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Dinero recibido -> "))
                    pdr=float(input())
                    if(pdr<1):
                        print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Cancelando..."))
                        achii=open("inventario.txt",mode="w",encoding="utf-8")
                        achii.write(cance);#Escribir productos originales
                        achii.close()
                    if(pdr>=v):
                        cambio=pdr-v#Cambio a dar
                        yt=a-cambio
                    if(yt<0):
                        print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("No hay suficiente dinero para dar cambio"));
                        achii=open("inventario.txt",mode="w",encoding="utf-8")
                        achii.write(cance);#Escribir productos originales
                        achii.close()
                        input()
                        print("\033[2J\033[1;1F")
                        return menu()
                    if(yt>-1):
                        print(Cursor.POS(2,12)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Su cambio es ${cambio}"));
                        achid=open("Dinero_en_caja.txt",mode="w",encoding="utf-8")
                        achid.write(v);
                        achid.close()
                    
                input()
                print("\033[2J\033[1;1F")
                return menu()
            if(cpro in dinv):
                cpron=cpro#para actualizar el inventario
                rl+=1#por si compra varias veces el producto
                spre=dinv.get(cpro[-1])#sacar el presio del diccionario
                spre=spre.split(",")
                pre=spre[-1]#Precio importante
                pre=float(pre)
                totalap+=pre#suma del precio
                npt=spre[0]#nombre del producto
                cnt=spre[-2]#Total de producto
                cnt=int(cnt)
                cnt=cnt-1
                if(cpron in tiq):
                    tiq[cpron]=[rl+1]
                if(cpron not in tiq):
                    rl=0
                    tiq[cpron]=[1]
                if(cnt==0):
                    del dinv[cpron]
                    newi=str(dinv);
                    newi=newi.strip('{').strip('}').strip("\ufeff");
                    newi=newi.replace("',","-");
                    achii=open("inventario.txt",mode="w",encoding="utf-8")
                    achii.write(newi)
                    achii.close()
                elif(cnt!=0):
                    vb=""
                    del dinv[cpron]
                    npt=str(npt)
                    cnt=str(cnt)
                    pre=str(pre)
                    vb=npt+","+cnt+","+pre
                    dinv[cpron]=[vb]
                    newi=str(dinv);
                    newi=newi.strip('{').strip('}').strip("\ufeff");
                    newi=newi.replace("[","").replace("]","");
                    newi=newi.replace("',","-");
                    newi=newi.replace(" ","");
                    achii=open("inventario.txt",mode="w",encoding="utf-8")
                    achii.write(newi)
                    achii.close()
                    
            else:
                ven(100,15)
                print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("No hay producto con ese codico"));
                input()
                print("\033[2J\033[1;1F")
    except:
        input()
        print("\033[2J\033[1;1F")
        return vender()
    
def regie():#Regritro de monbre de empresa y de empleados
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        ce=0#Contador para asignar codigo de empleado
        ven(55,10)
        print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("1- Modificar monbre de empresa"));
        print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("2- Modificar registro de empleados"));
        print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("3- Salir"));
        op=int(input());
        print("\033[2J\033[1;1F")
        if(op==1):
            ven(62,10)
            achir=open("registro_de_empresa.txt",mode="r",encoding="utf-8")
            nome=achir.readline();#Nombre de la empresa
            achir.close()
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Selecciono modificar mombre de la empresa"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"El nombre actual de la emperas es -> {nome}"))
            print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Si desea modificar el nombre de la empresa ingrese S y si no N"));
            mod=str(input());#Para saber si quiere modificar el nombre o no
            if(mod=="S"):
                print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Nuevo nombre"));
                v=str(input());#Nuevo nombre de la empresa
                achir=open("registro_de_empresa.txt",mode="w",encoding="utf-8")
                achir.write(v)
                achir.close()
                print("\033[2J\033[1;1F")
                return regie()
            if(mod=="N"):
                print("\033[2J\033[1;1F")
                return regie()
            while(mod!="S" or mod!="N"):
                print("\033[2J\033[1;1F")
                return regie()
        if(op==2):
            achie=open("registro_de_empleados.txt",mode="r",encoding="utf-8")
            empl=achie.read();#Saca la lista de empleados
            achie.close()
            emple=""
            c=0
            for i in (empl):
                if(i=="'"):
                    c+=1
                else:
                    emple=emple+i
            empl=emple
            empl=empl.split(",")
            dempl={}#diccionario de empleados
            for empl in (empl):
                dempl[empl.split(":")[0]]=empl.split(":")[1]
            ven(100,10)
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Selecciono modificar registro de empleados"));
            print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Los empleados actualmente registrados son-> {dempl}"));
            print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Si desea agregar un empleado inserte A, si desea eliminar un empleado E"));
            print(Cursor.POS(2,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("y para salir inserte cualquier cosa"));
            mode=(input());
            if(mode=="A"):
                print("\033[2J\033[1;1F")
                ven(62,10)
                print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Codigo del nuevo empleado "));
                codn=str(input());#codigo del nuevo trabajador
                if(codn not in dempl):        
                    print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Nombre del empleado"));
                    nomn=str(input());#nombre del nuevo empleado
                    achie=open("registro_de_empleados.txt",mode="a",encoding="utf-8")
                    en=","+codn+":"+nomn#Para escribie el nuevo codigo en el archivo
                    achie.write(en)
                    achie.close()
                    print("\033[2J\033[1;1F")
                else:
                  print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Ya existe el codigo"))
                  input()
                  print("\033[2J\033[1;1F")
                  return regie()
        
            if(mode=="E"):
                print(Cursor.POS(2,8)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Codigo del empleado a eliminar "));
                bor=(input());#codigo a borrar
                del dempl[bor]
                new=str(dempl);
                new=new.strip("[").strip("]").strip('{').strip('}');
                achie=open("registro_de_empleados.txt",mode="w",encoding="utf-8")
                achie.write(new)
                achie.close()
                print("\033[2J\033[1;1F")
            
        if(op==3):
            ven(25,5)
            print(Cursor.POS(8,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Saliendo..."));
            input()
            print("\033[2J\033[1;1F")
            return menu()
        else:
            return regie()
    
    except:
        return regie()

    input()

def inven():
    try:
        from colorama import Cursor,init,Fore,Back,Style;
        init(autoreset=True)
        achii=open("inventario.txt",mode="r",encoding="utf-8")
        inv=achii.read();#Productos que se tiene
        achii.close()
        inve=""
        for i in (inv):#for para quitar '
                    if(i!="'"):
                        inve=inve+i
        inv=inve
        inv=inve.split("-")
        dinv={}#diccionario de productos
        for inv in (inv):
            dinv[inv.split(":")[0]]=inv.split(":")[1]
        ven(100,10)
        print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Selecciono inventario"));
        print(Cursor.POS(2,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+(f"Los productos en existencia son-> {dinv}"));
        print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Si desea agregar un prucucto inserte A, si desea modificar el invertario M, si deceas eliminar un producto E y para salir inserte cualquier cosa"));
        mi=str(input());#Opcion de que hacer con el inventario
        if(mi=="A"):
            print("\033[2J\033[1;1F")
            ven(100,18)
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Codigo del nuevo producto"));
            codp=str(input());#codigo del producto
            if(codp not in dinv):        
                print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Nombre del producto"));
                nomp=str(input());#nombre del nuevo producto
                print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Cantidad del producto"));
                capn=int(input());#cantidad de productos
                print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Precio del producto"));
                ppro=float(input());#precio del producto
                achii=open("inventario.txt",mode="a",encoding="utf-8")
                nomp=str(nomp)
                capn=str(capn)
                ppro=str(ppro)
                pn="-"+codp+":"+nomp+","+capn+","+ppro#Para escribie el nuevo codigo en el archivo
                achii.write(pn)
                achii.close()
            else:
                print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Ya esta un producto registrado con ese codigo"))
                input()
                print("\033[2J\033[1;1F")
                return inven()
            
        if(mi=="E"):
            print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Codigo del  producto a eliminar"));
            codpb=str(input());#codigo del producto borrado
            del dinv[codpb]
            newi=str(dinv);
            newi=newi.strip('{').strip('}').strip("\ufeff");
            newi=newi.replace("',","-");
            newi=newi.replace(" ","");
            achii=open("inventario.txt",mode="w",encoding="utf-8")
            achii.write(newi)
            achii.close()
            
        if(mi=="M"):
            print("\033[2J\033[1;1F")
            ven(100,18)
            print(Cursor.POS(2,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Codigo del  producto a modificar"));
            codpm=str(input());#codigo del producto borrado
            del dinv[codpm]
            newi=str(dinv);
            newi=newi.strip('{').strip('}').strip("\ufeff");
            newi=newi.replace("',","-");
            newi=newi.replace(" ","");
            achii=open("inventario.txt",mode="w",encoding="utf-8")
            achii.write(newi)
            achii.close()
            print(Cursor.POS(2,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Nombre del producto"));
            nomp=str(input());#nombre del nuevo producto
            print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Cantidad del producto"));
            capn=int(input());#cantidad de productos
            print(Cursor.POS(2,9)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("Precio del producto"));
            ppro=float(input());#precio del producto
            nomp=str(nomp)
            capn=str(capn)
            ppro=str(ppro)
            newi="-"+codpm+":"+nomp+","+capn+","+ppro
            achii=open("inventario.txt",mode="a",encoding="utf-8")
            achii.write(newi)
            achii.close()
            input()
            print("\033[2J\033[1;1F")
            return menu()
            
        else:
            print(Back.WHITE+Fore.BLUE+Style.BRIGHT+("Saliendo..."));
            input()
            print("\033[2J\033[1;1F")
            menu()
    except:
        return inven()
    
    input()
    
def menu():
    from colorama import Cursor,init,Fore,Back,Style;
    init(autoreset=True)
    lo=[1]
    y=4
    achie=open("registro_de_empleados.txt",mode="r",encoding="utf-8")
    empl=achie.read();#Saca la lista de empleados
    achie.close()
    emple=""
    c=0
    for i in (empl):
        if(i=="'"):
            c+=1
        else:
            emple=emple+i
            empl=emple
            empl=empl.split(",")
            dempl={}#diccionario de empleados
    for empl in (empl):
        dempl[empl.split(":")[0]]=empl.split(":")[1]
    codn=str(input("Ingrese su codigo "));#codigo del trabajador
    if(codn not in dempl):
        print("Codigo incorrecto")
        return menu()
    else:
        si=codn
        print("\033[2J\033[1;1F")
        pass
    for i in (lo):
        lo+=[2]
        ven(55,10)
        print(Cursor.POS(20,3)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("MENU"))
        print(Cursor.POS(6,4)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("1-Caja"));
        print(Cursor.POS(6,5)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("2-Inventario"));
        print(Cursor.POS(6,6)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("3-Registro de empresa"));
        print(Cursor.POS(2,7)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("4-Teacla esc para salir"));
        print(Cursor.POS(2,y)+Back.WHITE+Fore.BLUE+Style.BRIGHT+("-->"));
        x=funkeypress()
        if x == 18656:
            print("\033[2J\033[1;1F")
            y-=1
        if x == 20704:
            print("\033[2J\033[1;1F")
            y+=1
        if (x == 13):
            if(y==4):
                print("\033[2J\033[1;1F")
                return vender(si)
            if(y==5):
                print("\033[2J\033[1;1F")
                return inven()
            if(y==6):
                print("\033[2J\033[1;1F")
                return regie()
        if x == 27:
            input()
        if(y==7):
            y=4
        if(y==3):
            y=6
        elif(x!=27 or x!=18656 or x!=20704 or x!=13):
            print("\033[2J\033[1;1F")
            continue
        

    input()

def ven(x,y):#ventana con for
    from colorama import init,Back,Fore;
    init(autoreset=True)
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x-3)+("--[]X"));
    for i in range(y):
        print(Back.MAGENTA+(" ")+Back.WHITE+(" ")*x+Back.MAGENTA+(" "));
    print(Fore.WHITE+Back.MAGENTA+(" ")*(x+2));

def funkeypress():
    """
    Waits for the user to press any key including function keys. Returns 
    the ascii code for the key or the scancode for the function key.
    """
    import msvcrt
    while 1:
        if msvcrt.kbhit():                  # Key pressed?
            a = ord(msvcrt.getch())         # get first byte of keyscan code  
            if a == 0 or a == 224:          # is it a function key?
                b = ord(msvcrt.getch())     # get next byte of key scan code
                x = a + (b*256)             # cook it.
                return x                    # return cooked scancode
            else:
                return a        

    
menu()
