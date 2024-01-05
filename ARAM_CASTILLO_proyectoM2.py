###################################################################

#Identifica en que cuadrantre se encuentran las coordenadas

def identificar_cuadrante(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"
    else:
        return None


x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))


if x != 0 and y != 0:
    cuadrante = identificar_cuadrante(x, y)
    if cuadrante:
        print(f"El punto se encuentra en el cuadrante {cuadrante}.")
    else:
        print("El punto se encuentra en el origen.")
else:
    print("Error: Ninguna coordenada puede ser igual a cero.")


##########################################################################

#Identifica la longitud de la palabra ingresada
    

def verificar_longitud_palabra(palabra):
        longitud = len(palabra)

        if 4 <= longitud <= 8:
            print(f"La palabra es correcta. Tiene {longitud} letras")
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras.")
        else:
            print(f"Sobran letras. Tiene {longitud} letras.")


palabra_ingresada = input("Ingrese una palabra: ")


verificar_longitud_palabra(palabra_ingresada)
