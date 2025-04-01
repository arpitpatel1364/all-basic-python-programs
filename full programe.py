import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

# Uncomment the next line if you need to create the database
# mycursor.execute("CREATE DATABASE scl_student")

mycursor.execute("USE scl_student")

query = input("wich query you want to use (insert/select)?")

if query == "insert":
    a = input("Are you a student or teacher (student / teacher)? ")
    if a.lower() == "student":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        number = input("Enter your phone number: ")
        semester = input("Enter your semester: ")
        branch = input("Enter your branch name: ")

        sql = "INSERT INTO student (name, email, number, semester, branch) VALUES (%s, %s, %s, %s, %s)"
        val = (name, email, number, semester, branch)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    elif a.lower() == "teacher":
        name = input("Enter your name: ")
        number = input("Enter your phone number: ")
        subject = input("Enter your subject detail: ")
        email = input("Enter your email: ")
        age = input("Enter your age: ")

        sql = "INSERT INTO teacher (name,number, subject,email,age) VALUES (%s, %s, %s, %s, %s)"
        val = (name, number, subject, email, age)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
elif query == "select":
    a = input("Are you a student or teacher (student / teacher)? ")
    if a.lower() == "student":
        mycursor.execute("SELECT * FROM student")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    elif a.lower() == "teacher":
        mycursor.execute("SELECT * FROM teacher")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
