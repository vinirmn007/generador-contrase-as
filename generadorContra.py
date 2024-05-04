import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,-_#/|@&%$()=?¿¡![]"

def generarContra(longitud):
    contra = ""
    for i in range(longitud):
        contra += random.choice(caracteres)
    return contra

print(generarContra(10))