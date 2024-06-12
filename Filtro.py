import sqlite3 as SQL
import pandas as pd

# Creamos la conexion con la base de datos 
conexion = SQL.connect("Sql_data/db_personas.db")

# Creamos una variable que creara un dataframe con una consulta sql, y esta sera extraida de la conexion anteriormente hecha
df = pd.read_sql_query("SELECT Pe.fecha_ingreso, Sa.rol, Pe.residencia, Pe.rut, Pe.nombre_completo, Pe.nacionalidad, Pe.fecha_de_nacimiento, Pe.profesion, Sa.Sueldo FROM personas AS Pe JOIN Salarios AS Sa ON Pe.id_rol = Sa.id_salarios", conexion)

# Creamos la funcion para el filtro
def Datospersonas(df : pd.DataFrame, nombre):
    # Ciclo while para la validacion
    while True:
        try:
            nombre = str(input('Ingresa el nombre completo de la persona: ')) # Pedimos el nombre completo de la persona
            sub_df = df[df['nombre_completo'] == nombre] # El nombre ingresado es igual al del dataframe

            fila = sub_df.iloc[0]
            fecha_ingreso = fila['fecha_ingreso'] 
            rol = fila['Rol']
            residencia = fila['residencia']
            rut = fila['rut']
            nombre_completo = fila['nombre_completo']
            nacionalidad = fila['nacionalidad']
            fecha_nacimiento = fila['fecha_de_nacimiento']
            profesion = fila['profesion']
            salario = fila['Sueldo']
   
            return fecha_ingreso, rol, residencia, rut, nombre_completo, nacionalidad, fecha_nacimiento, profesion, str(salario)
        except:
            ValueError
            print("Error al ingresar un nombre, intentelo nuevamente.")
    

datospersona = Datospersonas(df, 'Nombre de la persona')


for k in datospersona:
    print(k)