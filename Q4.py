# Quiz Application

score = 0

print("Welcome to the Quiz!\n")

answer = input("1. What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Delhi.")

answer = input("\n2. Which language is used for AI and ML? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Python.")

answer = input("\n3. How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is 7.")

print("\nQuiz Completed!")
print("Your Score:", score, "/3")