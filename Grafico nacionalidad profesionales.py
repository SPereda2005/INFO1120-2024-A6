import sqlite3 as SQL
import matplotlib.pyplot as plt
import pandas as pd

conexion = SQL.connect("Sql_data/db_personas.db")

Dataframe = pd.read_sql_query("SELECT nacionalidad, profesion FROM personas as Pe", conexion)

Barra = Dataframe.groupby('nacionalidad')['profesion'].count()
plt.xlabel('profesionales')
plt.xlabel('Nacionalidad')
plt.title('Cantidad de profesionales x nacionalidad')
plt.bar(Barra.index, Barra.values)
plt.show()