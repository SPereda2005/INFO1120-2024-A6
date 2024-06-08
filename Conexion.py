import sqlite3 as SQL

# Establecemos una conexion con la base de datos
conexion=SQL.connect("Sql_data/db_personas.db")
# En una variable guardamos el cursor de la base de datos
consulta = conexion.cursor()
# Con la variable anterior que contiene el cursor dentro de la base de datos ejecutaremos nuestra consulta
consulta.execute("SELECT Pe.nombre_completo, Sa.Rol FROM personas AS Pe INNER JOIN Salarios AS Sa ON Pe.id_rol = Sa.id_salarios")
# Luego creamos una consulta que almacene todos los datos devueltos de la consulta
muestra_consulta = consulta.fetchall()
# Con un ciclo for k en la variable muestra_consulta haremos que cuando se muestre por pantalla nuestro codigo se vea mas ordenado
for k in muestra_consulta:
    print(k)

