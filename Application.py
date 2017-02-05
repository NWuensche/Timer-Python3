import tkinter as tk
import threading
import time
import pyglet

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.minutes = 0
        self.seconds = 0
        self.tick = threading.Timer(1.0, self.updateSeconds)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.time = tk.Label(self)
        self.time["text"] = self.getTime()
        self.time.pack(side="top")

        self.add = tk.Button(self)
        self.add["text"] = "+"
        self.add["command"] = self.addMinutes
        self.add.pack(side="top")

        self.subtract = tk.Button(self)
        self.subtract["text"] = "-"
        self.subtract["command"] = self.subtractMinutes
        self.subtract.pack(side="top")

        self.start = tk.Button(self)
        self.start["text"] = "start"
        self.start["command"] = self.startTimer
        self.start.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.stopTimer)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def addMinutes(self):
        self.minutes += 5
        self.time["text"] = self.getTime()

    def subtractMinutes(self):
        if(self.minutes >= 5):
            self.minutes -= 5
            self.time["text"] = self.getTime()

    def startTimer(self):
        self.tick.start()

    def stopTimer(self):
        self.master.destroy()
        self.tick.cancel()

    def updateSeconds(self):
        while(True):
            if(self.seconds == 0):
                if(self.minutes == 0):
                    bell = pyglet.media.load('bell.wav')
                    bell.play()
                    self.tick.cancel()
                    self.tick = threading.Timer(1.0, self.updateSeconds)
                    break
                self.minutes -= 1
            self.seconds = (self.seconds - 1) % 60
            self.time["text"] = self.getTime()
            print(str(self.seconds))
            time.sleep(1)

    def getTime(self):
        return self.getMinutes() + self.getSeconds()

    def getMinutes(self):
        if(self.minutes >= 10):
            return str(self.minutes)
        return "0" + str(self.minutes)

    def getSeconds(self):
        if(self.seconds >= 10):
            return ":" + str(self.seconds)
        return ":0" + str(self.seconds)
