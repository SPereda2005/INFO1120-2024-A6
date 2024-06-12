import pandas as pd
import sqlite3 as SQL

# Creamos la conexion con la base de datos 
conexion = SQL.connect("Sql_data/db_personas.db")

# Creamos una variable que creara un dataframe con una consulta sql, y esta sera extraida de la conexion anteriormente hecha
df = pd.read_sql_query("SELECT Pe.fecha_ingreso, Sa.rol, Pe.residencia, Pe.rut, Pe.nombre_completo, Pe.nacionalidad, Pe.fecha_de_nacimiento, Pe.profesion, Sa.Sueldo FROM personas AS Pe JOIN Salarios AS Sa ON Pe.id_rol = Sa.id_salarios", conexion)

Dataframe = pd.DataFrame(df)
# Mostramos por pantalla el dataframe
print(Dataframe)




