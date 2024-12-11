from tkinter import *
import pyttsx3
from tkinter import messagebox

engine = pyttsx3.init()

def playText():
  text = textEntry.get()
  if not text:
    messagebox.showwarning(title= "Warning", message = "Please enter some text!")
  else:
    engine.say(text)
    engine.runAndWait()

def clearText():
  textEntry.delete(0, END)

root = Tk()
root.title("Text to Speech")
root.geometry("500x300")

label = Label(root, text="Text to Speech", font=('arial', 20))
label.pack(pady=10)

text = Label(root, text="Enter Your Text", font=('arial', 12), fg='grey')
text.pack()

textEntry = Entry(root, font=(12), width=30)
textEntry.pack(pady=10)

frame = Frame(root)
frame.pack(pady=20)

playButton = Button(frame, text="Play", bg="green", fg="white", font=("Arial", 12), width=10, command=playText)
playButton.grid(row=0, column=0, padx=10)

setButton = Button(frame, text="Set", bg="blue", fg="white", font=("Arial", 12), width=10, command=clearText)
setButton.grid(row=0, column=1, padx=10)

exitButton = Button(frame, text="Exit", bg="red", fg="white", font=("Arial", 12), width=10, command=exit)
exitButton.grid(row=0, column=2, padx=10)

root.mainloop()