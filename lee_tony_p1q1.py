# Quiz Creation Activity

import time
from rich import print
score_now = 0

# Question 1

print("What is 2 + 5")
ans = float(input())
if ans == 7:
    score_now = score_now + 1
    print("Correct!")
else:
    print("Incorrect ;=;")
    score_now = score_now
if score_now == 1:
    print(f"You got 1 question correct so far!")
else:
    print(f"You got {score_now} questions correct so far.")

# Question 2

print("What is the colour of the colour red?")
ans = input().lower()
if ans == "red":
    score_now = score_now + 1
    print("Correct!")
else:
    print("Incorrect ;=;")
    score_now = score_now
if score_now == 1:
    print("You got 1 question correct so far!")
else:
    print(f"You got {score_now} questions correct so far!")

# Question 3

print("What is 8 + 12?")
ans = float(input())
if ans == 20:
    print("Correct!")
    score_now = score_now + 1
else:
    print("Incorrect ;=;")
    score_now = score_now
if score_now == 1:
    print("You got 1 question correct so far!")
else:
    print(f"You got {score_now} questions correct so far!")

# Question 4

print("what is 20.9 - 7.2?")
ans = float(input())
if ans == 13.7:
    print("Correct!")
    score_now = score_now + 1
else:
    print("Incorrect ;=;")
    score_now = score_now
if score_now == 1:
    print("You got 1 question correct so far!")
else:
    print(f"You got {score_now} questions correct so far!")

# Question 5

print("""How many fingers does a normal human being have in total?
    A: 0
    B: 5
    C: 10""")
ans = input()
if ans == C:
    print("Correct!")
    score_now = score_now + 1
else:
    print("Incorrect ;=;")
if score_now == 1:
    print("You got 1 question correct so far!")
else:
    print(f"You got {score_now} questions correct so far!")

print("Congratulations! you have finished the quiz!")
print(f"You got {score_now} questions out of 5 questions correct and a percentage of {(score_now / 5) * 100}&!")


