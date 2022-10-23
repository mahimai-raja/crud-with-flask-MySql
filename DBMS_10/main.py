from flask import Flask, render_template, request
import mysql.connector as con

app = Flask(__name__)  # Flask app object

# // TODO - Change your credentials

try :
    conObj = con.connect(host='localhost',user='YOUR_USERNAME',password='YOUR_PASS',auth_plugin='mysql_native_password', database='DBMS') # MySql Object
    print('$$$ Connections Successful $$$')
except Exception as e:
    print(e)
    print('\n\n\n$$$ Error in connection $$$\n\n\n')

mycursor = conObj.cursor() # Cursor Object

mycursor.execute("desc students")  # Structure of the relation 
headings = [column[0] for column in mycursor.fetchall()]  # Relation's attribute name

mycursor.execute("SELECT * FROM students") # Retrieving all the values in each records
data = mycursor.fetchall()


@app.route("/")
def index():
    return render_template("index.html", headings=headings, data=data)

@app.route('/insertF/', methods = ['POST'])
def insertF():
    rollno = request.form['rollno']
    name = request.form['name']
    depart = request.form['depart']
    sql = "insert into students (rollno,name,department) values (%s,%s,%s)"
    values = (rollno, name, depart)
    mycursor.execute(sql, values)
    conObj.commit()
    print("Data Insert Success")
    print('Insertion function is called', rollno, name, depart)
    return render_template('index.html', headings=headings, data=data)


@app.route('/updateF/', methods = ['POST'])
def updatetF():
    Orollno = request.form['oldrollno']
    rollno = request.form['rollno']
    name = request.form['name']
    depart = request.form['depart']
    sql = "update students set rollno=%s,name=%s,department=%s where rollno=%s"
    user = (rollno, name, depart,Orollno)
    mycursor.execute(sql, user)
    conObj.commit()
    print("Data Update Success")

    print('Updation function is called')
    return render_template('index.html', headings=headings, data=data)

@app.route('/deleteF/', methods = ['POST'])
def delectF():
    rollno = request.form['rollno']
    sql = "delete from students where rollno=%s"
    user = (rollno,)
    mycursor.execute(sql, user)
    conObj.commit()
    print("Data Delete Success")
    print('Deletion function is called')
    return render_template('index.html', headings=headings, data=data)


if __name__ == "__main__":
    app.run()


##$$ Author - Mahimai Raja J  $$##
##$$       ( iKurious )       $$##