print("Welcome to Git Version Control quiz!")

playing = input("Would you like to play?(type Y/N) ")

if (playing.lower().strip() != 'y'):
    print("Game shut down")
    quit()

print("Let's play! :)")

# Score board
score = 0

# Question 1
answer1 = input("What is the word you prefix to every Git command?: ")

if (answer1.lower().strip() == "git"):
    score += 1
    print('Good job! Your score is:', score)
else: 
    print("Uh oh incorrect! Your score is:",  )

# Question 2
answer2 = input("How do you add files with git?: ")

if (answer2.lower().strip() == "git add"):
    score += 1
    print('Good job! Your score is:', score)
else: 
    print("Uh oh incorrect!")

# Question 3
answer3 = input("What is the command for commiting changes?: ")

if (answer3.lower().strip() == "git commit"):
    score += 1
    print('Good job! Your score is:', score)
else: 
    print("Uh oh incorrect!")

# Question 4
answer4 = input("What command do you use to send your changes to GitHub?: ")

if (answer4.lower().strip() == "git push"):
    score += 1
    print('Good job! Your score is:', score)
else: 
    print("Uh oh incorrect!")


if (score == 4):
    print("Thank you for playing! You got all the questions corret, amazing job!")
elif (score == 0):
    print("Maybe you should head back to the documentation...")
else:
    print("Thank you for playing! You got", score, "questions correct, not bad!")