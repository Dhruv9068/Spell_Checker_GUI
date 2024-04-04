
import tkinter
from tkinter import *
from textblob import TextBlob
def Check_spelling():
    word= entry_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root, text="Correct Text IS: ",font=("Sacramento", 20), bg = "#9DF1DF", fg = "#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)
root= Tk()
root.title("Spelling checker")
root.geometry('700x400')
root.config(background = "#9DF1DF")
heading= Label(root,text="Spelling Checker",font=("sangnimito",30,"bold"),bg="#9DF1DF",fg="black")
heading.pack(pady=(50,0))

entry_text= Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)
entry_text.pack(pady=10)
entry_text.focus()
button=Button(root,text="Check",font=("Ariel",20,"bold"),fg="red",bg="#F7C8E0", command =Check_spelling)
button.pack()






spell = Label(root, font=("poppins", 20), bg = "#9DF1DF", fg = "#364971")

spell.place(x=350,y=250)






mainloop()