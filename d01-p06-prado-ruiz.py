#practica 06
#prado núñez luis armando
#ruiz rodriguez jorge missael


print("Practoca 06");
print("Prado Núñez Luis Armando");
print("Ruiz Rodriguez Jorge Missael");
print(".........................................");
print("");
print("Para llamar un ejercicio inserte e mas el numero de ejercicio seguido de () ejemplo: e01()");
print("");

def e01():#ejercicio 1
      em=80       #promedia de matematicas
      tm=(10+50+60)/3
      emp=em*0.60
      tmp=tm*0.40
      pm=emp+tmp/2
      print("¿Cual es el promedio de cada materia y promedio total?");
      print("");
      print("El promedio de matematicas es",pm);

      ef=80
      tf=(10+50+60+10+50)/5
      efp=ef*0.40
      tfp=tf*0.60
      pf=efp+tfp/2
      print("El promedio de fisica es",pf);

      eq=80
      tq=(10+50+60+10+50+60+10+50+60)/9
      eqp=eq*0.85
      tqp=tq*0.15
      pq=eqp+tqp/2
      print("El promedio de quimica es",pq);

      pt=(pm+pf+pq)/3
      print("Promedio total es",pt)

def e02():#ejercicio2
      cap=900
      gan=cap*0.08

      print("¿Cual es la capital del individuo?");
      print("");
      print("La capital mas su sueldo total es",gan);


def e03():#ejercicio3
      sub=1050
      com=sub*0.10
      sume=sub*4
      suan=sume*12
      comanu=com*4
      com10=comanu*10
      total=com10+suan

      print("El sueldo base del vendedor es",sub);
      print("Su commision de venta es",com);
      print("Su sueldo mensual es",sume);
      print("Su sueldo anual es",suan);
      print("¿cuanto ganara en un año con 10 meses de comision?");
      print("Su ganancia total es",total);


def e04():#ejercicio4
      com=250
      des=com*0.153
      pt=com-des
      print("un hombre hizo una compra de 250$, la cual la tienda hace un descuento 15.3% en compra");
      print("¿Cuanto tiene que pagar con el descueto incluido?");
      print("La paga total es",pt);

def e05():#ejercicio5
      par=(80+80)/2
      ef2=65
      tf2=95
      pp=par*0.55
      pef2=ef2*0.30
      ptf2=tf2*0.15
      promt=pp+pef2+ptf2
      print("¿Cuale es la calificaion final?");
      print("");
      print("La calificacion final es",promt);
      
def e06():#ejercicio 6
      h,m=50,30
      g=h+m
      print("El grupo esta formado de 80 estudiantes 50 son hombres y 30 mujeres");
      hp=h*100/g
      mp=m*100/g
      print("El porcentaje de hombres en el salon es --->",hp);
      print("");
      print("E porcetaje de mujeres en el salon es ---->",mp);

def e07():#ejercicio 7
      fact,fn=2018,1999
      print("¿Cuantos años tinene una persona que nacio en 1999 en el 2018? ");
      edad=fact-1999
      print("");
      print("La persona tiene ----->",edad);
      
def e08():#ejercicio 8
      pre=1000000
      print("Un hospital recibe 1000000 el cual se reparte en tres áreas en las cuales se reparte de la siguiente manera:");
      print("Ginecología:40%, Traumatologia:30% y Pedriatría:30%");
      presupuestom=1000000/12
      gina=40*1000000/100
      traa=30*1000000/100
      peda=30*1000000/100
      ginm=40*presupuestom/100
      tram=30*presupuestom/100
      pedm=30*presupuestom/100
      print("");
      print("Ginecologia en un año recibe --->",gina);
      print("Traumalogía en un año recibe --->",traa);
      print("Gunecologia en un año recibe --->",peda);
      print("Ginecologia en un mes recibe --->",ginm);
      print("Traumalogía en un mes recibe --->",tram);
      print("Gunecologia en un mes recibe --->",pedm);

def e90():#ejercicio 9
      print("Se compró un carro en 30000 y se le quiere ganar el 35%");
      carro=30000
      porcen=35*carro/100
      total=carro+porcen
      print("");
      print("En el precio que lo tiene que vender es --->",total);

def e10():#ejercicio 10
      print("Un joven corre lunes, miercoles y viernes 1km");
      print("El lunes tardo 38m, el miercoles 40m y el viernes 35m");
      semana=113/3
      print("");
      print("En promedio tarda",semana);

def e11():#ejercicio 11
      print("Tres personas invierten en una empresa");
      print("El primero invierte 100000 el sugundo 25000 y el tercero 75000");
      pri=100000
      segun=25000
      terc=75000
      invert=pri+segun+terc
      prip=pri*100/invert
      segunp=segun*100/invert
      tercp=terc*100/invert
      print("La inversion total es --->",invert);
      print("El primero invirtió --->",prip);
      print("El segundo invirtió --->",segunp);
      print("El tercero invirtió --->",tercp);
      
