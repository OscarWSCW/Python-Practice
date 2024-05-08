score = 0
print("hello")
# Ask the user their name
name = input("What is your name? ")
#Greet the user and welcome them to the quiz
print("Welcome to this quiz," ,name) 


print("This quiz is about the earth")
#Ask the user a question and tell the user to answer the question

answer= input("What is the largest country by population?").lower()
if answer == "India".lower():
    print ("Correct!") 
    score += 1
elif answer =="" :
    print("Not sure?")   
else:
    print("Wrong!")
    print("The correct answer is India")

answer1 = input("What is the greenest type of grass?").lower()
if answer1 == "Perennial ryegrass".lower():
    print ("Correct!")   
elif answer1 =="" :
 print("Not sure?")

else:
    print("Wrong!")
    print("The correct answer is Perennial ryegrass")

answer2= "Which country snows the most?"
a = "Canada"
b = "Iceland"
c = "Japan"
d = "Norway"
answer2 = input("{}\nA.{} B.{} C.{} D.{}".format(answer2, a, b, c, d)).lower()
if answer2 == c or answer2 == "c":
    print ("Correct!")  
    score += 1
elif answer2 =="" :
     print("Not sure?") 
elif answer2 != a and answer2 != "A" and answer2 != b and answer2 != "B" and answer2 != c and answer2 != "C" and answer2 != d and answer2 != "D":
  print("Wrong")
else:

    print("Wrong!")
print ("The correct answer is Japan")

answer3= input("What is the most spoken language?").lower()
if answer3 == "English".lower():
    print ("Correct!")  
    score += 1
elif answer3 =="" :
 print("Not sure?")  
else:
    print("Wrong!")
print ("The correct answer is English")

answer4= input("How deep is the ocean in meters?").lower()
if answer4 == "10,935 meters".lower():
    print ("Correct!") 
    score += 1
elif answer4 =="" :
 print("Not sure?")   
else:
    print("Wrong!")
print ("The correct answer is 10,935 meters")


#End the quiz

print("Thank you for playing, {}!. You got {} points".format(name, score ))
