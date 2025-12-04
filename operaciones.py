#Funcion que recibe una loista y regresa la sumatoria
def sumar(numeros:list[float]) -> float:
    res=sum(numeros)
    return res

#Funcion que recibe una lista y regresa su promedio
def promediar(numeros:list[float]) -> float:
    if (len(numeros) == 0):
        return 0
    prom = sum(numeros) / len(numeros)
    return prom

#Contar las organizaciones en el archivo CSV  
import pandas as pd  
def contar_org(ruta):
    datos=pd.read_csv(ruta, encoding="latin-1")
    conteo = len(datos)
    return conteo


datos=[10, 20, 35, 1.5, 70.2]
s =sumar(datos)
print(f"La suma de los datos es", s)

p=promediar(datos)
print(f"El promedio de los datos es", p)

cant=contar_org("Organization_v3.csv")
print(f"La cantidad de organizaciones es", cant)

