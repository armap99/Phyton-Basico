#practica 07
#prado núñez luis armando
#ruiz rodriguez jorge missael


print("Practica 07");
print("Luis Armnado Prado Núñez");
print("Jorge Missael Ruiz Rodriguez");
print("-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-");
print("Para llamar un ejercicio inserte e mas el numero de ejercicio seguido de () ejemplo: e01()");
print("");

def e01():#ejercicio 01
    calificacion=float(input("Inserte calificacion -> "));
    if(calificacion>100):
        print("Valor no valido");
    if(calificacion<0):
        print("Valor no valido");
    elif(calificacion<80):
        print("Reprobaste");
    elif(80<calificacion<101):
        print("Aprobaste");

def e02():#ejercicio 02
    sueldo=float(input("Inserte su sueldo "));
    if(sueldo<0):
        print("Valor no valido");
    elif(sueldo>9000):
        aumento1=sueldo*0.12
        nsueldo=sueldo+aumento1
        print("Tienes un aumento del 12% tu sueldo final es ->",nsueldo);
    elif(sueldo<9000):
        aumento2=sueldo*0.30
        nsueldo2=sueldo+aumento2
        print("Tienes un aumento del 30% tu sueldo final es ->",nsueldo2);

def e03():#ejercicio 03
    print("La hora se paga a $9.26");
    htrabajadas=float(input("Inserte numero de horas trabajadas "));
    if(htrabajadas<0):
        print("Valor no valido");
    if(htrabajadas>100):
        print("Valor no valido");
    if(0<htrabajadas<40):
        ght1=htrabajadas*9.26
        print("Hoy ganaste -> ",ght1);
    if(40<htrabajadas<48):
        hrse1=htrabajadas-40
        phrse1=hrse1*18.52
        ght2=phrse1+370.4
        print("Hoy ganaste  -> ",ght2);
    if(48<htrabajadas<101):
        hrse2=htrabajadas-48
        phrse2=hrse2*27.78
        ght3=phrse2+518.56
        print("Hoy ganaste  -> ",ght3);

def e04():
    hijos=int(input("Cuantos hijos tienes "));
    if (hijos<=0):
        print("Valor no valido");
        return e04()
    elif (hijos<3):
           h2=70.00
           print("recibiras $",h2);
           hi_es=int(input("Cuantos hijos titnes en edad escolar de 6 entr 18 años "));
           he=hi_es*10
           print ("Recibiras $",he,"por tus hijos en edad escolar");
           v=int(input("Eres viudo(a)?  si=1  no=2 "));
           if (v<=0 or v>=3):
                 print("Dato no valido")
                 return e04()
           if (v==1):
                 vs=20.00
                 print("recibiras $",vs,"por ser viudo(s)");
                 print("");
                 to1=h2+he+vs
                 print("Usted recibira el apoyo total de $",to1);
           if (v==2):
                 print("No recibira este apoyo");
                 print("");
                 to2=h2+he
                 print("Usted reecibira el apoyo total de $",to2);
    elif (hijos>=3 or hijos<5):
           h5=90.00
           print("recibiras $",h5);
           hi_es=int(input("Cuantos hijos titnes en edad escolar de 6 entr 18 años "));
           he=hi_es*10
           print ("Recibiras $",he,"por tus hijos en edad escolar");
           v=int(input("Eres viudo(a)?  si=1  no=2 "));
           if (v<=0 or v>=3):
               print("Dato no valido")
               return e04()
           if (v==1):
                 vs=20.00
                 print("recibiras $",vs,"por ser viudo(s)");
                 print("");
                 to1=h5+he+vs
                 print("Usted recibira el apoyo total de $",to1);
           if (v==2):
                 print("No recibira este apoyo");
                 print("");
                 to2=h5+he
                 print("Usted reecibira el apoyo total de $",to2);
    elif (hijos>5):
           h6=120.00
           print("recibiras $",h6);
           hi_es=int(input("Cuantos hijos titnes en edad escolar de 6 entr 18 años "));
           he=hi_es*10
           print ("Recibiras $",he,"por tus hijos en edad escolar");
           v=int(input("Eres viudo(a)?  si=1  no=2 "));
           if (v<=0 or v>=3):
               print("Dato no valido")
               return e04()
           if (v==1):
                 vs=20.00
                 print("recibiras $",vs,"por ser viudo(s)");
                 print("");
                 to1=h6+he+vs
                 print("Usted recibira el apoyo total de $",to1);
           if (v==2):
                 print("No recibira este apoyo");
                 print("");
                 to2=h6+he
                 print("Usted reecibira el apoyo total de $",to2);
                  
def e05():#ejercicio 05
    Dn=int(input("Cual es su dia de nacimiento "));
    if (Dn<0):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    if (Dn>31):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    Mn=int(input("Que mes nacistes "));
    if (Mn<0):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    if (Mn>13):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    Añ=int(input("Que año nacistes "));
    ed=2018-Añ
    if (Añ>2018):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    if (Añ<1900):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    if (ed>17):
        print("Prodas formar parte del equipo de voleibol")
    elif (ed<18):
           print("No podras ser parte del equipo");
           ff=print("Repirte otra vez todo");
           return ff
    Ge=int(input("Que grado escolar cursas "));
    if (Ge<0):
        print ("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    if (Ge>9):
        print ("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    Gu=int(input("En que grupo estas 1=A  2=B  3=C : "));
    if (Gu<0):
        print("Daton no valido");
        ff=print("Repirte otra vez todo");
        return ff
    if (Gu>3):
        print ("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    Pro=int(input("Tu promedio total sta el ultimo semenestre "));
    if (Pro<80):
        print ("No puedes entrar por tener pormedio bajo lo siento");
        ff=print("Repirte otra vez todo");
        return ff
    elif (Pro>100):
        print("No ahy promedio major a 100");
        ff=print("Repirte otra vez todo");
        return ff
    Ho=int(input("Cual horario prefieres 5=Matutino 6=Vespertino "));
    if (Ho<5):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    if (Ho>6):
        print("Dato no valido");
        ff=print("Repirte otra vez todo");
        return ff
    print("Felicidades por entrar en el equipo de voleibol");
    
def e06():#ejercicio 06
    nauto=int(input("Inserte el numero de auto "));
    millas=float(input("Inserte el número de millas "));
    if(millas<0):
        print("Valor no valido");
    if(millas>600):
        print("Valor no valido");
    if(80<millas<601):
        print("Esta arriba del limite de velocidad");
    kilometros=float(input("Inserte kilometros rcecorridos "));
    if(kilometros<0):
        print("Valor no valido");
    if(200<kilometros<350):
        print("Hace falta mantenimiento de auto");
    gask=float(input("Cuantos kilometros recorre con un litro de gasolina"));
    if(10>gask>16):
        print("Valor no valido");
    if(14<gask<16):
        print("Consume poca gasolina");
    elif(10<gask<13):
        print("Consume algo de gasolina");
    viaje=100*gask
    print("Su auto en un viaje de 100kilometros consume",viaje);
    
def e07():#ejercicio 07
    njuga=int(input("Inserte numero de jugador -> "));
    if(njuga<0):
        print("Valor no valido");
    if(njuga>500):
        print("Valor no valido");
    tiroa=int(input("Cuantos tiros anoto el jugador -> "));
    if(tiroa<0):
        print("Valor no valido");
    if(tiroa>150):
        print("Valor no valido");
    tof=int(input("Inserte tiros fallados -> "));
    if(tof<0):
        print("Valor no valido");
    if(tof>150):
        print("Valor no valido");
    tirot=tiroa+tof   
    print("En total tiro",tirot);
    puntoa=int(input("Cuantos puntos anoto el jugador "));
    if(puntoa>190):
        print("Valor no valido");
    if(puntoa<2):
        print("Valor no valido");
    elif(3<puntoa<6):
        print("Anoto pocos puntos");
    elif(7<puntoa<15):
        print("Anoto puntos acepables");
        triple=puntoa//3
        print("Anoto puntos de tres en promedio ->",triple);
    elif(16<puntoa<22):
        print("Felicidades por sus anotaciones");
        triple=puntoa//3
        print("Anoto puntos de tres en promedio ->",triple2);
        
