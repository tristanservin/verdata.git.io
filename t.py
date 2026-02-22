x = int(input("Ingrese su edad: "))
if x >= 18:
    print("Eres mayor de edad")
else:   
     print("Eres menor de edad")


y=float(input("cuantas horas trabajaste:"))
if y > 3:
     print("Tienes buena productividad")
else:     print("Tienes mala productividad")


hecta=float(input("Cuantas hectareas sembraste:"))
rendimiento= float(input("Cual es el rendimiento por hectarea(toneladas):"))
produccion= hecta * rendimiento
if produccion >= 10:
    print("alta produccion")
else:     print("normal produccion")

precio=float(input("Cual es el precio del producto:"))
ingresos= produccion * precio
if ingresos > 30000:
    print("Tienes buenos ingresos")
elif ingresos >= 15000:
    print("Tienes ingresos normales")
else:     print("Tienes bajos ingresos")

temperatura=float(input("Cual es la temperatura actual:")) 
if temperatura <10:
    print("Hace frio")
elif temperatura >= 10 and temperatura < 25:
    print("Hace un clima agradable")
else:     print("Hace calor")



edad=int(input("Ingrese su edad:"))
if edad < 18:  
        print("sigue aprendiendo")  
elif edad >= 18 and edad < 25:  
        print("ten mas experiencia")  
elif edad >= 25:  
        print("concentrate en tu trabajo")