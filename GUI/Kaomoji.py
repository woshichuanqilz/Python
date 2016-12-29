# -*- coding: utf-8 -*-
from Tkinter import *
from fuzzyfinder import fuzzyfinder
import re
import random
from lizhelib import *
lista = [u'joy',
u'love',
u'embarrassment',
u'sympathy',
u'dissatisfaction',
u'anger',
u'sorrow',
u'fear',
u'indifference',
u'confusion',
u'doubt',
u'surprise',
u'greeting',
u'hugging',
u'winking',
u'apologizing',
u'nosebleeding',
u'hiding',
u'writing',
u'running',
u'sleeping',
u'cat',
u'bear',
u'dog',
u'rabbit',
u'pig',
u'bird',
u'fish',
u'spider',
u'friends',
u'enemies',
u'weapons',
u'magic',
u'cheers',
u'music',
u'games',
u'faces',
u'special']

KaomojiDict = {'Joy':[
ur'(?■_■)']}

class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.DicKey = ''
        self.lista = lista
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Return>", self.GetFirstContent)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):
        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def GetFirstContent(self, event):
        emoji = random.choice(KaomojiDict['Joy'])
        print emoji
        ClipCopy(emoji)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        suggestions = fuzzyfinder(self.var.get(), self.lista)
        return list(suggestions)


if __name__ == '__main__':
    root = Tk()
    entry = AutocompleteEntry(lista, root)
    entry.grid(row=0, column=0)
    entry.focus_set()
    Button(text='nothing').grid(row=1, column=0)
    Button(text='nothing').grid(row=2, column=0)
    Button(text='nothing').grid(row=3, column=0)

    root.mainloop()

