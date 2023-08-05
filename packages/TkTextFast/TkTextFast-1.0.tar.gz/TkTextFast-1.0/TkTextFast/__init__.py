from tkinter import *
from tkinter.font import Font

index = 0
fam = None
siz = None

def transtext(class_,word):
    global index,fam,siz
    index += 1
    a = word.split(" | ")
    try:
        value = a[0].split(" ")
    except:
        class_.insert(END,word,f"a{index}")
    else:
        class_.insert(END, a[1], f"a{index}")
        for j in value:

            nv = j.split(":")
            if nv[0] == "color":
                set_color = nv[1]
                class_.tag_config(f"a{index}",foreground=set_color)
            if nv[0] == "back":
                set_back = nv[1]
                class_.tag_config(f"a{index}", background=set_back)
            if nv[0] == "size":
                set_big = nv[1]
                if fam == None:
                    b = Font(size=int(set_big))
                    class_.tag_config(f"a{index}",font=b)

                else:
                    b = Font(size=int(set_big),family=fam)
                    class_.tag_config(f"a{index}",font=b)
                siz = int(set_big)
            if nv[0] == "font":
                set_font = nv[1]
                if siz == None:

                    bf = Font(family=set_font)
                    class_.tag_config(f"a{index}",font=bf)
                else:
                    bf = Font (size=siz,family=set_font)
                fam = set_font
            if nv[0] == "just":
                set_just = nv[1]
                class_.tag_config(f'a{index}',justify = set_just)
    index += 1
    siz = None
    fam = None