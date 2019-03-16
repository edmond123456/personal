""" 
https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk3_entry_text.py
https://stackoverflow.com/questions/44443270/use-latex-symbols-in-sympy-expressions

 """

import tkinter as tk
import sympy as sym
import sympy.printing as printing
import wolframalpha 

app_id = "VKAVEK-RKGXQHL64W"
client = wolframalpha.Client(app_id)

window = tk.Tk()
window.title('my window')
window.geometry('1000x200')
e = tk.Entry(window, bd=10,width=500)
e.pack()





def ans():
    var = e.get()
    res = client.query(var)
    answer = next(res.results).text 
    a = str(answer)
    t.insert('insert',a)




b1 = tk.Button(window, text='query', width=15,
              height=2, command=ans)
b1.pack()


t = tk.Text(window, height=3)
t.pack()

window.mainloop()
