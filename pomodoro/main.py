from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
clock = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(clock)
    canvas.itemconfig(timer_txt, text="00:00")
    title_txt.config(text="Timer", fg=GREEN)
    reps = 0
    mark_txt.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0 and reps:
        count_down(WORK_MIN * 60)
        title_txt.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_txt.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_txt.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = "{:0>2}".format(count // 60)  # or math.floor()
    count_sec = "{:0>2}".format(round(count % 60, 2))
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += CHECKMARK
            mark_txt.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_txt = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
title_txt.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

restart_btn = Button(text="Restart", command=reset_timer)
restart_btn.grid(column=2, row=2)

mark_txt = Label(text="", bg=YELLOW,
                 fg=GREEN, font=(FONT_NAME, 14, "bold"))
mark_txt.grid(column=1, row=3)
print()

window.mainloop()