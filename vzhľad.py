from tkinter import *

root = Tk()
root.geometry("731x460")
root.wm_title("Bazoš BOT pro max")

[iName, iPriceFrom, iPriceTo, iMustContain, iBrand, iAlert,iControl, iFound, iCompare
 ] = [StringVar(), IntVar(), IntVar(),
         StringVar(), StringVar(), StringVar, IntVar(), StringVar(),StringVar()]

windows = [
    {
        "obj": iName,
        "text": "Zadaj názov položky: ",
        "row": 4,
        "col": 0
    },
    {
        "obj": iPriceFrom,
        "text": "Zadaj cenu od: ",
        "row": 5,
        "col": 0
    },
    {
        "obj": iPriceTo,
        "text": "Zadaj cenu do: ",
        "row": 6,
        "col": 0,
    },
    {
        "obj": iMustContain,
        "text": "Musí obsahovať: ",
        "row": 7,
        "col": 0,
    },
    {
        "obj": iBrand,
        "text": "Značka: ",
        "row": 8,
        "col": 0
    },
    {
        "obj": iAlert,
        "text": "Výber upozornenia: ",
        "row": 4,
        "col": 3
     },
    {
        "obj": iControl,
        "text": "Čas kontroly bazáru: ",
        "row": 5,
        "col": 3
    },
]


def create_input(obj, text, row, col):
    Label(root, text=text).grid(row=row, column=col, sticky ="w")
    Entry(root, textvariable=obj).grid(row=row, column=col + 1)

farba = Canvas(root, bg="orange",width=730, height=100).grid(row=0, column=0,pady=(0,15) , rowspan=1, columnspan=6)
heading = Label(farba, text="Bazoš BOT", font=("Verdana", 20),bg="orange").grid(row=0, column=2)

produkt = Canvas(root,bg="dark grey", width=730, height=70).grid(row=9, column=0,pady=(25,10) , rowspan=1, columnspan=6)
poloha = Label(farba, text="Nájdený produkt:       ", font=("Verdana", 12),bg="dark grey").grid(row=9, column=0)

produkt1 = Canvas(root, bg="dark grey",width=730, height=70).grid(row=10, column=0,pady=(25,10) , rowspan=1, columnspan=6)
poloha1 = Label(farba, text="Produkt na porovnanie: ", font=("Verdana", 12),bg="dark grey").grid(row=10, column=0)

for window in windows:
    create_input(window["obj"], window["text"], window["row"], window["col"])





#create_window(iName, "Zadaj názov položky: ", 3, 1)
#create_window(obj=iPrice, text="Zadaj cenu od: ", row=4, col=1)

root.mainloop()
