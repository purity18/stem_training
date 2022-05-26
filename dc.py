#dictionaries in python
mydict={
"Book": "Dynamies",
"publisher" :"longhorn",
"year":2001,
"authors":["Kim","John"]
}

#accessing item
x=mydict["year"]
print(x)

#accessing using get
y=mydict["year"]
print(y)

#all keys
x=mydict.keys()
print(x)

#all vaues
x=mydict.values()
print(x)

#Prnting all items in dictionary
x=mydict.items()
print(x)

#checking key errror
if"publisher in mydict:" :
    print("publisher is one of the keys")

#dictionaries can hold diff data types


