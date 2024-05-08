from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import font as tkFont
import tkinter as tk
import random

window = Tk()
#think about hexadecimal color options, can be anything
window.configure(background = '#FF00FF') #current color is magenta
window.geometry("500x500")
window.title("Rps")

custom_font = tkFont.Font(family="Arial", size=30)


titleLabel = Label(window, text="ROCK PAPER SCISSCORS", font=custom_font, padx=10, pady=10)
titleLabel.pack(side='top', anchor='center')

quitButton = Button(window, text="Quit", command=window.destroy)
quitButton.place(x=240,y=300)
displayText = "Click a button to start"

def show():
    

    name = askstring("Start", "Enter you name")
    window.destroy()
    mainWindow = Tk()
    mainWindow.configure(background = '#FF00FF') #current color is magenta
    mainWindow.geometry("500x500")
    mainWindow.title("Rps")

    custom_font = tkFont.Font(family="Arial", size=20)


    nameLabel = Label(mainWindow, text=name, font=custom_font, padx=10, pady=10)
   
    # Calculate the center position with offset
    center_x = 0.5 * 500  # Half of window width
    center_y = 0.5 * 500  # Half of window height
    offset_x = 50  # Offset to the right
    offset_y = -80  # Offset downward

    # Place the name label at the calculated position
    nameLabel.place(x=center_x + offset_x - nameLabel.winfo_reqwidth() / 2,
                     y=center_y + offset_y - nameLabel.winfo_reqheight() / 2)
    
    robotLabel = Label(mainWindow, text="GPT", font=custom_font, padx=10, pady=10)
   
    # Calculate the center position with offset
    center_x = 0.5 * 500  # Half of window width
    center_y = 0.5 * 500  # Half of window height
    offset_x = -50  # Offset to the right
    offset_y = -80  # Offset downward

    # Place the name label at the calculated position
    robotLabel.place(x=center_x + offset_x - robotLabel.winfo_reqwidth() / 2,
                     y=center_y + offset_y - robotLabel.winfo_reqheight() / 2)
    
    humanScore = 0
    botScore = 0
    def simulateGame(choice, humanScore, botScore, humanLabel, botLabel):
        list1 = [1, 2, 3]
        randomChoice = random.choice(list1)
        #Ties situation, Human Winning, Bot Winning
        
        if (choice == 1 & randomChoice == 1) or (choice == 2 & randomChoice == 2) or (choice == 3 & randomChoice == 3):
            displayText = "Tie!"
            displayLabel.config(text = displayText)

        #This is the case of human winning
        elif (choice == 1 and randomChoice == 3) or (choice == 2 and randomChoice == 1) or (choice == 3 and randomChoice == 2)  :
            displayText = "You win!"
            humanScore += 1
            humanLabel.config(text = str(humanScore))
            displayLabel.config(text = displayText)


        #score is probably 3    
        else:
            displayText = "You lose!"
            botScore += 1
            botLabel.config(text = str(botScore))
            displayLabel.config(text = displayText)



        #wait, you want to announce the score of the winner and loser?
        if (humanScore == 3) or (botScore == 3):
            game_over_window = Tk()
            game_over_window.configure(background = '#FF00FF') #current color is magenta
            game_over_window.geometry("500x500")
            game_over_window.title("Rps")
            game_over_window.destroy()
            mainWindow.destroy()
            

    humanLabel = Label(mainWindow, text=str(humanScore))
    humanLabel.place(x=300,y=150)

    botLabel = Label(mainWindow, text=str(botScore))
    botLabel.place(x=200,y=190)

    displayLabel = Label(mainWindow, text=displayText)
    displayLabel.place(x=300,y=50)

    rockButton = Button(mainWindow, text="Rock", command=simulateGame(1, humanScore, botScore, humanLabel, botLabel))
    rockButton.place(x=50,y=300)

    paperButton = Button(mainWindow, text="Paper", command=simulateGame(2, humanScore, botScore, humanLabel, botLabel))
    paperButton.place(x=175,y=300)

    scisscorsButton = Button(mainWindow, text="Scisscors", command=simulateGame(3, humanScore, botScore, humanLabel, botLabel))
    scisscorsButton.place(x=300,y=300)

    mainWindow.mainloop()
   
B = Button(window, text ="Start", command = show)
B.place(x=240,y=250)

window.mainloop()
