import tkinter as tk
import Flags
'''
class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        text = tk.Text(self, wrap="none")
        vsb = tk.Scrollbar(orient="vertical", command=text.yview)
        text.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        text.pack(fill="both", expand=True)

        for i in range(20):
            b = tk.Button(self, text="Button #%s" % i)
            text.window_create("end", window=b)
            text.insert("end", "\n")

        text.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
    
    
# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window
root = Tk()
  
# Creating button. In this destroy method is passed
# as command, so as soon as button 1 is pressed root
# window will be destroyed
btn1 = Button(root, text ="Button 1", command = root.destroy)
btn1.pack(pady = 10)
  
# Creating button. In this destroy method is passed
# as command, so as soon as button 2 is pressed
# button 1 will be destroyed
btn2 = Button(root, text ="Button 2", command = btn1.destroy)
btn2.pack(pady = 10)
  
end = Button(root, text ="End", command = root.destroy)
end.pack(pady = 10)

# infinite loop
mainloop()

'''
# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

root = Tk()

'''
# function to be called when
# keyboard buttons are pressed
def key_press(event):
    key = event.char
    print(key, 'is pressed')
 
# creates tkinter window or root window
root = Tk()
root.geometry('200x100')
'''
'''
# here we are binding keyboard
# with the main window
root.bind('<Key>', key_press)
 
mainloop()
'''
'''
def hello():
    print("hello")

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter name here: ")

def myClick():
    myLabel = Label(root, text = "Hello " + e.get())
    myLabel.pack() #packs what is put onto screen as label

myButton = Button(root, text = "Animation 1" , command = an1).pack()
myButton2 = Button(root, text = "Animation 2" , command = an2).pack()
myButton3 = Button(root, text = "Animation 3" , command = an3).pack()
myButton4 = Button(root, text = "Animation 4" , command = an4).pack()
myButton5 = Button(root, text = "Animation 5" , command = an5).pack()
myButton6 = Button(root, text = "Animation 6" , command = an6).pack()
myButton7 = Button(root, text = "Animation 7" , command = an7).pack()
myButton8 = Button(root, text = "Animation 8" , command = an8,state=DISABLED).pack()
myButton9 = Button(root, text = "Animation 9" , command = an9).pack()
myButton10 = Button(root, text = "Animation 10" , command = an10).pack()
myButton11 = Button(root, text = "Animation 11" , command = hello,state=DISABLED).pack()


root.mainloop()
'''
'''
from tkinter import *   

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Button Background Example')
  
button = Button(tkWindow, text = 'Submit', bg='black', fg='white')  
button.pack()  
  
tkWindow.mainloop()
'''

from tkinter import *   

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')
  
button = Button(tkWindow, text = 'Submit', bg='#ffffff', activebackground='#00ff00')  
button.pack()  
  
tkWindow.mainloop()