import tkinter as tk
import random

class Game():
    def __init__(self):
        self.possible_actions = ["rock", "paper", "scissors"]
        self.user_action = None
        self.computer_action = None
        
    def user(self, action):
        self.user_action = action
        
    def comp(self):
        self.computer_action = random.choice(self.possible_actions)
        
    def tie(self):
        if self.computer_action == self.user_action:
            return f"Both players selected {self.user_action}. It's a tie!"
        
    def win(self):
        if (self.user_action == "rock" and self.computer_action == "scissors") or (self.user_action == "paper" and self.computer_action == "rock") or (self.user_action == "scissors" and self.computer_action == "paper"):
            return f"{self.user_action.capitalize()} smashes {self.computer_action}. You win! Wow! Cool! Awesome!"
        
    def lose(self):
        if (self.user_action == "rock" and self.computer_action == "paper") or (self.user_action == "paper" and self.computer_action == "scissors") or (self.user_action == "scissors" and self.computer_action == "rock"):
            return f"{self.computer_action.capitalize()} covers {self.user_action}. You lose. ha ha ha "

class Rock(Game):
    def __init__(self):
        super().__init__()
        self.user_action = "rock"
        
class Paper(Game):
    def __init__(self):
        super().__init__()
        self.user_action = "paper"
    
class Scissors(Game):
    def __init__(self):
        super().__init__()
        self.user_action = "scissors"
        
def play_game(user_choice, result_label, user_image_label, computer_image_label):
    game = None
    
    if user_choice == "rock":
        game = Rock()
        user_image_label.config(image=us_r_img)
    elif user_choice == "paper":
        game = Paper()
        user_image_label.config(image=us_p_img)
    elif user_choice == "scissors":
        game = Scissors()
        user_image_label.config(image=us_s_img)
    
    game.comp()
    
    if game.computer_action == "rock":
        computer_image_label.config(image=com_r_img)
    elif game.computer_action == "paper":
        computer_image_label.config(image=com_p_img)
    elif game.computer_action == "scissors":
        computer_image_label.config(image=com_s_img)
    
    result = None
    
    if game.tie():
        result = game.tie()
    elif game.win():
        result = game.win()
    elif game.lose():
        result = game.lose()
    
    result_label.config(text=result)

# граa интерфейс
win = tk.Tk()
win.configure()
win.geometry("600x600")
win.title('Rock Paper Scissors')

result_label = tk.Label(win, text="", font=("Helvetica", 16))
result_label.place(x=50, y=270)

start_label = tk.Label(win, text="Rock Paper Scissors", font=("Helvetica", 16))
start_label.pack(pady=20)

u_label = tk.Label(win, text="You:", font=("Helvetica", 16))
u_label.place(x=100, y=60)

me_label = tk.Label(win, text="Me:", font=("Helvetica", 16))
me_label.place(x=440, y=60)

g_img = tk.PhotoImage(file='lose1.png')
g_img = g_img.subsample(3,3)
girl_label = tk.Label(win, image=g_img, font=("Helvetica", 16))
girl_label.place(x=25, y=485)

b_img = tk.PhotoImage(file='win.png')
b_img = b_img.subsample(3,3)
b_label = tk.Label(win, image=b_img, font=("Helvetica", 16))
b_label.place(x=500, y=490)


com_r_img = tk.PhotoImage(file='r1.png')
com_p_img = tk.PhotoImage(file='p1.png')
com_s_img = tk.PhotoImage(file='s1.png')

user_image_label = tk.Label(win, image=None)
user_image_label.place(x=80, y=90)

computer_image_label = tk.Label(win, image=None)
computer_image_label.place(x=320, y=90)


us_r_img = tk.PhotoImage(file='r.png')
rock_button = tk.Button(win, image=us_r_img, bd=0, highlightthickness=0, command=lambda: play_game("rock", result_label, user_image_label, computer_image_label))
rock_button.place(x=40, y=330)

us_p_img = tk.PhotoImage(file='p.png')
paper_button = tk.Button(win, image=us_p_img, bd=0, highlightthickness=0, command=lambda: play_game("paper", result_label, user_image_label, computer_image_label))
paper_button.place(x=200, y=330)

us_s_img = tk.PhotoImage(file='s.png')
scissors_button = tk.Button(win, image=us_s_img, bd=0, highlightthickness=0, command=lambda: play_game("scissors", result_label, user_image_label, computer_image_label))
scissors_button.place(x=380, y=330)

win.mainloop()                                        
                         