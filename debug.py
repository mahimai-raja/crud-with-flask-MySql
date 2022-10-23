import mysql.connector as conn

# // TODO - Change your credentials

mysql = conn.connect(host='localhost',user='YOUR_USERNAME',password='YOUR_PASS',auth_plugin='mysql_native_password', database='DBMS')  # MySql object

mycursor = mysql.cursor() # Cursor Object

try :
    mycursor.execute("desc students")  # Structure of the relation
    heading = [column[0] for column in mycursor.fetchall()]  # Relation's attribute name

    # TODO Try out : fetchone(), fetctmany()

    mycursor.execute("SELECT * FROM students") # Retrieving all the values in each records
    data = mycursor.fetchall() # List of tubles is assigned to the variable

    print(heading)
    print(data)
    print('Executed successfully')

except Exception as e:
    print(e)  # In case of error 

finally :
    print('iKurious ! ! ! ')


