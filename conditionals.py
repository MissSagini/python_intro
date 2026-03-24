# if the language is python then give a welcome language
language = "Python"
if language == "Python": 
    print("Welcome to python programming!")
language = "Javascript"
if language == "Python": 
    print("Welcome to python programming!")
else: 
    print("select your language")

name = "Sagini"
if name == "Sagini":
    print("Sagini is a young lady!")
name = "Cynthia"
if name == "Sagini":
    print("Sagini is a young lady!")
else: 
    print("What do you know about her?")

# Short circuit evaluation
age = 20
if age > 18:
    print("You are an adult! Welcome to the club!")
elif age < 18 and age > 12:
    print("You are a teenager! You can go to class and read!")
else:
    print("You are a toddler!")

age = 16
if age > 18:
    print("You are an adult! Welcome to the club!")
elif age < 18 and age > 12:
    print("You are a teenager! You can go to class and read!")
else:
    print("You are a toddler!")

age = 11
if age > 18:
    print("You are an adult! Welcome to the club!")
elif age < 18 and age > 12:
    print("You are a teenager! You can go to class and read!")
else:
    print("You are a toddler!")