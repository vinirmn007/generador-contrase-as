import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,-_#/|@&%$()=?¿¡![]"

def solicitarLongitud():
    longitud = int(input("Ingresa la longitud para tu contraseña: "))
    longitud = validador(longitud)
    return longitud

def validador(longitud):
    while longitud < 8:
        longitud = int(input("La contraseña debe tener al menos 8 caracteres.\nIngresala de nuevo por favor: "))
    return longitud


def generarContra(longitud):
    validador(longitud)
    contra = ""
    for i in range(longitud):
        contra += random.choice(caracteres)
    return contra


def main():
    longitud = solicitarLongitud()
    contra = generarContra(longitud)
    print(f"Tu contraseña es: {contra}")

main()