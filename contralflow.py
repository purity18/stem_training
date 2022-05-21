# if statment
x=0
if x >=1 :
    print("Hey i'm still here")
    x-=1
    print(x)
print("Done")
#else statment
x=10
if x==10 :
    print(x)
else :
    print("not 1o")


#elif to reate grading system
grade = int(input("write student score: "))
if grade >80 and grade<101 :
    print("student got an A")
elif grade >=70 and grade<80 :
    print("student got a B")
elif grade >=60 and grade<70 :
    print("student got C")
elif grade >=50 and grade<60 :
    print("Student got D")
else :
    print("Student got E")







