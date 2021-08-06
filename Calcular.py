#juan camilo niño crear funcion multiplicar
def multiplicar():
    numero=int(input("ejecutara el programa cuantas veces ="))

    for t in (1,numero):
        num1=float(input("ingrese un numero="))
        num2=float(input("ingrese numero dos ="))
        multi=num1*num2
        print("su multiplicacion es =" + str(multi))


    print("se termino el programa :)")
multiplicar()