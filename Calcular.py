def multiplicar():

    numero1=int(input("ejecutara el programa cuantas veces ="))

    for t in (1,numero1):
        num1=float(input("ingrese un numero="))
        num2=float(input("ingrese numero dos ="))
        multi=num1*num2
        print("su multiplicacion es =" + str(multi))


    print("se termino el programa :)")

def resta():

   num1=float(input("ingrese el numero:"))
   num2=float(input("ingrese el segundo:"))
   resta=num1-num2
   print(resta)
   print("la resta es :",resta)

def suma():
    num1=float(input("Ingrese el numero: "))
    num2=float(input("Ingrese el numero: "))
    suma=num1+num2
    print ("El resultado de la suma es: ",suma)

def divicion ():
    nume1=float(input('ingrese el numero1: '))
    nume2=float(input('ingrese el numero2: '))
    resultado=nume1/nume2
    print(resultado)

print ("Si quieres multiplicar = 1")
print ()
print ("Si quieres restar = 2 ")
print ()
print ("Si quieres dividir = 3")
print ()
print ("Si quieres sumar = 4")
print ()
numero=int(input())
print ()
if numero==1 :
    multiplicar()
elif numero==2 :
    resta()
elif numero==3 :
    divicion()
elif numero==4 :
    suma()