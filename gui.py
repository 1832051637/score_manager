import tkinter

gui = tkinter.Tk()

score_list = []

def show_menu():
    pass

def add_score():
    pass

def show_score():
    pass

def remove_score():
    pass

def modify_score():
    pass

def exit_app():
    exit()

APP_NAME = "Score Manager"
MONITOR_WIDTH = gui.winfo_screenwidth()
MONITOR_HEIGHT = gui.winfo_screenheight()
WINDOW_WIDTH = MONITOR_WIDTH // 2
WINDOW_HEIGHT = MONITOR_HEIGHT // 2
WINDOW_X = 200
WINDOW_Y = 200
WINDOW_SIZE = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}"

gui.title(APP_NAME)
gui.geometry(WINDOW_SIZE)

button_frame = tkinter.Frame(gui)

button_frame.pack(pady=10)

tkinter.Button(
    button_frame, text="Add Score", width=20, command=add_score
    ).grid(row=0, column=0, pady= 10)
tkinter.Button(
    button_frame, text="Show Score", width=20, command=show_score
    ).grid(row=1, column=0, pady= 10)

tkinter.Button(
    button_frame, text="Remove Score", width=20, command=remove_score
    ).grid(row=2, column=0, pady= 10)

tkinter.Button(
    button_frame, text="Modify Score", width=20, command=modify_score
    ).grid(row=3, column=0, pady= 10)

tkinter.Button(
    button_frame, text="Exit", width=20, fg="#FFFFFF",bg="#FF0000",
    command=exit_app
    ).grid(row=4, column=0, pady= 10)

gui.mainloop()
