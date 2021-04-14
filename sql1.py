from sqlite3 import connect

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(user='root', host='localhost', password='nikitaa@23', database='sakila')

mycursor = mydb.cursor()
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)
# mycursor.execute('SHOW TABLES')

mycursor.execute('SELECT * FROM netflix_titles')
myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
#
print(mycursor.rowcount)
#
mycursor.execute("select show_id, release_year from netflix_titles")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

df = pd.read_sql_query('''SELECT * FROM netflix_titles''', mydb)
df1 = pd.DataFrame(df, columns=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description'])
pd.set_option('display.max_columns',12)

filt = (df['release_year']==2020)
print(df.loc[filt,['description','rating','release_year']])
#print(df.head())