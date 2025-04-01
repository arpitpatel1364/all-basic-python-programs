class student:
    def stu(self):
        # f = open("mystudentfile.txt", "x")
        for i in range(5):
            a = input("enter student name: ")
            f = open("mystudentfile.txt", "a")
            f.write(a+ "\n")
    def teacher(self):
        # f = open("teacher.txt", "x")
        for i in range(5):
            a = input("enter teacher name: ")
            f = open("teacher.txt", "a")
            f.write(a + "\n")


