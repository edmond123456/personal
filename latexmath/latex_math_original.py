""" 
https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk3_entry_text.py
https://stackoverflow.com/questions/44443270/use-latex-symbols-in-sympy-expressions

 """

import tkinter as tk
import sympy as sym
import sympy.printing as printing

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
# e = tk.Entry(window, show="*")
#e = tk.Entry(window, show="1")
e = tk.Entry(window, bd=10)
e.pack()





def transform():
    var = e.get()
    string = sym.symbols(var)
    t.insert('insert', printing.latex(string))




b1 = tk.Button(window, text='transform', width=15,
              height=2, command=transform)
b1.pack()


t = tk.Text(window, height=3)
t.pack()

window.mainloop()
