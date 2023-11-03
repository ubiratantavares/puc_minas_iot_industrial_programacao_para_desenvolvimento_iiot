#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Nov 02, 2023 11:03:05 AM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import projeto

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = projeto.TelaPrincipal(_top1)
    root.mainloop()

def alertar(*args):
    if _debug:
        print('projeto_support.alertar')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

def plotar(*args):
    if _debug:
        print('projeto_support.plotar')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

if __name__ == '__main__':
    projeto.start_up()




