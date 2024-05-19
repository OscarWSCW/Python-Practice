score = 0
play = "yes"
print("Hello")
import random

question_format = "{}\nA. {} B.{} C.{} D.{}"
good_comments = ["Way to go!", "Keep it up!", "Fantastic!"]
bad_comments = ["Keep trying!", "Maybe next time", "Don't give up"]
Questions = [
             ]
# Ask the user their name
name = input("What is your name? ")



#Greet the user and welcome them to the quiz
print("Welcome to this quiz, {}.".format(name))
print("This quiz is about the earth.")


#Check number of question attempts
while True:
 try:
     tries = input("How many attempts do you want at each question (1-2)? ")  
     tries = int(tries)
     break
 except:
    print ("That's not a number")


#Ask the user a question and tell the user to answer the question
while play == "yes":
   question_attemps1 = tries
   while question_attemps1 > 0:
        answer1 = input("What is the largest country by population? ").lower()
        if answer1 == "India".lower():
            print ("Correct!") 
            score += 1 
            print("You get one point")
            break
        elif answer1 =="" :
            print("You don't know? ")   
        else:
            print("Wrong!")

        question_attemps1 -=1
        print("The answer is India")

   question_attemps2 = tries
   while question_attemps2 > 0:
        answer2 = input("What is the greenest type of grass? ").lower()
        if answer2 == "Perennial ryegrass".lower():
            print ("Correct!") 
            score += 1
            print("You get one point")
            break
        elif answer2 =="" :
            print("You don't know? ")   
        else:
            print("Wrong!")
        question_attemps2 -=1
        print("The answer is Perennial ryegrass")

   question_attemps3 = tries
   while question_attemps3 > 0:
        answer3= "Which country snows the most?"
        q3a = "Canada"
        q3b = "Iceland"
        q3c = "Japan"
        q3d = "Norway"
        answer3 = input("{}\nA.{} B.{} C.{} D.{}".format(answer3, q3a, q3b, q3c, q3d)).lower()
        if answer3 == q3c.lower() or answer3 == "c":
            print ("Correct!")  
            score += 1
            print ("You get one point")
            break
        elif answer2 =="" :
            print("Not sure?") 
        elif answer2 != q3a and answer2 != "A" and answer2 != q3b and answer2 != "B" and answer2 != q3c and answer2 != "C" and answer2 != q3d and answer2 != "D":
            print("Wrong")
            print ("The answer is Japan")
        else:
            print("Wrong!")
            print ("The answer is Japan")
        question_attemps3 -=1

   question_attemps4 = tries
   while question_attemps4 > 0:
        answer4 = input("What is the most spoken language? ").lower()
        if answer4 == "English".lower():
            print ("Correct!")  
            score += 1
            print ("You get one point")
            break
        elif answer4 =="" :
            print("Not sure?")
        else:
            print("Wrong!")
            print ("The answer is English")
            question_attemps4 -=1

   question_attemps5 = tries
   while question_attemps5 > 0:
        answer5 = input("How deep is the ocean in meters? ").lower()
        if answer5 == "10,935 meters".lower():
            print ("Correct!") 
            score += 1
            print ("You get one point")
            break
        elif answer5 =="" :
            print("Not sure?")  
        else:
            print("Wrong!")
            print ("The answer is 10,935 meters")
        question_attemps5 -=1
    

            #End the quiz
        print("Thank you for playing, {}!. You got {} points".format(name, score ))

            #Replay

        play = input("Do you want to play again? ").lower()
