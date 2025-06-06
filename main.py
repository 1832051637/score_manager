from tkinter import *
from tkinter import simpledialog, messagebox

gui = Tk()
score_list = []


def show_menu():
    pass

def add_score():
    gui.iconify()
    cancelled = False
    while not cancelled:
        name = simpledialog.askstring("Add Score", "Enter student's name (Cancel to stop):")
        cancelled = (name == None)
        if not cancelled:
            try:
                score = float(simpledialog.askstring("Add Score", f"Enter score for {name}:"))
                score_list.append({"Name": name, "Score": score})
            except:
                messagebox.showerror("Input Error", "Invalid score input.")
    gui.deiconify()

def show_score():
    gui.iconify()

    if len(score_list) == 0:
        messagebox.showinfo("Notice", "No scores available")
    else:
        score_output = ""
        all_scores = []
        for student in score_list:
            all_scores.append(student["Score"])
            score_output += f"{student["Name"]}: {student["Score"]}\n"
        # print(all_scores)
        score_output += f"Highest: {max(all_scores)}\n" \
                    + f"Lowest: {min(all_scores)}\n" \
                    + f"Mean: {sum(all_scores)/len(all_scores)}\n"
        messagebox.showinfo("Scores", score_output)
        

    gui.deiconify()
    pass

def remove_score():
    pass

def modify_score():
    pass

def exit_app():
    exit()

# Some GUI Configs
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
gui.iconphoto(False, PhotoImage(file="resources/images/icon.png"))


Label(gui, text="Welcome to score manager!", font=("Arial", 16), pady=10).pack()
button_frame = Frame(gui)
button_frame.pack(pady=10)

Button(
    button_frame, text="Add Score", width=20, command=add_score
    ).grid(row=0, column=0, pady= 10)
Button(
    button_frame, text="Show Score", width=20, command=show_score
    ).grid(row=1, column=0, pady= 10)
Button(
    button_frame, text="Remove Score", width=20, command=remove_score
    ).grid(row=2, column=0, pady= 10)
Button(
    button_frame, text="Modify Score", width=20, command=modify_score
    ).grid(row=3, column=0, pady= 10)
Button(
    button_frame, text="Exit", width=20, fg="#FFFFFF",bg="#FF0000",
    command=exit_app
    ).grid(row=4, column=0, pady= 10)

gui.mainloop()
