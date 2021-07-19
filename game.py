def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------------")
    print("RESULTS")
    print("---------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (y/n): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False
# -------------------------


questions = {
"What is my favourite color?: ": "A",
"What is my favourite smoothie?: ": "A",
"Which is NOT my favourite game?: ": "C",
"What is my favourite sport car?: ": "B"
}

options = [["A) White", "B) Red", "C) Yellow", "D) Blue"],
           ["A) Oreo Smoothie", "B) Milo Smoothie", "C) Strawberry Smoothie", "D) Banana Smoothie"],
           ["A) Roblox", "B) Minecraft", "C) Free Fire", "D) PUBG"],
           ["A) Bugatti", "B) Lamborghini", "C) Ferarri", "D) BMW"]]

new_game()

while play_again():
    new_game()

print("Byee")