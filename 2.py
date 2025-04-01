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


mycursor.close()
mydb.close()