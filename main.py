score = 0
print("hello")
# Ask the user their name
input("What is your name?")
#Greet the user and welcome them to the quiz
print("Welcome to this quiz.") 
print("This quiz is about the earth")
#Ask the user a question and tell the user to answer the question

answer= input("What is the largest country by population?")
if answer == "India":
    print ("Correct!") 
    score += 1
elif answer =="" :
    print("Not sure?")   
else:
    print("Wrong!")
    print("The correct answer is India")

answer1 = input("What is the greenest type of grass?")
if answer1 == "Perennial ryegrass":
    print ("Correct!")   
elif answer1 =="" :
 print("Not sure?")

else:
    print("Wrong!")
    print("The correct answer is Perennial ryegrass")

answer2= input("Which country snows the most?")
if answer2 == "Japan":
    print ("Correct!")  
    score += 1
elif answer2 =="" :
     print("Not sure?")  
else:
    print("Wrong!")
print ("The correct answer is Japan")

answer3= input("What is the most spoken language?")
if answer3 == "English":
    print ("Correct!")  
    score += 1
elif answer3 =="" :
 print("Not sure?")  
else:
    print("Wrong!")
print ("The correct answer is English")

answer4= input("How deep is the ocean?")
if answer4 == "10,935 meters":
    print ("Correct!") 
    score += 1
elif answer4 =="" :
 print("Not sure?")   
else:
    print("Wrong!")
print ("The correct answer is 10,935 meters")


#End the quiz

print("Thank you for playing!. You got ",score, "points" )
