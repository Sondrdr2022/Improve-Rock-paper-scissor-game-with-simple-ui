import random
import tkinter as tk
#Setting up parameters to hold the score for the game
player_win = 0
bot_win = 0
draw = 0
#Define function to randomly choose between rock,paper,scissor
def game():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(x, y):
    #"global"function to access the created parameter from outside of the define function
    global player_win, bot_win, draw
    if x == y:
        draw +=1
        return "It's a tie!"
    elif (x == "Rock" and y == "Scissors") or (x == "Scissors" and y == "Paper") or (x == "Paper" and y == "Rock"):
        player_win +=1
        return "You win!"
    #Close the applicant if the player choose to close the app
    elif (x == "Exit"):
        window.quit()
    else:
        bot_win +=1
        return "Computer wins!"


# UI setup
def play_game(x):
    y = game()
    result = determine_winner(x, y)
    result_label.config(text=f"Computer chose: {y}\nResult: {result}\nplayer win: {player_win}, bot win: {bot_win}, draw: {draw}")

# Initialize main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("300x300")

# Display title
title_label = tk.Label(window, text="Choose Rock, Paper, or Scissors!", font=("Arial", 14))
title_label.pack(pady=10)

# Buttons for player choices
rock_button = tk.Button(window, text="Rock", width=10, command=lambda: play_game("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=10, command=lambda: play_game("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=10, command=lambda: play_game("Scissors"))
scissors_button.pack(pady=5)
# This button isn't very useful since there's a close button already but since the code version have the option to choose to quit
#or to continue the game so i added this in
rock_button = tk.Button(window, text="Exit", width=10, command=lambda: play_game("Exit"))
rock_button.pack(pady=5)

# Label to display result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run the application
window.mainloop()
