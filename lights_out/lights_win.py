# import glob
# import os
# import subprocess
# import time

# import ipdb

from tkinter import ttk, Tk,  E, S, StringVar, END, VERTICAL

for r in range(5):
    for c in range(5):
        ttk.Button(
            up, text="*", command=lambda: load_directory(0)).grid(column=c, row=r, sticky=(W, E))
