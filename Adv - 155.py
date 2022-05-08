from tkinter import *
root=Tk()
root.title("Dictonary")
root.geometry("600x400")
root.configure(background = 'yellow')

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)


dictonary = {'Mutable': 'Values can be changed just like a list',
             'Immutable': 'Values can not be changed just like a tuple',
             'Tkinter': 'It is the GUI library of python'}

def mutable():
    label_of_mutable["text"] = dictonary['Mutable']
    
def immutable():
    label_of_immutable["text"] = dictonary["Immutable"]
    
def tkinter():
    label_of_tkinter["text"] = dictonary['Tkinter']
    
button_mutable = Button(root , text = "Meaning of Mutable", command = mutable)
button_mutable.place(relx = 0.5, rely = 0.2, anchor = CENTER)

label_of_mutable.place(relx = 0.5, rely = 0.3, anchor = CENTER)

button_immutable = Button(root , text = "Meaning of Immutable", command = immutable)
button_immutable.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_of_immutable.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button_tkinter = Button(root, text = "Meaning of Tkinter", command = tkinter)
button_tkinter.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label_of_tkinter.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()