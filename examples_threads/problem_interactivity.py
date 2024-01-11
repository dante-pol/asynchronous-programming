from tkinter import *

root = Tk("Title")
root.geometry("600x420")

btn = Button(root, text="kar kar!", command= lambda: print(input("input >>")))
btn.pack()

root.mainloop()