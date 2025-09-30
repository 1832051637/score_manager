from tkinter import *
from tkinter import simpledialog, messagebox

class gui:
    def __init__(self):
        # Some GUI Configs
        
        self.gui = Tk()
        self.APP_NAME = "Score Manager"
        self.gui.title(self.APP_NAME)
        self.gui.iconphoto(False, 
                           PhotoImage(file="resources/images/icon.png"))
        self.MONITOR_WIDTH = self.gui.winfo_screenwidth()
        self.MONITOR_HEIGHT = self.gui.winfo_screenheight()
        self.WINDOW_WIDTH = self.MONITOR_WIDTH // 2
        self.WINDOW_HEIGHT = self.MONITOR_HEIGHT // 2
        self.WINDOW_X = 200
        self.WINDOW_Y = 200
        self.WINDOW_SIZE = \
        f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+"\
        f"{self.WINDOW_X}+{self.WINDOW_Y}"
        self.gui.geometry(self.WINDOW_SIZE)
        self.score_list = []
        Label(self.gui, text="Welcome to score manager!",
              font=("Arial", 16), pady=10).pack()
        self.button_frame = Frame(self.gui)
        self.button_frame.pack(pady=10)

    def start(self):
        self.put_buttons()
        self.gui.mainloop()

    def put_buttons(self):
        Button(
            self.button_frame, text="Add Score", width=20, command=self.add_score
            ).grid(row=0, column=0, pady= 10)
        Button(
            self.button_frame, text="Show Score", width=20, command=self.show_score
            ).grid(row=1, column=0, pady= 10)
        Button(
            self.button_frame, text="Remove Score", width=20, command=self.remove_score
            ).grid(row=2, column=0, pady= 10)
        Button(
            self.button_frame, text="Modify Score", width=20, command=self.modify_score
            ).grid(row=3, column=0, pady= 10)
        Button(
            self.button_frame, text="Curve", width=20, command=self.curve
            ).grid(row=4, column=0, pady= 10)
        Button(
            self.button_frame, text="Exit", width=20, fg="#FFFFFF",bg="#FF0000",
            command=self.exit_app
            ).grid(row=5, column=0, pady= 10)
        pass

    def show_menu(self):
        pass

    def add_score(self):
        self.gui.iconify()
        cancelled = False
        while not cancelled:
            name = simpledialog.askstring(
                "Add Score", "Enter student's name (Cancel to stop):")
            cancelled = (name == None)
            if not cancelled:
                try:
                    score = float(simpledialog.askstring(
                        "Add Score", f"Enter score for {name}:"))
                    self.score_list.append({"Name": name, "Score": score})
                except:
                    messagebox.showerror(
                        "Input Error", "Invalid score input.")
        self.gui.deiconify()


    def show_score(self):
        if len(self.score_list) == 0:
            messagebox.showinfo("Notice", "No scores available")
            return
        score_window = Toplevel()
        score_window.title("Score List")
        score_window.iconphoto(False, PhotoImage(file="resources/images/icon.png"))
        score_output = ""
        score_output += f"{'Name':<15}{'Score':>10}\n"
        score_output += "-" * 25  + "\n"
        all_scores = []
        for student in self.score_list:
            all_scores.append(student["Score"])
            score_output += f"{student["Name"]:<15}{student["Score"]:>10}\n"

        score_output += "-" * 25  + "\n"
        score_output += f"{'Highest:':<15}{max(all_scores):>10}\n"
        score_output += f"{'Lowest:':<15}{min(all_scores):>10}\n" 
        score_output += f"{'Mean:':<15} {sum(all_scores)/len(all_scores):>10.2f}\n"
        label = Label(score_window, text=score_output, 
                      font=("Courier", 12), justify="left", 
                      padx=10, pady=10)
        label.pack()

    def remove_score(self):
        if len(self.score_list) == 0:
            messagebox.showerror("Error", "No score to remove!")
            return
        remove_window = Toplevel()
        remove_window.title("Rmove a score")
        remove_window.iconphoto(False, PhotoImage(file="resources/images/icon.png"))

        label = Label(remove_window, text="Select a student to remove")
        label.pack(pady=5)
        list_box = Listbox(remove_window, selectmode=MULTIPLE, width=30)
        list_box.pack(pady=10, fill=BOTH, expand=True)
        for student in self.score_list:
            list_box.insert(END, f"{student['Name']} - {student['Score']}")

        def delete_selected():
            selected = list(list_box.curselection())
            if not selected:
                messagebox.showwarning("Warning", "Please select at least one student.")
                return
            for i in reversed(selected):
                self.score_list.pop(i)
            remove_window.destroy()
        delete_btn = Button(remove_window, text="Delete Selected", command=delete_selected)
        delete_btn.pack(pady=10)
    
    def modify_score(self):
        pass

    def curve(self):
        pass

    def curve_formula(self):
        pass

    def exit_app(self):
        exit()
