import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="[Enter your own password]",
    database="[your database name]"
)

mycursor = mydb.cursor()

sql_formula = # insert the SQL code you want here as a string

mycursor.execute(sql_formula) # this runs the command

myresult = mycursor.fetchall() # this returns what is in the databases

# mydb.commit() # use this if you need to commit a change to the server