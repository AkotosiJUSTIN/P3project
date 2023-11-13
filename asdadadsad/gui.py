import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_87=tk.Listbox(root)
        GListBox_87["bg"] = "#90f090"
        GListBox_87["borderwidth"] = "1px"
        GListBox_87["cursor"] = "circle"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_87["font"] = ft
        GListBox_87["fg"] = "#333333"
        GListBox_87["justify"] = "center"
        GListBox_87["relief"] = "ridge"
        GListBox_87.place(x=140,y=60,width=224,height=45)
        GListBox_87["exportselection"] = "1"

        GListBox_475=tk.Listbox(root)
        GListBox_475["bg"] = "#90f090"
        GListBox_475["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_475["font"] = ft
        GListBox_475["fg"] = "#333333"
        GListBox_475["justify"] = "center"
        GListBox_475.place(x=140,y=150,width=224,height=45)

        GLineEdit_442=tk.Entry(root)
        GLineEdit_442["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_442["font"] = ft
        GLineEdit_442["fg"] = "#333333"
        GLineEdit_442["justify"] = "center"
        GLineEdit_442["text"] = "how many questions?"
        GLineEdit_442.place(x=140,y=240,width=224,height=45)

        GButton_697=tk.Button(root)
        GButton_697["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_697["font"] = ft
        GButton_697["fg"] = "#000000"
        GButton_697["justify"] = "center"
        GButton_697["text"] = "Button"
        GButton_697.place(x=140,y=330,width=224,height=45)
        GButton_697["command"] = self.GButton_697_command

    def GButton_697_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
