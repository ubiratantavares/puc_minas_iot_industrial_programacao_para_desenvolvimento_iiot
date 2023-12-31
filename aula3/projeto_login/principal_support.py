#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Nov 02, 2023 12:24:51 AM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import principal

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = principal.Principal(_top1)
    root.mainloop()

def clique_btnEnviar(*args):
    if _debug:
        print('principal_support.clique_btnEnviar')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

def cliquebtnEnviar(*args):
    if _debug:
        print('principal_support.cliquebtnEnviar')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

if __name__ == '__main__':
    principal.start_up()




