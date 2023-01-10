import tkinter as tk
import hashlib


def start():
    s=cnt.get()
    ec=hashlib.sha1(s.encode(encoding='UTF-8')).hexdigest()
    out.delete(0,tk.END)
    out.insert(0,ec)
w=tk.Tk()
w.title("sha1 Encrypt")
w.geometry("1000x500")
tk.Label(w,text="sha1 Encrypt").pack()
cnt=tk.Entry(w)
cnt.pack()
tk.Button(w,text="Encrypt",command=start).pack()
out=tk.Entry(w)
out.pack()
tk.Label(w,text="Result⇧").pack()
w.mainloop()