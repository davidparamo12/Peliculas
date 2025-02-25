from fastapi import FastAPI
import pandas as pd
import numpy as np

df_mes = pd.read_csv("Dataset/df_tabla_mes")
df_dia = pd.read_csv("Dataset/df_tabla_dia")
df_titulo = pd.read_csv("Dataset/df_tabla_titulo")
df_voto_200 = pd.read_csv("Dataset/df_tabla_voto")
df_actor = pd.read_csv("Dataset/df_tabla_actor")
df_director = pd.read_csv("Dataset/df_nombre_director")

app = FastAPI()

# def cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que
# fueron estrenadas en el mes consultado en la totalidad del dataset.
# Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X


def peli_mes(mes: str):
    mes = mes.lower()
    tabla_mes = df_mes[df_mes == mes].count()
    if tabla_mes.empty:
        return {"error": f"Porfavor digitar correctamente el mes en español---Please write the month in spanish"}
    return f"{tabla_mes} cantidad de peliculas fueron estrenadas en el mes de {mes}"


# API endpoint that calls the function
@app.get("/peli_mes/{mes}")
def get_peli_mes(mes: str):
    message_1 = peli_mes(mes)
    return {"message": message_1}


# def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que
# fueron estrenadas en día consultado en la totalidad del dataset.
# Ejemplo de retorno: X cantidad de películas fueron estrenadas en los días X


def peli_dia(dia: str):
    dia = dia.lower()
    tabla_dia = df_dia[df_dia == dia].count()
    if tabla_dia.empty:
        return {"error": f"Porfavor digitar correctamente el día en español---Please write the day in spanish"}
    return f"{tabla_dia} cantidad de peliculas fueron estrenadas en el dia de {dia}"


# API endpoint that calls the function
@app.get("/peli_dia/{dia}")
def get_peli_mes(dia: str):
    message_2 = peli_dia(dia)
    return {"message": message_2}


# def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta
# el título, el año de estreno y el score.
# Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X

def score(titulo: str):
    titulo = titulo.lower()
    tabla_titulo = df_titulo[df_titulo == titulo]
    if tabla_titulo.empty:
        return {"error": f"No se encontró ningún titulo con el nombre {titulo}"}
    voto_prome = tabla_titulo["vote_average"]
    año = tabla_titulo["release_año"]
    popularity_1 = tabla_titulo["popularity"]
    return f"La pelicula {titulo} fue estrenada el año {año} con una popularidad de {popularity_1} y un promedio de votos de {voto_prome}"

# API endpoint that calls the function


@app.get("/score/{titulo}")
def get_score(titulo: str):
    message_3 = score(titulo)
    return {"message": message_3}


# def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título,
# la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
# Ejemplo de retorno: La película X fue estrenada en el año X. La misma cuenta con un total de X valoraciones, con un promedio de X

def score_2000(titulo: str):
    titulo = titulo.lower()
    tabla_titulo_2000 = df_voto_200[df_voto_200 == titulo]
    if tabla_titulo_2000.empty:
        return f"Esta pelicula no se encuentra en nuestra base de datos. Es probable que tenga menos de 2000 valoraciones."
    votos = tabla_titulo_2000["vote_count"]
    promedio = tabla_titulo_2000["vote_average"]
    año = tabla_titulo_2000["release_year"]
    return f"La pelicula {titulo} tiene {votos} valoraciones y tiene un promedio de {promedio}"

# API endpoint that calls the function


@app.get("/score_2000/{titulo}")
def get_score(titulo: str):
    message_4 = score_2000(titulo)
    return {"message": message_4}

# def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver
# el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno.
# La definición no deberá considerar directores.
# Ejemplo de retorno: El actor X ha participado de X cantidad de filmaciones, el mismo ha conseguido un retorno de X con un promedio
# de X por filmación


def get_actor(actor: str):
    actor = actor.lower()
    tabla_actor = df_actor[df_actor["nombre_actor"] == actor]
    if tabla_actor.empty:
        return {"error": f"Porfavor digitar correctamente el nombre del actor principal"}
    numero_peli = len(tabla_actor)
    suma_actor = tabla_actor["return"].sum()
    prom_actor = suma_actor/numero_peli
    return f"El actor {actor} tiene un retorno total de {suma_actor} con un promedio de {prom_actor}"


# API endpoint that calls the function


@app.get("/get_actor/{actor}")
def get_score(titulo: str):
    message_5 = get_actor(titulo)
    return {"message": message_5}


# def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo
#  devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento,
# retorno individual, costo y ganancia de la misma.


def get_director(director: str):
    director = director.lower()
    tabla_director = df_director[df_director["nombre_director"] == director]
    if tabla_director.empty:
        return {"error": f"No se encontró ningún director con el nombre {director}"}
    numero_peli_dir = len(tabla_director)
    suma_director = tabla_director["return"].sum()
    prom_director = suma_director/numero_peli_dir
    return f"El director {director} tiene un retorno total de {suma_director} con un promedio de {prom_director}"


# API endpoint that calls the function


@app.get("/get_director/{director}")
def get_dir(director: str):
    message_6 = get_director(director)
    return {"message": message_6}
