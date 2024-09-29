print("Welcome to my Quiz!")
py=input("Do you want to play? ")

if py.lower() !="yes":
    quit()
else:
    print("Wow! let's play :)")
    score=0

py=input("Which keyword is used to define a class in python? ")
if py.lower() == ("class"):
    print("Good job!")
    score +=1
else:
    print("oh,Wrong!")

py=input("What is the keyword is used to define a function in python? ")
if py.lower() == ("def"):
    print("Great! ")
    score +=1
else:
    print("Oops!")

py=input("Which language is popular in Data science,AI,and more? ")
if py.lower() == ("python"):
    print("Excellent!")
    score +=1
else:
    print("Oh,Wrong!")

py=input("Who can learn programming languages? ")
if py.lower() == ("everyone" or "anyone"):
    print("Nice!")
    score +=1
else:
    print("Incorrect!")

py=input("How do you start a comment in python? ")
if py.lower() == ("#"):
    print("Wow!")
    score +=1
else:
    print("Wrong!")


py=input("What is the output of the following code: 'print(2**3)' ? ")
if py.lower() == ("8"):
    print("Excellent!")
    score +=1
else:
    print("Nope!")

py=input("Which python data type is used to store key-value pairs? ")
if py.lower() == ("dictionary"):
    print("Congratulations!")
    score +=1
else:
    print("Incorrect!")

py=input("Which function is used to get the lengh of a list in python? ")
if py.lower() == ("len()"):
    print("Wow!")
    score +=1
else:
    print("Wrong!")

py=input("Which operator is used for exponentiation in python")
if py.lower() == ("**"):
    print("Great!")
    score +=1
else:
    print("Oh,Wrong!")

py=input("Which function is used to sort a list in python? ")
if py.lower() == ("sort"):
    print("Super!")
    score +=1
else:
    print("Incorrect!")
    

print("Congratulations! You Got " + str(score) + " Questions Correct! ")
print("You Got " + str((score/10) * 100) + " %")



