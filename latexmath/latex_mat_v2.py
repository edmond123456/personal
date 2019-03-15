
""" https://stackoverflow.com/questions/36636185/is-it-possible-for-python-to-display-latex-in-real-time-in-a-text-box """

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

from Tkinter import *
from ttk import *

def graph(text):
    tmptext = entry.get()
    tmptext = "$"+tmptext+"$"

    ax.clear()
    ax.text(0.2, 0.6, tmptext, fontsize = 50)  
    canvas.draw()


root = Tk()

mainframe = Frame(root)
mainframe.pack()

text = StringVar()
entry = Entry(mainframe, width=100, textvariable=text)
entry.pack()

label = Label(mainframe)
label.pack()

fig = matplotlib.figure.Figure(figsize=(4, 2), dpi=200)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


#Greek
def alpha(): 
    entry.insert('insert', 'α')
def Beta(): 
    entry.insert('insert', 'β')
def Gamma(): 
    entry.insert('insert', 'γ')
def Delta(): 
    entry.insert('insert', 'δ')
def Epsilon(): 
    entry.insert('insert', 'ε')
def Theta(): 
    entry.insert('insert', 'θ')
def Kappa(): 
    entry.insert('insert', 'κ')
def Lambda(): 
    entry.insert('insert', 'λ')
def Mu(): 
    entry.insert('insert', 'μ')
def Xi(): 
    entry.insert('insert', 'ξ')
def Pi(): 
    entry.insert('insert', 'π')
def Rho(): 
    entry.insert('insert', 'ρ')
def Sigma(): 
    entry.insert('insert', 'σ')
def Tau(): 
    entry.insert('insert', 'τ')
def Phi(): 
    entry.insert('insert', 'φ')
def Chi(): 
    entry.insert('insert', 'χ')
def Psi(): 
    entry.insert('insert', 'ψ')
def Omega(): 
    entry.insert('insert', 'ω')

wid=30
hei=30
# Greek
btn_alpha = Button(root,text = 'α',command = alpha)
btn_alpha.place(x = 0,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'β',command = Beta)
btn_alpha.place(x = 0+wid*1,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'γ',command = Gamma)
btn_alpha.place(x = 0+wid*2,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'δ',command = Delta)
btn_alpha.place(x = 0+wid*3,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'ε',command = Epsilon)
btn_alpha.place(x = 0+wid*4,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'θ',command = Theta)
btn_alpha.place(x = 0+wid*5,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'κ',command = Kappa)
btn_alpha.place(x = 0+wid*6,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'λ',command = Lambda)
btn_alpha.place(x = 0+wid*7,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'μ',command = Mu)
btn_alpha.place(x = 0+wid*8,y = 350,width = wid,height = hei)
btn_alpha = Button(root,text = 'ξ',command = Xi)
btn_alpha.place(x = 0+wid*0,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'π',command = Pi)
btn_alpha.place(x = 0+wid*1,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'ρ',command = Rho)
btn_alpha.place(x = 0+wid*2,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'σ',command = Sigma)
btn_alpha.place(x = 0+wid*3,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'τ',command = Tau)
btn_alpha.place(x = 0+wid*4,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'φ',command = Phi)
btn_alpha.place(x = 0+wid*5,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'χ',command = Chi)
btn_alpha.place(x = 0+wid*6,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'ψ',command = Psi)
btn_alpha.place(x = 0+wid*7,y = 350+hei*1,width = wid,height = hei)
btn_alpha = Button(root,text = 'ω',command = Omega)
btn_alpha.place(x = 0+wid*8,y = 350+hei*1,width = wid,height = hei)




# function
def xa(): 
    entry.insert('insert', '^{U}')
def xab(): 
    entry.insert('insert', '_{L}^{U}')
def ppx(): 
    entry.insert('insert', ' \frac{\partial ?}{\partial x}')
def p2px2(): 
    entry.insert('insert', ' \frac{\partial^2 ?}{\partial x^2}')
def ddx(): 
    entry.insert('insert', ' \frac{\mathrm{d} ?}{\mathrm{d} x}')
def inte(): 
    entry.insert('insert', '\int ?')
def inteab(): 
    entry.insert('insert', '\int_{L}^{U}')

btn_xa = Button(root,text = 'x^(a)',command = xa)
btn_xa.place(x = 0+wid*10,y = 350,width = wid,height = hei)
btn_xab = Button(root,text = 'x_(a)^(b)',command = xab)
btn_xab.place(x = 0+wid*11,y = 350,width = wid*2,height = hei)
btn_ppx = Button(root,text = 'p/px',command = ppx)
btn_ppx.place(x = 0+wid*13,y = 350,width = wid*2,height = hei)
btn_ddx = Button(root,text = 'd/dx',command = ddx)
btn_ddx.place(x = 0+wid*15,y = 350,width = wid,height = hei)
btn_inte = Button(root,text = 'integral',command = inte)
btn_inte.place(x = 0+wid*16,y = 350,width = wid*2,height = hei)
btn_inteab = Button(root,text = 'integralab',command = inteab)
btn_inteab.place(x = 0+wid*10,y = 350+hei,width = wid*2,height = hei)












root.bind('<Motion>', graph)
root.mainloop()