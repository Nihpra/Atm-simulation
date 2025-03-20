import tkinter as atm
from tkinter import *


cblue = "#080414"
cyellow = "#ffff1a"
cgray = "#C0C0C0"
cgreen = "#00ff00"
cred = "#ff1a1a"

# REGISTERS
global AX
global BX
global CX
global ZF
global M1

AX = 0
BX = 0
CX = 0
ZF = 0
M1 = 1000


def MOV():
    global CX
    CX = AX

def SUB():
    global AX
    AX = AX - BX

def exit():
    ATM_app.quit()

# BUTTONS
def btn_comp(tab):
    # ATM FUNCTIONS
    def title(tab):
        h1 = Label(tab, text="8086 ATM SIMULATOR", font=('Century 40 bold'), bg=cblue, fg="white")
        h1.place(x="150", y="20")

    def open():
        num = screen_display.get()
        if num != '':
            ATM_app.destroy()
            w2 = atm.Tk()
            w2.title("ATM")
            w2.geometry("900x500+230+110")
            w2.configure(bg=cblue)
            title(w2)

            # FUNCTIONS
            def balance():
                bal_info = Label(w2, text="₱" + str(M1) + ".00", font=("Century", 50), bg=cblue, fg="white")
                bal_info2 = Label(w2, text="Available balance", font=("Century 15 bold"), bg=cblue, fg="white")
                bal_info.place(x="520", y="190")
                bal_info2.place(x="575", y="270")

              
