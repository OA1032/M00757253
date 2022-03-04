import tkinter as tk

window = tk.Tk()
window.title('Tkinter hello world')

'''text = tk.Label(text = "What's your name?", foreground = 'white', background = 'blue', width = 30, height = 3)

text.pack()

entry = tk.Entry(width = 30)
entry.pack()

name = entry.get()#Denisk
entry.delete(0,tk.END)

def save_and_print():
    name = entry.get()
    entry.delete(0,tk.END)
    print (name)

button = tk.Button(text = 'Submit',width = 30, height = 5, command = save_and_print)
#button.pack(padx = 5, pady = 5)

window.bind('<Return>', lambda event: save_and_print())

frame = tk.Frame(master = window)
label = tk.Lable(master = frame, text = 'Frame!')

frame.columconfigure(0, weight = 1)
frame.columconfigure(1, weight = 3)

text.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'n')
entry.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = 's')
button.grid(column = 1, row = 0, padx = 5, pady = 5, sticky = 'se')
label.grid(column = 1, row = 1, padx = 5, pady = 5, sticky = 'nsew')

frame1 = tk.Frame(width = 100, height = 100, bg = 'green')
frame2 = tk.Frame(width = 20, height = 20, bg = 'red')
frame3 = tk.Frame(width = 50, height = 50, bg = 'blue')

frame1.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
frame2.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
frame3.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)'''
for i in range(3):
    window.columnconfigure(i, weight = i + 1,minsize = 75)
    window.rowconfigure(i, weight = i + 1,minsize = 75)
for row in range(3):
    for col in range(3):
        frame = tk.Frame(master = window, relied = tk.RAISED,borderwidth = 1)
        frame.grid(row=row,colum = col, padx = 5, pady = 5)
        label = tk.LABEL(master = frame, text = f'(i), (j)')
        label.pack()

window.mainloop()