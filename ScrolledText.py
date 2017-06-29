import Tkinter as tk

class ScrolledText(tk.Frame):
    def __init__(self, parent, textvariable, *args, **kwargs):
        tk.Frame.__init__(self, parent)       
        self.text = tk.Text(self, *args, **kwargs)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.bind("<Key>", self.text_changed)
        self.text.bind('<Delete>', self.text_del)
        self.text.bind('<BackSpace>', self.text_backspace)
        self.textvariable = textvariable
        self.text.bind('<Enter>', self.enter)
        self.text.bind('<Leave>', self.leave)
        
        
    def enter(self, event):
        self.text.config(cursor="hand2")

    def leave(self, event):
        self.text.config(cursor="")

    def text_changed(self, key):
        self.textvariable.set('')
        self.textvariable.set(self.text.get('1.0', tk.END))
        
    def text_backspace(self, key):
        self.textvariable.set(self.text.get('1.0', self.text.index(tk.CURRENT + ' -1 chars')))
    
    def text_del(self, key):
        self.textvariable.set(self.text.get('1.0', self.text.index(tk.INSERT)))
        
        
if __name__ == '__main__':
    
    def text_changed(textbox_name, event):
        if textbox_name == 'textbox_text':
            print event.get()
    
    gui = tk.Tk()
    textbox_text = tk.StringVar()
    textbox_text.trace("w", lambda name, index, mode, sv=textbox_text: text_changed('textbox_text', textbox_text))
    scrolled_text = ScrolledText(gui, textvariable=textbox_text)
    scrolled_text.pack()
    gui.mainloop()