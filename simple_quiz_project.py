list = []
score = 0
print("Welcome, to Github quiz")
perm = input("Would you like to play the quiz? ").lower()
if (perm != "yes"):
    quit()
print("Thank you, for participating the quiz")

ques1 = input("1. What is the parent company of GitHub? ").lower()
if (ques1 == "microsoft"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("1")

ques2 = input("2. What is the default branch name in a newly created GitHub repository? ").lower()
if (ques2 == "main"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("2")

ques3 = input("3. What command do you use to clone a GitHub repository to your local machine? ").lower()
if (ques3 == "git clone"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("3")

ques4 = input("4. What is the primary programming language used to develop GitHub? ").lower()
if (ques4 == "ruby"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("4")

ques5 = input("5. What is the maximum file size for a single file in a GitHub repository?(eg. 5 kb) ").lower()
if (ques5 == "100 MB"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("5")

ques6 = input("6. Which GitHub feature allows you to track tasks, bugs, or feature requests? ").lower()
if (ques6 == "issues"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("6")

ques7 = input("7. What does the 'fork' operation in GitHub do? ").lower()
if (ques7 == "create copy"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("7")

ques8 = input("8. What command is used to push changes from a local repository to GitHub? ").lower()
if (ques8 == "git push"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("8")

ques9 = input("9. What is the name of GitHub's visual code editor? ").lower()
if (ques9 == "github codespaces"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("9")

ques10 = input("10. What is the GitHub feature that lets you automate tasks based on repository events? ").lower()
if (ques10 == "github actions"):
    print("You're correct!")
    score+=1
else:
    print("Wrong anawer!")
    list.append("10")


print(f"Congratulations, You Scored: {score}")
print(f"Wrong answers in: {list}")

