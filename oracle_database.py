import os
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\SANTOSH KOSHTI\Downloads\instantclient_21_6")

try:
    print("database connecting..")
    con = cx_Oracle.connect('scott/tiger@localhost:1521/orcl')
    cur = con.cursor()
    print("database", con.username, "user connected.")

except cx_Oracle.DatabaseError as er:
    print('Hiiiii There is an error in the Oracle database:', er)


# create database
# try:
# 	cur.execute('CREATE TABLE Pynew(urls varchar2(250))')
# 	print("New DataBase Created..")
# except cx_Oracle.DatabaseError as er:
#  	print('DataBase Already exits..', er)

# 1)connect database to python:
# 	import cx_Oracle
# 	cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\SANTOSH KOSHTI\Downloads\instantclient_21_6")
# 	con = cx_Oracle.connect('scott/tiger@localhost:1521/orcl')
# 	cur = con.cursor()

# 2) get data from database to python:
#
# cur.execute(query)
#
# # get all data
# for i in cur.fetchall():
# 	print(i)
#
# # gets specific number of data, default max 100 data gives
# for i in cur.fetchmany(give_some_number):
# 	print(i)
#
# # get only one data
# for i in cur.fetchone():
# 	print(i)
#
# 3) EXECUTEQUERY into database
# 	QUERY = WRITE ANY QUERY LIKE CREATE,UPDATE,INSERT,DELETE
# 	cur.execute(QUERY)
# 	#use last for savig data
# 	con.commit()
#
# 4) QUIT DATABASE
# cur.close()

