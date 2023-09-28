# Autor: Prof. Pedro H.J
# Data: 28/11/22
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import telas
from tanque import *
from monitor import *

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = telas.tela1(_top1)
    t1 = Tanque(_w1)
    m1 = Monitor(t1)


    root.mainloop()

if __name__ == '__main__':
    telas.start_up()