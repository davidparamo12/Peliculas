Objetivos del primer trabajo es EXTRAER, TRANSFORMAR Y CARGAR datos que se pueden deployar.

Nombre de archivo= ETL
Nombre de archivo final= data_csv (con esta tabla obtenemos los datos finales)

EXTRAER:

1. El primer paso fue importar pocas librerias, las suficientes para poder extraer, transformar y cargar.

2. El uso de pandas permite abrir y juntar ambas bases de datos con la funcion merge-

TRANSFORMAR-

3. El primer problema es que la informacion esta anidada- hay diccionarios dentro de las columnas. 
Se realizan 4 desanidadas de los diccionarios de acuerdo a los parametros de la tarea y que son importantes para 
poder alcanzar el objetivo de crear un MVP en el que se pueda recomendar peliculas:

    1. Se separa CAST- para obtener el nombre del actor especialmente y elimino el resto de columnas. También quito caracteres inutiles para que el nombre del actor quede "nombre_actor". Al obtener el nombre del actor lo agrego a la data completa... repito este proceso para:

    2. CREW- aca obtengo el dato del director. Se quedan dos columnas- job_crew y name_crew

    3. BELONGS TO COLLECTION- Me quedo solo con el titulo y lo agrego a mi data completa. Agrego el titulo en minuscula para que sea mas facil el uso de operaciones posteriores.

    4. PRODUCTION COMPANY-Me quedo solo con el nombre de la productora- Proceso pedido por la tarea.

Para la separacion de los datos se utilizo de la funcion- str.split(",", expand=True). Esta funcion separa por "," el diccionario pero a la vez
genera una gran cantidad de columnas adicionales. Se le pusieron un numero y luego se eliminaron estas columnas adicionales.

Al fusionar el data set credits y movies_dataset, la base de datos inicio con 27 columnas. Al terminar este primer proceso de transformacion se crearon las siguientes columnas- name_actor, job_crew, name_crew, name_movie y name_company

![alt text](image.png)


4. De acuerdo al repositorio se rellenaron los valores vacios con 0 para las variables "revenue" y "budget".

5. Se eliminan los datos nulos de "release_date", "vote_average" y "vote_count". Esto se debe a que mejoramos el rendimiento de los datos.

6. El siguiente paso es transformar la columna "release date" que es fundamental para crear el MVP ya que requerimos los valores diarios y mensuales. 
    1. El primer paso fue usar de la funcion pd.to_datetime de pandas que hace que la columna pase de un dtype=object a datetime64[ns].
    2. Creamos 3 columnas mas para separar por año, mes y dia de la semana. El mes es un entero al igual que dia semana. Por esta razon requerimos de una transformacion para volverlo un string.
    3. Creamos un diccionario para mapear un numero de acuerdo al string que queremos de acuerdo al mes y al dia de la semana. El diccionario esta en lower case para facilitar las busquedas posteriores.
    4. Se eliminan las columnas antiguas y solo quedamos con las columnas release_año (int), release_mes(str), release_dia(str).

7. Los datos "revenue" y "budget" se pasan a enteros y al tipo float. Se genera la division entre ambos para crear la variable "return". Luego todos los vacios son rellenados con ceros. 

8. Se realiza el último barrido de datos- se eliminan las columnas que no sean relevantes y todas los datos que esten nulos de las columnas mas relevantes para el MVP- como el titulo, nombre de actor, nombre de director y nombre de compañia. Por ultimo se filtra la base de datos para que solo esté el nombre del director. La decision de borrar los datos que esten vacios y que solo tengamos los datos del director corresponde por dos razones: 
    1. para que la subida del archivo sea posible a Render. 
    2. Mantener unos datos alineados a lo que pide el repositorio. En este sentido se mantienen los datos de las variables que mas se pidieron en el repositorio.  Queda una tabla de 2.369 filas x 18 columnas

9. Se procede a crear una tabla nueva en tipo CSV para que de ahi se saque toda la informacion para las funciones.




2 PARTE DEL TRABAJO- CREACION DE LAS FUNCIONES

1. Desde un archivo tipo python, sin Jupyter, iniciamos el trabajo.
2. Se importan las librerias correspondientes- en especial sobre Fastapi
