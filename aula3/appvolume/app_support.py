#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Nov 02, 2023 02:55:45 PM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tanque import Tanque
import app

_debug = True  # False to eliminate debug printing from callback functions.


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = app.Tela(_top1)
    root.mainloop()


def enviar(*args):
    try:
        altura = float(_w1.txtAltura.get())
        diametro = float(_w1.txtDiametro.get())
        tanque = Tanque(altura, diametro)
        _w1.txtAltura.delete(0, 'end')
        _w1.txtAltura.focus_set()
        _w1.txtDiametro.delete(0, 'end')
        _w1.lblValor.config(
            text=f"{str(tanque.calcular_volume()).replace('.', ',')}")
    except ValueError:
        _w1.lblValor.config(text="Erro")


if __name__ == '__main__':
    app.start_up()
