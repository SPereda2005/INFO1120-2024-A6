import sqlite3 as SQL
import matplotlib.pyplot as plt
import pandas as pd

conexion = SQL.connect("Sql_data/db_personas.db")

Dataframe = pd.read_sql_query("SELECT Pe.fecha_ingreso, Sa.rol, Pe.residencia, Pe.rut, Pe.nombre_completo, Pe.nacionalidad, Pe.fecha_de_nacimiento, Pe.profesion, Sa.Sueldo FROM personas AS Pe JOIN Salarios AS Sa ON Pe.id_rol = Sa.id_salarios", conexion)

Barra = Dataframe.groupby('profesion')['Sueldo'].mean()
plt.xlabel('profesion')
plt.xlabel('Sueldo')
plt.title('Sueldo promedio x profesion')
plt.bar(Barra.index, Barra.values)
plt.show()




