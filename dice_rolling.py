import random as rand
import tkinter as tk
import data_dice as dd

class DiceRoller:
    def __init__(self):
        # Screen settings
        self.screen = tk.Tk()
        self.screen.geometry('1280x780')
        self.screen.title('Dice Roller Simulator')

        # Title
        self.title = tk.Label(self.screen, text='Roll the Dice!', font=('Arial', 40))
        self.title.pack(pady=10)

        # Roll button
        self.roll_button = tk.Button(self.screen, text='ROLL', font=('Arial', 40), command=self.roll)
        self.roll_button.place(x=550, y=500)

        # Dice display
        self.dice_display = tk.Label(self.screen, text='', font=('Arial', 40))
        self.dice_display.place(x=550, y=150)

    def roll(self):
        number = rand.randint(1, 6)
        print(number)

        match number:
            case 1:
                self.dice_display.config(text=dd.dice_parts[0] + '\n' + dd.dice_parts[1] + '\n' + dd.dice_parts[3] + '\n' + dd.dice_parts[1] + '\n' + dd.dice_parts[0])
            case 2:
                self.dice_display.config(text=dd.dice_parts[0] + '\n' + dd.dice_parts[1] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[1] + '\n' + dd.dice_parts[0])
            case 3:
                self.dice_display.config(text=dd.dice_parts[0] + '\n' + dd.dice_parts[2] + '\n' + dd.dice_parts[3] + '\n' + dd.dice_parts[4] + '\n' + dd.dice_parts[0])
            case 4:
                self.dice_display.config(text=dd.dice_parts[0] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[1] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[0])
            case 5:
                self.dice_display.config(text=dd.dice_parts[0] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[3] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[0])
            case 6:
                self.dice_display.config(text=dd.dice_parts[0] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[5] + '\n' + dd.dice_parts[0])


DiceRoller().screen.mainloop()
