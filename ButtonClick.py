from tkinter import *
import subprocess

def runSelenium():
    res = subprocess.run(["pytest",'testCases/test_first.py'])
    print(res.stdout)
tk = Tk()
tk.title('Test Executor')
btn = Button(tk,text='Run',command=runSelenium)
btn.pack()
tk.mainloop()