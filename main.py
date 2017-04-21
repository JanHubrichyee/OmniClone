import tkinter as tk
from tkinter import ttk

#Fonts
LARGE_FONT = ("Verdana", 12)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="Icon.ico")
        tk.Tk.wm_title(self, "OmniClone")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.LabelFrame(self, width=1900, height=30, bg="white")
        frame.grid()

        frame_button = tk.Frame(self, bg="white")
        frame_button.grid(sticky="nwe")

        c_inbox = tk.LabelFrame(frame_button, width=70, height=70, borderwidth=5, highlightbackground="black", highlightcolor="white", text="inbox")
        c_projects = tk.LabelFrame(frame_button, width=70, height=70, borderwidth=5, highlightbackground="black", highlightcolor="white", text="projects")
        c_tags = tk.LabelFrame(frame_button, width=70, height=70, borderwidth=5, highlightbackground="black", highlightcolor="white", text="tags")
        c_forecast = tk.LabelFrame(frame_button, width=70, height=70, borderwidth=5, highlightbackground="black", highlightcolor="white", text="forecast")
        c_flagged = tk.LabelFrame(frame_button, width=70, height=70, borderwidth=5, highlightbackground="black", highlightcolor="white", text="flagged")
        c_review = tk.LabelFrame(frame_button, width=70, height=70, borderwidth=5, highlightbackground="black", highlightcolor="white", text="review")
        c_none = tk.LabelFrame(frame_button, width=70, height=500, borderwidth=5, highlightbackground="black", highlightcolor="white")

        c_sidepanel = tk.LabelFrame(frame_button, width=300, height=920, borderwidth=5, highlightbackground="black", highlightcolor="grey")
        c_mainpanel = tk.LabelFrame(frame_button, width=1000, height=920, borderwidth=5, highlightbackground="black", highlightcolor="grey")
        c_rightpanel = tk.LabelFrame(frame_button, width=300, height=920, borderwidth=5, highlightbackground="black", highlightcolor="grey")


        c_inbox.grid(row=1, sticky="W")

        c_sidepanel.grid(row=1, rowspan=7, column=1)
        c_mainpanel.grid(row=1, rowspan=7, column=2)
        c_rightpanel.grid(row=1, rowspan=7, column=3, sticky="e")

        c_projects.grid(row=2, sticky="W")
        c_forecast.grid(row=3, sticky="W")
        c_tags.grid(row=4, sticky="W")
        c_flagged.grid(row=5, sticky="W")
        c_review.grid(row=6, sticky="W")
        c_none.grid(row=7,sticky="W")



        #Startpage stuff

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #nextPage stuff


root = App()
root.mainloop()