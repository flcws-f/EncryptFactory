import tkinter as tk
import base64


def start():
    s=cnt.get()
    ec=base64.b32encode(s.encode("utf-8"))
    out.delete(0,tk.END)
    out.insert(0,ec)
w=tk.Tk()
w.title("Base32 Encrypt")
w.geometry("1000x500")
tk.Label(w,text="Base32 Encrypt").pack()
cnt=tk.Entry(w)
cnt.pack()
tk.Button(w,text="Encrypt",command=start).pack()
out=tk.Entry(w)
out.pack()
tk.Label(w,text="Result⇧").pack()
w.mainloop()