from tkinter import*
import sys
from math import*


def basicCalculator(root, side):
    storeObj = Frame(root, borderwidth = 1, bd = 4, bg = "Light Slate Gray")
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj
    
def buttonsForCalculator(root, side, text, command = None):
    storeObj = Button(root, text=text, command = command)
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj
    
class application(Frame):
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
            
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Front", "FreeSans 20 Bold")
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Basic Calculator")
        
        display = StringVar()
        Entry(self, relief = RIDGE, textvariable = display, justify = "right", 
            bd = 30, bg = "Light Slate Gray").pack(side = TOP, expand = YES,
            fill = BOTH)
            
        for clearButton in (["CE"], ["C"]):
            erase = basicCalculator(self, TOP)
            for ichar in clearButton:
                buttonsForCalculator(erase, LEFT, ichar, lambda storeObj = display, 
                                    q = ichar : storeObj.set(''))
                                    
        for numButtons in ("789%", "456/", "123*", "0.-+"):
            FunctionNum = basicCalculator(self,TOP)
            for char in numButtons:
               buttonsForCalculator(FunctionNum, LEFT, char,
                    lambda storeObj = display, q = char: storeObj.set(storeObj.get() + q))
                    
        EqualsButton = basicCalculator(self, TOP)
        for iEquals in "=":
            if iEquals == "=":
                btniEquals = buttonsForCalculator(EqualsButton, LEFT, iEquals)
                btniEquals.bind("<ButtonRelease-1>", lambda e, s = self, storeObj = display:s.calc(storeObj), "+")
                
            else:
                btniEquals = buttonsForCalculator(EqualsButton, LEFT, iEquals, lambda storeObj = display,
                                                s = " %s"%iEquals: storeObj.set(storeObj.get()+s))
                    

        
if __name__ == "__main__":
    application().mainloop()
