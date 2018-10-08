import os, sys
import MySQLdb
import signal, os, sys

db = MySQLdb.connect(host='localhost',    # tu host, usualmente localhost
                     user='root',         # tu usuario
                     passwd='diego',  # tu password
                     db='prueba') # el nombre de la base de datos


a=db.cursor()

sql='select * from audio;'
a.execute(sql)

countrow=a.execute(sql)
print("Number date",countrow)
data=a.fetchall()
print(data)











