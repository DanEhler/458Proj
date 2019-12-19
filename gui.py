from tkinter import *
import task_parser
import subprocess as sub


class GUI(Frame):

    def createWidgets(self):
        # top = Tk()
        # sTitle = Label(top, text="Enter Number of tasks")
        # num = Entry(top, bd=5)
        #
        # # Packing
        # sTitle.pack()
        # num.pack()
        # ##
        #
        # ##
        # top.mainloop()
        #
        # numT = num.get()
        # print(numT)
        ####

        self.num = Entry(self, bd=5, textvariable=self.v)
        self.tasklist = Entry(self, bd=5, textvariable=self.va)
        ####
        self.button = Button(self, text="Enter", command=self.callback)
        self.sTitle = Label(self, text="Number of Tasks")
        self.lTitle = Label(self, text="Enter tasks as a list (c0,p0,c1,p1...)")
        self.aTitle = Label(self, text="What algorithm(s) to use")
        self.checkR = Checkbutton(self, text="RMS", variable=self.vr)
        self.checkE = Checkbutton(self, text="EDF", variable=self.ve)
        # Packing
        self.sTitle.pack()
        self.num.pack()
        self.lTitle.pack()
        self.tasklist.pack()
        self.aTitle.pack()
        self.checkR.pack()
        self.checkE.pack()
        self.button.pack()

    def output(self, output):
        self.txt = Text(self)
        self.txt.insert(END, output)
        self.txt.pack()

    def callback(self):
        self.v.get()
        self.va.get()
        self.vr.get()
        self.ve.get()
        print(self.v.get())
        print(self.va.get())
        task_parser.read(self.va.get(), self.vr.get(), self.ve.get(),self)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.v = StringVar()
        self.vr = IntVar()
        self.ve = IntVar()
        self.va = StringVar()
        self.pack()
        self.createWidgets()


root = Tk()
app = GUI(master=root)
app.mainloop()
root.destroy()
# if __name__ == "__main__":
#     test()
