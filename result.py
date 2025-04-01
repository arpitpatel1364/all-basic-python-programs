name=input("enter your name")
rollnum=input("enter your rollnum")
eng=int(input("enter your english marks"))
guj=int(input("enter your gujrati marks"))
sci=int(input("enter your science marks"))
sosc=int(input("enter your social science marks"))
sct=int(input("enter your sanscrit marks"))
com=int(input("enter your computer marks"))
total_marks=eng+guj+sci+sosc+sct+com
average_marks = (total_marks / 6)
percentage = (total_marks / 600) * 100
print("total mark=",total_marks,"average mark=",average_marks,"percentage=",percentage)


