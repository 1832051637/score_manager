import tkinter

gui = tkinter.Tk()

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

score_list = []

def show_menu():
    # Show menu to operate
    pass


gui.mainloop()
