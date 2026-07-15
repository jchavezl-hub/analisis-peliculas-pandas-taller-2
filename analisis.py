import pandas as pd

datos = pd.read_csv("peliculas.csv")

nuevo = datos[["titulo", "genero", "calificacion"]].copy()
def clasica(anio):
    if anio < 1995:
        return "Si"
    else:
        return "No"

nuevo["Clasica"] = datos["anio"].apply(clasica)

def clasificacion(nota):

    if nota > 8.5:
        return "Excelente"
    elif nota >= 7:
        return "Buena"
    elif nota >= 5:
        return "Regular"
    elif nota >= 3:
        return "Mala"

    else:
        return "Pesima"

nuevo["Apreciacion"] = datos["calificacion"].apply(clasificacion)


nuevo.to_csv("peliculas_procesadas.csv", index=False)

promedio = datos.groupby("genero")["calificacion"].mean()

cantidad = datos.groupby("genero")["titulo"].count()

with pd.ExcelWriter("estadisticas.xlsx") as archivo:


    promedio.to_excel(archivo, sheet_name="Promedio")

    cantidad.to_excel(archivo, sheet_name="Cantidad")

print("Archivo creado correctamente.")