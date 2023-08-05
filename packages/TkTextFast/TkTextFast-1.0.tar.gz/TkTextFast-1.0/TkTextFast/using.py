from __init__ import *
from tkinter import *

tk = Tk()
a = Text(tk)
a.pack(fill=BOTH,expand=1)



transtext(a,"color:red font:楷体 size:30 just:center | Hello world!")

mainloop()