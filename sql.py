import  mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="albin@democracy@1234",
        database='mydatabase')

print(mydb)

mycursor=mydb.cursor()

def show_table():
    mycursor.execute("SHOW TABLES")
    for db in mycursor:
        print(db)

def isUsenameAvailable(name):
    mycursor.execute(f"SELECT username FROM loginpage WHERE username='{name}'")
    for x in mycursor:
        return len(x)

# mycursor.execute("CREATE TABLE loginpage(username varchar(50) PRIMARY KEY, password varchar(50))")
print(isUsenameAvailable(("Albin Reji")))