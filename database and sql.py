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


    mycursor.execute("SELECT * FROM teacher")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

elif a.lower() == "teacher":
    name = input("Enter what you want to search in name: ")

    sql = "SELECT name FROM teacher WHERE name = %s"
    val = (name,)

    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()

    if myresult:
        print("yes..!", myresult, "was in record")
    else:
        print("No record found.")


mycursor.close()
mydb.close()