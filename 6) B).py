import sqlite3 as SQL
import matplotlib.pyplot as plt


# Conectamos la base de datos SQLite3
conexion = SQL.connect('Sql_data/db_personas.db')
consulta = conexion.cursor()

# Ejecutamos una consulta para obtener los datos que necesitamos
consulta.execute("SELECT profesion, COUNT(*) FROM personas GROUP BY profesion")

# Guardamos las profesiones en una variable agrupadas con GROUP BY
profesiones = [dato[0] for dato in consulta]
# Guardamos el conteo de las profesiones en una variabkle
conteos = [dato[1] for dato in consulta]

# Crear el gráfico de tartas
plt.pie(conteos, labels=profesiones, autopct='%1.1f%%', startangle=90)
# Datos conteos, etiquetas(profesiones), los datos se aproximan con solo 1 decimal, el grafico comienza en el angulo 90
plt.title('Gráfico de Tartas') # Le asignamos un nombre al grafico

# Mostrar el gráfico
plt.show()
