import tkinter as UI

def test():
    top = UI.Tk()
    sTitle = UI.Label(top, text="Enter Number of tasks")
    num = UI.Entry(top, bd=5)

    # Packing
    sTitle.pack()
    num.pack()
    ##

    ##
    top.mainloop()

    numT = num.get()
    print(numT)
if __name__ == "__main__":
    test()

