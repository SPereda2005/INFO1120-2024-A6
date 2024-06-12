import sqlite3 as SQL
import matplotlib.pyplot as plt
import pandas as pd

# Establecemos una conexion con la base de datos 
conexion = SQL.connect("Sql_data/db_personas.db")
# Hacemos nuestra consulta SQL
Dataframe = pd.read_sql_query("SELECT nacionalidad, profesion FROM personas as Pe", conexion)
# Creamos una variable que guarde las nacionalidades agrupadas y cuante las profesiones
Barra = Dataframe.groupby('nacionalidad')['profesion'].count()
plt.xlabel('Cantidad profesionales') # Eje Y nombrado Cantidad profesionales
plt.xlabel('Nacionalidad') # Eje X nombrado Nacionalidad
plt.title('Cantidad de profesionales x nacionalidad') # Titulo del grafico
plt.bar(Barra.index, Barra.values) # Agregamos las nacionalidades al eje x y la cantidad de profesionales al eje Y
plt.show() # Muostramos el grafico