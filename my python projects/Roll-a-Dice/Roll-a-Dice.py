import tkinter as tk       #here we are importing the tkinter which is a standard GUI library for python used for crating Graphic User Interface .
from PIL import Image , ImageTk        # we are using Pillow library which is an imaging library .
import random

window = tk.Tk()
window.geometry("1000x720")
window.title("Roll-a-Dice: Your Virtual dice Rolling Companion")



dice= ["D1.png","D2.png","D3.png","D4.png","D5.png","D6.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image = image1)
label2 = tk.Label(window, image = image2)


label1.image=image1
label2.image=image2

label1.place(x=20 , y=200)
label2.place(x=570,y=200)

#givng the command to the ROLL button

def dice_roll():
    image1= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1

    image2= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2

button = tk.Button(window, text='ROLL' , bg='green', fg='yellow', font="Times 20 bold", command=dice_roll)
button.place(x=450 , y=0)

window.mainloop()
