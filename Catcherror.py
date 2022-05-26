#try except in python to catch errors
from multiprocessing.dummy import Value


try :
    div=10/0
    value=int(input("Enter a number:"))
    print(value)
except ValueError:
    print("invalid num entered")
except ZeroDivisionError:
    print("divided by zero")



