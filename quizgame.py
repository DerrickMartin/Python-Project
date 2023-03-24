#Print Welcome Message
print("Welcome to my quiz game")

# First question
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

#First Question
answer = input("What animal is a mans best friend? ")
if answer.lower() == "dog":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
# Second Question
answer = input("How do you spell the color red? ")
if answer.lower() == "red":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Third Question
answer = input("What color is the sky? ")
if answer.lower() == "blue":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Fourth Question
answer = input("What anime has over 1000 episodes ")
if answer.lower() == "one piece":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Print the Score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")