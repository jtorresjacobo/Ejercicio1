import os, sys
import MySQLdb
import signal, os, sys

def connection():
	db = MySQLdb.connect(host='localhost',    # tu host, usualmente localhost
	                     user='root',         # tu usuario
	                     passwd='jacobo',  # tu password
	                     db='Audios') # el nombre de la base de datos
	return db


def input(usuario,path,detalles):

	c=connection()
	a=c.cursor()

	sql="insert File values('"+usuario+"','"+path+"','"+detalles+"');"

	a.execute(sql)

	countrow=a.execute(sql)
	print("Number date",countrow)
	data=a.fetchall()
	print(data)
	c.commit()
	c.close()













