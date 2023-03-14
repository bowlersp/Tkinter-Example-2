from tkinter import *

##How to use padding and grid to maniuplate GUI properties

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="I am a label", font=("Arial", 18))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button

def button_clicked():
  print("I got clicked")
  new_text = input.get()
  my_label.config(text=new_text)
  
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me too!", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

