import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.minutes = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.time = tk.Label(self)
        self.time["text"] = self.getMinutes() + self.getSeconds()
        self.time.pack(side="top")

        self.add = tk.Button(self)
        self.add["text"] = "+"
        self.add["command"] = self.addMinutes
        self.add.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def addMinutes(self):
        self.minutes += 5
        self.time["text"] = self.getMinutes() + self.getSeconds()

    def getMinutes(self):
        if(self.minutes >= 10):
            return str(self.minutes)
        return "0" + str(self.minutes)

    def getSeconds(self):
        return ":00"
