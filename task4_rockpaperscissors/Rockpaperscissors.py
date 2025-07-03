import tkinter as tk
from tkinter import messagebox
import random


class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game 🎮")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f4c3")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 5
        self.current_round = 1
        self.history = []

        self.build_ui()

    def build_ui(self):
        tk.Label(
            self.root, text="Rock Paper Scissors Game ✊🖐️✌️",
            font=("Arial", 24, "bold"), bg="#689f38", fg="white", pady=10
        ).pack(fill=tk.X)

        self.round_label = tk.Label(
            self.root, text=f"Round: {self.current_round} / {self.rounds}",
            font=("Arial", 14, "bold"), bg="#f0f4c3"
        )
        self.round_label.pack(pady=10)

        score_frame = tk.Frame(self.root, bg="#f0f4c3")
        score_frame.pack(pady=5)

        self.user_score_label = tk.Label(
            score_frame, text=f"Your Score: {self.user_score}",
            font=("Arial", 14), bg="#f0f4c3"
        )
        self.user_score_label.grid(row=0, column=0, padx=20)

        self.computer_score_label = tk.Label(
            score_frame, text=f"Computer Score: {self.computer_score}",
            font=("Arial", 14), bg="#f0f4c3"
        )
        self.computer_score_label.grid(row=0, column=1, padx=20)

        # Choice Buttons
        btn_frame = tk.Frame(self.root, bg="#f0f4c3")
        btn_frame.pack(pady=20)

        rock_btn = tk.Button(
            btn_frame, text="✊ Rock", font=("Arial", 14, "bold"), width=12,
            bg="#42a5f5", fg="white", command=lambda: self.play("Rock")
        )
        rock_btn.grid(row=0, column=0, padx=10)

        paper_btn = tk.Button(
            btn_frame, text="🖐️ Paper", font=("Arial", 14, "bold"), width=12,
            bg="#ef5350", fg="white", command=lambda: self.play("Paper")
        )
        paper_btn.grid(row=0, column=1, padx=10)

        scissors_btn = tk.Button(
            btn_frame, text="✌️ Scissors", font=("Arial", 14, "bold"), width=12,
            bg="#66bb6a", fg="white", command=lambda: self.play("Scissors")
        )
        scissors_btn.grid(row=0, column=2, padx=10)

        # Result Label
        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 16, "bold"),
            bg="#f0f4c3", fg="black"
        )
        self.result_label.pack(pady=10)

        # History Label and Listbox
        tk.Label(
            self.root, text="Game History 📜",
            font=("Arial", 14, "bold"), bg="#f0f4c3"
        ).pack()

        self.history_box = tk.Listbox(
            self.root, width=60, height=6, font=("Arial", 12), bg="white"
        )
        self.history_box.pack(pady=5)

        # Reset Button
        reset_btn = tk.Button(
            self.root, text="🔄 Reset", width=15, font=("Arial", 12, "bold"),
            bg="#ff7043", fg="white", command=self.reset_game
        )
        reset_btn.pack(pady=10)

    # ---------------- Game Logic ----------------
    def play(self, user_choice):
        if self.current_round > self.rounds:
            messagebox.showinfo("Game Over", "Game is over. Please reset to play again.")
            return

        computer_choice = random.choice(self.choices)

        result = ""
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "Computer Wins!"
            self.computer_score += 1

        self.history.append(
            f"Round {self.current_round}: You ➡️ {user_choice}, Computer ➡️ {computer_choice} — {result}"
        )
        self.history_box.insert(tk.END, self.history[-1])

        self.result_label.config(text=result)
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

        self.current_round += 1
        if self.current_round <= self.rounds:
            self.round_label.config(text=f"Round: {self.current_round} / {self.rounds}")
        else:
            self.round_label.config(text="Game Over!")
            self.end_game_summary()

    def end_game_summary(self):
        if self.user_score > self.computer_score:
            summary = "🎉 You won the game!"
        elif self.user_score < self.computer_score:
            summary = "💻 Computer won the game!"
        else:
            summary = "🤝 It's a tie game!"
        messagebox.showinfo("Game Over", summary)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.current_round = 1
        self.history.clear()

        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        self.round_label.config(text=f"Round: {self.current_round} / {self.rounds}")
        self.result_label.config(text="")
        self.history_box.delete(0, tk.END)


# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()