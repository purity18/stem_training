from lib2to3.pytree import LeafPattern


fruit={"apples","banana","oranges"}
print(fruit)
print(fruit)
print(fruit)


def output(a):
    print("hi",a)
output("mii")


#function to replace character instring
def replace_in(phrase):
    word=""
    for letter in phrase:
        if letter.lower()in "aeiou":
            word=word+"g"
        else:
            word=word+letter
    return word
print(replace_in(input("enter a phrase:")))




