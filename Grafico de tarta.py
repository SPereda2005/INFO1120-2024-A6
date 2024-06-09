import sqlite3
import matplotlib.pyplot as plt


# Conectamos la base de datos SQLite3
conexion = sqlite3.connect('Sql_data/db_personas.db')
cursor = conexion.cursor()

# Ejecutamos una consulta para obtener los datos que necesitamos
cursor.execute("SELECT profesion, COUNT(*) FROM personas GROUP BY profesion")

# Obtenemos los resultados de la consulta
datos = cursor.fetchall()

# Guardamos las profesiones en una variable agrupadas con GROUP BY
profesiones = [dato[0] for dato in datos]
# Guardamos el conteo de las profesiones en una variabkle
conteos = [dato[1] for dato in datos]

# Crear el gráfico de tartas
plt.pie(conteos, labels=profesiones, autopct='%1.1f%%', startangle=90)
# Datos conteos, etiquetas(profesiones), los datos se aproximan con solo 1 decimal, el grafico comienza en el angulo 90
plt.title('Gráfico de Tartas') # Le asignamos un nombre al grafico

# Mostrar el gráfico
plt.show()
