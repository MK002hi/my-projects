from tkinter import *
import random

you_won = 0
computer_won = 0
draw = 0
choices = ["rock", "paper", "scissors"]

def show_frame(frame):
    frame.tkraise()

def start_game():
    show_frame(page2)

def no_game():
    show_frame(page4)

def play_game(user_choice):
    global you_won, computer_won, draw
    computer_choice = random.choice(choices)

    user_label.config(text=f"Your Choice: {user_choice.capitalize()}")
    computer_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Draw!", fg="blue")
        draw += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You Win!", fg="green")
        you_won += 1
    else:
        result_label.config(text="Computer Wins!", fg="red")
        computer_won += 1

def show_scores():
    score_label.config(text=f"You won: {you_won} \nComputer won: {computer_won} \nNo. of draws: {draw}")

    if you_won > computer_won:
        winner_label.config(text="You are the winner! 🎉", fg="green")
    elif you_won < computer_won:
        winner_label.config(text="Computer is the winner. \nBetter luck next time. 😊", fg="red")
    else:
        winner_label.config(text="It's a draw. 😊", fg="blue")

    show_frame(page5)

def exit_program():
    root.destroy()

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x600")
root.resizable(False, False)

page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)
page4 = Frame(root)
page5 = Frame(root)

for frame in (page1, page2, page3, page4, page5):
    frame.grid(row=0, column=0, sticky="nsew")

Label(page1, text="Do you want to play this game?", font=("Arial", 32)).pack(pady=30)
Button(page1, text="Yes ✅", font=("Arial", 24), width=10, bg="darkblue", fg="white", command=start_game).pack(pady=10)
Button(page1, text="No ❌", font=("Arial", 24), width=10, bg="orange", fg="white", command=no_game).pack(pady=10)

Label(page2, text="Let's start!", font=("Arial", 32)).pack(pady=30)
Label(page2, text="Choose 'rock', 'paper', or 'scissors' in each round\n\nClick 'Exit' to finish the game", font=("Arial", 24)).pack(pady=20)
Button(page2, text="Okay", font=("Arial", 24), bg="darkblue", fg="white", command=lambda: show_frame(page3)).pack(pady=10)

Label(page3, text="Rock Paper Scissors Game", font=("Arial", 32, "bold")).pack(pady=10)
Label(page3, text="Make your choice:", font=("Arial", 24)).pack(pady=5)

button_frame = Frame(page3)
button_frame.pack(pady=10)

Button(button_frame, text="Rock 🪨", font=("Arial", 24), width=10, bg="grey", command=lambda: play_game("rock")).grid(row=0,column=0,padx=5)
Button(button_frame, text="Paper 📄", font=("Arial", 24), width=10, bg="lightblue", command=lambda: play_game("paper")).grid(row=0,column=1,padx=5)
Button(button_frame, text="Scissors ✂️", font=("Arial", 24), width=10, bg="green", command=lambda: play_game("scissors")).grid(row=0, column=2, padx=5)

user_label = Label(page3, text="Your Choice: None", font=("Arial", 24))
user_label.pack(pady=5)
computer_label = Label(page3, text="Computer's Choice: None", font=("Arial", 24))
computer_label.pack(pady=5)

result_label = Label(page3, text="", font=("Arial", 28, "bold"))
result_label.pack(pady=10)

Button(page3, text="Exit", font=("Arial", 24), bg="red", fg="white", command=show_scores).pack(pady=10)

Label(page4, text="Okay 😊", font=("Arial", 32)).pack(pady=30)
Button(page4, text="Exit", font=("Arial", 24), bg="darkblue", fg="white", command=exit_program).pack(pady=10)

score_label = Label(page5, text="", font=("Arial", 28))
score_label.pack(pady=20)

winner_label = Label(page5, text="", font=("Arial", 28, "bold"))
winner_label.pack(pady=10)

Button(page5, text="Okay", font=("Arial", 24), bg="darkblue", fg="white", command=exit_program).pack(pady=20)

show_frame(page1)

root.mainloop()








