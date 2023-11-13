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

        GMessage_232=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_232["font"] = ft
        GMessage_232["fg"] = "#333333"
        GMessage_232["justify"] = "center"
        GMessage_232["text"] = "difficulty"
        GMessage_232.place(x=80,y=20,width=120,height=50)

        GRadio_49=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_49["font"] = ft
        GRadio_49["fg"] = "#333333"
        GRadio_49["justify"] = "center"
        GRadio_49["text"] = "easy"
        GRadio_49.place(x=90,y=70,width=85,height=25)
        GRadio_49["command"] = self.GRadio_49_command

        GRadio_210=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_210["font"] = ft
        GRadio_210["fg"] = "#333333"
        GRadio_210["justify"] = "center"
        GRadio_210["text"] = "moderate"
        GRadio_210.place(x=100,y=110,width=85,height=25)
        GRadio_210["command"] = self.GRadio_210_command

        GRadio_742=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_742["font"] = ft
        GRadio_742["fg"] = "#333333"
        GRadio_742["justify"] = "center"
        GRadio_742["text"] = "hard"
        GRadio_742.place(x=90,y=150,width=85,height=25)
        GRadio_742["command"] = self.GRadio_742_command

        GMessage_761=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_761["font"] = ft
        GMessage_761["fg"] = "#333333"
        GMessage_761["justify"] = "center"
        GMessage_761["text"] = "operator"
        GMessage_761.place(x=290,y=20,width=120,height=50)

        GRadio_751=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_751["font"] = ft
        GRadio_751["fg"] = "#333333"
        GRadio_751["justify"] = "center"
        GRadio_751["text"] = "addition"
        GRadio_751.place(x=310,y=70,width=85,height=25)
        GRadio_751["command"] = self.GRadio_751_command

        GRadio_256=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_256["font"] = ft
        GRadio_256["fg"] = "#333333"
        GRadio_256["justify"] = "center"
        GRadio_256["text"] = "subtraction"
        GRadio_256.place(x=320,y=110,width=85,height=25)
        GRadio_256["command"] = self.GRadio_256_command

        GRadio_385=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_385["font"] = ft
        GRadio_385["fg"] = "#333333"
        GRadio_385["justify"] = "center"
        GRadio_385["text"] = "multiplication"
        GRadio_385.place(x=320,y=150,width=85,height=25)
        GRadio_385["command"] = self.GRadio_385_command

        GRadio_626=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_626["font"] = ft
        GRadio_626["fg"] = "#333333"
        GRadio_626["justify"] = "center"
        GRadio_626["text"] = "division"
        GRadio_626.place(x=310,y=190,width=85,height=25)
        GRadio_626["command"] = self.GRadio_626_command

        GLineEdit_50=tk.Entry(root)
        GLineEdit_50["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_50["font"] = ft
        GLineEdit_50["fg"] = "#333333"
        GLineEdit_50["justify"] = "center"
        GLineEdit_50["text"] = "Enter a number"
        GLineEdit_50.place(x=150,y=280,width=180,height=50)

        GMessage_927=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_927["font"] = ft
        GMessage_927["fg"] = "#333333"
        GMessage_927["justify"] = "center"
        GMessage_927["text"] = "how many questions would you like to answer?"
        GMessage_927.place(x=150,y=240,width=180,height=30)

        GButton_916=tk.Button(root)
        GButton_916["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_916["font"] = ft
        GButton_916["fg"] = "#000000"
        GButton_916["justify"] = "center"
        GButton_916["text"] = "play game"
        GButton_916.place(x=170,y=380,width=150,height=50)
        GButton_916["command"] = self.GButton_916_command

    def GRadio_49_command(self):
        print("command")


    def GRadio_210_command(self):
        print("command")


    def GRadio_742_command(self):
        print("command")


    def GRadio_751_command(self):
        print("command")


    def GRadio_256_command(self):
        print("command")


    def GRadio_385_command(self):
        print("command")


    def GRadio_626_command(self):
        print("command")


    def GButton_916_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
