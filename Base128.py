import tkinter as tk
import base128


def start():
    s=cnt.get()
    ec=base128.base128()
    ec=list(ec.encode(s.encode("utf-8")))[0]
    out.delete(0,tk.END)
    out.insert(0,ec)
w=tk.Tk()
w.title("Base128 Encrypt")
w.geometry("1000x500")
tk.Label(w,text="Base128 Encrypt").pack()
cnt=tk.Entry(w)
cnt.pack()
tk.Button(w,text="Encrypt",command=start).pack()
out=tk.Entry(w)
out.pack()
tk.Label(w,text="Result⇧").pack()
w.mainloop()