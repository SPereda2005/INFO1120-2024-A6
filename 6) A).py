import sqlite3 as SQL
import matplotlib.pyplot as plt
import pandas as pd
# Conectamos nuetra base de datos
conexion = SQL.connect("Sql_data/db_personas.db")
# Hacemos la consulta SQL
Dataframe = pd.read_sql_query("SELECT Pe.fecha_ingreso, Sa.rol, Pe.residencia, Pe.rut, Pe.nombre_completo, Pe.nacionalidad, Pe.fecha_de_nacimiento, Pe.profesion, Sa.Sueldo FROM personas AS Pe JOIN Salarios AS Sa ON Pe.id_rol = Sa.id_salarios", conexion)
# Creamos una variable que agrupa las profesiones y saca el promedio de los sueldos
Barra = Dataframe.groupby('profesion')['Sueldo'].mean()
plt.xlabel('profesion') # Eje y llamado profesion
plt.xlabel('Sueldo') # Eje x llamado sueldo
plt.title('Sueldo promedio x profesion') # Ponemos nombre al grafico 
plt.bar(Barra.index, Barra.values) # Agregamos las profesiones agrupadas al eje X y los sueldos promediados al eje Y
plt.show() # Mostramos el grafico




