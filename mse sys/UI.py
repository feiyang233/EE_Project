
from tkinter import *

master = Tk()
master.title('Welcome')
master.geometry('450x400')


var = StringVar(master)
var.set("one") # initial value
L=["one", "two", "three", "four"]
option = OptionMenu(master, var, *L)
option.pack(side='bottom')

#
# test stuff

def ok():
    print ("value is", var.get())
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()

#The following example shows how to create an option menu from a list of options:
'''


from tkinter import *

# the constructor syntax is:
# OptionMenu(master, variable, *values)

OPTIONS = [
    "egg",
    "bunny",
    "chicken"
]

master = Tk()
master.title('Welcome')
master.geometry('450x400')
variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w =OptionMenu(*(master, variable)+tuple(OPTIONS))
w.pack()

mainloop()
'''