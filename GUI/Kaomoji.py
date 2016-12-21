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
ur'(*^ω^)',
ur'(′?｀*)',
ur'(-??-)',
ur'(o^▽^o)',
ur'(⌒▽⌒)☆',
ur'(￣ω￣)',
ur'(o?ω?o)',
ur'(＠＾－＾)',
ur'(^人^)',
ur'(o′▽`o)',
ur'(*′▽`*)',
ur'(′ω｀)',
ur'(≧?≦)',
ur'(o′?｀o)',
ur'(＾▽＾)',
ur'(⌒ω⌒)',
ur'╰(▔?▔)╯',
ur'(─??─)',
ur'(???)',
ur'(???)',
ur'(☆▽☆)',
ur'(⌒?⌒)',
ur'＼(≧▽≦)／',
ur'⌒(o＾▽＾o)ノ',
ur'(*?▽?*)',
ur'(???)',
ur'(?ω?)',
ur'(￣▽￣)',
ur'ヽ(>?',
ur'o(≧▽≦)o',
ur'(☆ω☆)',
ur'(っ?ω?? )',
ur'＼(￣▽￣)／',
ur'(*ˉ︶ˉ*)',
ur'＼(＾▽＾)／',
ur'\(★ω★)/',
ur'\(^ヮ^)/',
ur'(〃＾▽＾〃)',
ur'(╯?▽?)╯',
ur'o(>ω'],
'Love':[
ur'(?′з｀)ノ',
ur'(?μ_μ)',
ur'(￣ε￣＠)',
ur'ヽ(???)ノ',
ur'(─??─)?',
ur'(*???)',
ur'(′ω｀?)',
ur'(???)?',
ur'(??▽??)',
ur'?(。-ω-)',
ur'(′ε｀ )?',
ur'(?˙︶˙?)',
ur'?＼(￣▽￣)／?',
ur'(⌒▽⌒)?',
ur'?(?ε?)?',
ur'? (￣З￣)',
ur'(?ω?)',
ur'(′???`)',
ur'(°?°?)',
ur'(⌒_⌒;)',
ur'(*/ω＼)',
ur'(*/。＼)',
ur'(*/_＼)',
ur'(*?ω?)',
ur'(*μ_μ)',
ur'(?.?)',
ur'(//▽//)',
ur'(//ω//)',
ur'(ノ*?▽?*)',
ur'(*?▽?)',
ur'(￣▽￣*)ゞ',
ur'(*/▽＼*)'],
'Sympathy':[
ur'(ノ_',
ur'(＃＞＜)',
ur'☆ｏ(＞＜；)○',
ur'(￣ ￣|||)',
ur'(；￣Д￣)',
ur'(￣□￣」)',
ur'(＃￣0￣)',
ur'(＃￣ω￣)',
ur'(￢_￢;)',
ur'(＞ｍ＜)',
ur'(」゜ロ゜)」',
ur'(〃＞＿＜;〃)',
ur'(＾＾＃)',
ur'(︶︹︺)',
ur'(￣ヘ￣)',
ur'(￣︿￣)',
ur'(＞﹏＜)',
ur'凸(￣ヘ￣)',
ur'ヾ( ￣O￣)ツ',
ur'(????)',
ur'o(>',
ur'(」＞＜)」',
ur'(???)?',
ur'(?_?)'],
'Anger':[
ur'(＃`Д′)',
ur'(｀皿′＃)',
ur'(｀ω′)',
ur'(?｀ω′?)',
ur'(｀ー′)',
ur'ヽ(｀⌒′メ)ノ',
ur'凸(｀△′＃)',
ur'(｀ε′)',
ur'ψ(｀?′)ψ',
ur'ヾ(｀ヘ′)??',
ur'ヽ(‵﹏′)ノ',
ur'(?｀?′)',
ur'(╬｀益′)',
ur'┌∩┐(◣_◢)┌∩┐',
ur'凸(｀?′)凸',
ur'Σ(▼□▼メ)',
ur'(°?°╬)',
ur'ψ(▼へ▼メ)～→',
ur'(ノ°益°)ノ',
ur'(?▼益▼)',
ur'(?｀?′)凸',
ur'((╬◣﹏◢))',
ur'(╬ ò﹏ó)',
ur'(凸?益?)凸',
ur'↑_(ΦwΦ)Ψ',
ur'←~(Ψ▼?▼)∈',
ur'?(?益?)?',
ur'(??益?)?'],
'Sorrow':[
ur'(ノ_',
ur'(*-_-)',
ur'(′-ω-｀)',
ur'(μ_μ)',
ur'(?Д`)',
ur'(-ω-、)',
ur'。゜゜(′Ｏ｀)°゜。',
ur'o(TヘTo)',
ur'(；ω；)',
ur'( ?，_ゝ｀)',
ur'(个_个)',
ur'(╯︵╰,)',
ur'???(?>',
ur'(╯_╰)',
ur'(╥_╥)',
ur'(／??、)',
ur'(ノ_',
ur'(╥﹏╥)',
ur'(つω`*)',
ur'(?ω??)',
ur'???(?>ω',
ur'(T_T)',
ur'(>_',
ur'(Ｔ▽Ｔ)',
ur'o(〒﹏〒)o',
ur'(?﹏?)'],
'Fear':[
ur'(ノωヽ)',
ur'(／。＼)',
ur'(?_ヽ)',
ur'..?ヾ(。＞＜)シ',
ur'(″ロ゛)',
ur'(?人?)',
ur'＼(〇_ｏ)／',
ur'(/ω＼)',
ur'(/_＼)',
ur'?(＞＜)?',
ur'Σ(°△°|||)︴',
ur'(((＞＜)))',
ur'{{ (>_',
ur'ヽ(′ー｀)┌',
ur'┐(‘～` )┌',
ur'ヽ(　￣д￣)ノ',
ur'┐(￣ヘ￣)┌',
ur'ヽ(￣～￣　)ノ',
ur'╮(￣_￣)╭',
ur'ヽ(ˇヘˇ)ノ',
ur'┐(￣～￣)┌',
ur'┐(︶▽︶)┌',
ur'╮(￣～￣)╭',
ur'ˉ\_(ツ)_/ˉ',
ur'┐(′д｀)┌',
ur'╮(︶︿︶)╭',
ur'┐(￣?￣)┌',
ur'╮(︶▽︶)╭',
ur'(￣ω￣;)',
ur'σ(￣、￣〃)',
ur'(￣～￣;)',
ur'(?_?ヾ',
ur'(〃￣ω￣〃ゞ',
ur'┐(￣ヘ￣;)┌',
ur'(?_?;)',
ur'(￣_￣)???',
ur'╮(￣ω￣;)╭',
ur'(￣.￣;)',
ur'(＠_＠)',
ur'(??;)ゞ',
ur'Σ(￣。￣?)',
ur'(◎ ◎)ゞ',
ur'(ーー;)',
ur'?(ˉロˉ"?)'],
'Doubt':[
ur'(￢_￢)',
ur'(→_→)',
ur'(￢ ￢)',
ur'(￢?￢ )',
ur'(?_? )',
ur'(←_←)',
ur'(? ? )',
ur'(??? )',
ur'(?_?)',
ur'(?_?)'],
'Surprise':[
ur'w(?ｏ?)w',
ur'ヽ(?〇?)?',
ur'Σ(O_O)',
ur'Σ(?ロ?)',
ur'(⊙_⊙)',
ur'(o_O)',
ur'(O_O;)',
ur'(O.O)',
ur'(?ロ?) !',
ur'(□_□)',
ur'Σ(□_□)',
ur'∑(O_O;)'],
'Greeting':[
ur'(*?ω?)?',
ur'(￣▽￣)ノ',
ur'(?▽?)/',
ur'(*′?｀)?',
ur'(＠′ー`)??',
ur'＼(⌒▽⌒)',
ur'ヾ(☆▽☆)',
ur'(^０^)ノ',
ur'~ヾ(?ω?)',
ur'(???)ノ',
ur'ヾ(^ω^*)',
ur'(?_?)ノ',
ur'(o′ω`o)?',
ur'(￣ω￣)/',
ur'(′ω｀)ノ?',
ur'(⌒ω⌒)?',
ur'(≧▽≦)/',
ur'(???)/',
ur'(￣▽￣)/'],
'Hugging':[
ur'(づ￣ 3￣)づ',
ur'(つ≧▽≦)つ',
ur'(つ?ω?)つ',
ur'(っ???)っ',
ur'(づ?﹏?)づ',
ur'?(￣▽￣)?'],
'Winking':[
ur'(^_~)',
ur'( ?ｏ⌒)',
ur'(^_-)≡☆',
ur'(^ω~)',
ur'(>ω^)',
ur'(~人^)',
ur'(^_-)',
ur'( -_?)',
ur'(^_',
ur'(^人',
ur'☆⌒(≧▽?° )',
ur'☆⌒(ゝ。?)',
ur'(^_',
ur'(^_?)☆',
ur'(?ω',
ur'(シ_ _)シ',
ur'人(_ _*)',
ur'(*_ _)人',
ur'(シ. .)シ',
ur'(*￣ii￣)',
ur'(￣?￣*)',
ur'\(￣?￣)',
ur'(＾??＾)',
ur'(＾〃＾)',
ur'(￣ ¨ヽ￣)',
ur'(￣ ;￣)',
ur'(￣ ;;￣)'],
'Hiding':[
ur'|?ω?)',
ur'?(?_|',
ur'|ω?)?',
ur'ヾ(?|',
ur'|д?)',
ur'|_￣))',
ur'|▽//)',
ur'|_?)',
ur'|?д?)?',
ur'|???)╯'],
'Writing':[
ur'__φ(．．)',
ur'( ￣ー￣)φ__',
ur'__φ(。。)',
ur'__φ(．．;)',
ur'__φ(◎◎ヘ)'],
'Running':[
ur'ε=ε=┌( >_',
ur'。。。ミヽ(。＞＜)ノ'],
'Cat':[
ur'(=①ω①=)',
ur'(=；?；=)',
ur'(=｀ω′=)',
ur'(=⌒??⌒=)',
ur'(＾? ω ?＾)'],
'Bear':[
ur'(′(?)｀)',
ur'(／￣(?)￣)／',
ur'(￣(?)￣)',
ur'(／(?)＼)'],
'Dog':[
ur'∪＾ェ＾∪',
ur'∪?ω?∪',
ur'∪￣-￣∪',
ur'∪???∪',
ur'Ｕ^皿^Ｕ',
ur'ＵＴ?ＴＵ',
ur'U^?^ur',
ur'V●?●V'],
'Rabbit':[
ur'／(? × ?)＼',
ur'／(=′x`=)＼',
ur'／(^ × ^)＼',
ur'／(＞×＜)＼',
ur'／(???)＼'],
'Pig':[
ur'(′(00)｀)',
ur'(￣(ω)￣)',
ur'(′(oo)｀)',
ur'＼(￣(oo)￣)／',
ur'(￣(00)￣)'],
'Bird':[
ur'(￣Θ￣)',
ur'(`?Θ?′)',
ur'(｀Θ′)',
ur'(?Θ?)',
ur'＼(｀Θ′)／',
ur'(?θ?)',
ur'(?Θ?)',
ur'ヾ(￣◇￣)ノ〃'],
'Fish':[
ur'(°)#))',
ur'ζ°)))彡',
ur'>°))))彡',
ur'(°))',
ur'>^)))'],
'Friends':[
ur'＼(＾?＾)メ(＾?＾)ノ'],
'Enemies':[
ur'ヽ(>_',
ur'ヘ(>_'],
'Weapons':[
ur'￢o(￣-￣?)',
ur'―(T_T)→',
ur'((( ￣□)_／',
ur'(?￣▽￣)︻┳═一',
ur'Q(｀⌒′Q)'],
'Magic':[
ur'(?>ω',
ur'(＃￣□￣)o━∈??━━━━☆',
ur'(∩｀?′)?━炎炎炎炎炎'],
'Cheers':[
ur'(　’ω’)旦~~┏━┓'],
'Music':[
ur'ヘ(￣ω￣ヘ)',
ur'(?￣▽￣)?',
ur'?(￣▽￣?)',
ur'└(￣-￣└))',
ur'((┘￣ω￣)┘',
ur'√(￣‥￣√)',
ur'└(＾＾)┐',
ur'┌(＾＾)┘',
ur'＼(￣▽￣)＼',
ur'／(￣▽￣)／',
ur'(^_^?)',
ur'(~?▽?)~',
ur'~(?▽?~)',
ur'ヾ(?■_■)ノ?',
ur'(?￣△￣)?',
ur'(~￣▽￣)~',
ur'~(?▽?)~'],
'Games':[
ur'Ю　○三　＼(￣^￣＼)'],
'Special':[
ur'(￣^￣)ゞ',
ur'(－??)',
ur'(╯°益°)╯彡┻━┻'],
'money':[
ur'(?_?)',
ur'(￣﹃￣)'],
'hungry':[
ur'( ?▽?)っ?'],
'eating':[
ur'(っ????)'],
'yummy':[
ur'(　?ω?)?',
ur'(?■_■)']}


Dict = {'also':'Hello world'}

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

    # def comparison(self):
        # pattern = re.compile('.*' + self.var.get() + '.*')
        # return [w for w in self.lista if re.match(pattern, w)]
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

