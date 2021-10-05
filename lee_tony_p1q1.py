# Quiz Creation Activity

# The user will talk a quiz
#
import time
from rich import print
score_now = 0

print("What is 2 + 5")
ans = float(input())
if ans == 7:
    score_now = score_now + 1
    print("Correct!")
    print(f"You got {score_now}/1 questions correct so far")
    score_now = score_now + 1
else:
    print("Incorrect ;=;")
    print("You got {score_now}/1 questions correct so far")
    score_now = score_now
print("What is the colour of the colour red?")
ans = input()
if ans == "red":
    score_now = score_now + 1
    print("Correct!")
    print(f"You got {score_now}/2 questions correct so far")
else:
    print("Incorrect ;=;")
    print(f"You got {score_now}/2 questions correct so far")
    score_now = score_now

# Math Question
print("What is 98 + 7")
ans = float(input())
if ans == 105:
    print("Correct!")

else:
    print("Incorrect ;=;")
    score = score
print(score)
