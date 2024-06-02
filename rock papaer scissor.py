import tkinter as tk
import random
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
def create_heading(parent, text):
    """Create a styled heading label."""
    heading_label = tk.Label(parent, text=text, font=("Helvetica", 30, "bold"),fg="red")
    heading_label.pack(pady=20)  
    return heading_label
create_heading(root,'welcome to my game')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"


def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    result = determine_winner(user_choice, computer_choice)
    
  
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    
   
    if result == "You win!":
        user_score[0] += 1
    elif result == "You lose!":
        computer_score[0] += 1
    
    user_score_label.config(text=f"Your Score: {user_score[0]}")
    computer_score_label.config(text=f"Computer's Score: {computer_score[0]}")


def reset_game():
    user_score[0] = 0
    computer_score[0] = 0
    user_choice_label.config(text="Your Choice: -")
    computer_choice_label.config(text="Computer's Choice: -")
    result_label.config(text="")
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer's Score: 0")




user_score = [0]
computer_score = [0]


user_choice_label = tk.Label(root, text="Your Choice: -", font=("Helvetica", 20))
computer_choice_label = tk.Label(root, text="Computer's Choice: -", font=("Helvetica", 20))
result_label = tk.Label(root, text="", font=("Helvetica", 20))
user_score_label = tk.Label(root, text="Your Score: 0", font=("Helvetica", 20))
computer_score_label = tk.Label(root, text="Computer's Score: 0", font=("Helvetica", 20))

rock_button = tk.Button(root, text="Rock",font=16, command=lambda: play("rock"),bg="brown")
paper_button = tk.Button(root, text="Paper",font=16, command=lambda: play("paper"),bg="grey")
scissors_button = tk.Button(root, text="Scissors",font=16, command=lambda: play("scissors"),bg="blue")
reset_button = tk.Button(root, text="Reset Game",font=18, command=reset_game)


user_choice_label.pack()
computer_choice_label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()
reset_button.pack()
result_label.pack()
user_score_label.pack()
computer_score_label.pack()


root.mainloop()
