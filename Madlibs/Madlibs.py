# String Concatenation(How to put strings together)
# Suppose we want to create a string that says " Hello Python _________"
#a = "World" # (Some string variable)

# There are also few ways to do this
#print("Hello Python " + aawesome)
#print("Hello Python {}".format(a)) # this formatting helps in putting the variables value into that curly braces.
#print(f"Hello Python {a} ") #f string method to print anything.

adj = input("Adj : ")
verb1 = input("Verb1 : ")
verb2 = input("Verb 2 : ")
fp = input("Famous Person : ")

madlib = f"CP is so {adj}! It makes me excited all the time because\
I love to {verb1}.Stay Hydrated and {verb2} like you are {fp}!"
print(madlib)
           # that slash is a next line indication