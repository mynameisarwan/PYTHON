#psycopg2 nya sudah di test dari command line buka python test_database.py

import psycopg2 as pg2

connect = pg2.connect(database = 'DBSHOOL',user = 'postgres',password = '123')
cursor = connect.cursor()
cursor.execute('SELECT * FROM tbl_student;')
data = cursor.fetchall()
for entry in data:  
	print(entry)