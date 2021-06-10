from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="This is new text")
my_label.pack()

#Buttons
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()



window.mainloop()