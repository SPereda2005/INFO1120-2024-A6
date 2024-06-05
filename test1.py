import sqlite3 as SQL
import pandas as pd


conexion=SQL.connect("db_personas.db")
hola = conexion.cursor()
hola.execute("SELECT rut FROM personas")
como = hola.fetchall()
for k in hola:
    print(k)