import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = tk.Label(root, text="Your Choice: ", font=("Helvetica", 14))
        self.user_choice_label.pack(pady=10)

        self.computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Helvetica", 14))
        self.computer_choice_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: User 0 - 0 Computer", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)

        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")

        if winner == 'tie':
            self.result_label.config(text="It's a tie!", fg="blue")
        elif winner == 'user':
            self.result_label.config(text="You win!", fg="green")
            self.user_score += 1
        else:
            self.result_label.config(text="Computer wins!", fg="red")
            self.computer_score += 1

        self.score_label.config(text=f"Score: User {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_choice_label.config(text="Your Choice: ")
        self.computer_choice_label.config(text="Computer's Choice: ")
        self.result_label.config(text="")
        self.score_label.config(text="Score: User 0 - 0 Computer")


root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
