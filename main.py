from tkinter import *
import math
from pygame import mixer
import time

import turtle

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0


#---------------------------------add sound----------------------------------#
def play_sounds():
    mixer.init()
    sound = mixer.Sound("mixkit-positive-notification-951.wav")
    sound.play()


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvass.itemconfig(timer_text, text="00:00")

    timer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_button_function():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sce = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 and reps > 0:
        count_down(long_break_sec)
        timer_label.config(text="Long break", font=(FONT_NAME, 20, "bold"), fg=RED, bg=YELLOW)
        play_sounds()

    elif reps % 2 == 0 and reps > 0:
        count_down(short_break_sce)
        timer_label.config(text="Short break", font=(FONT_NAME, 20, "bold"), fg=PINK, bg=YELLOW)
        play_sounds()

    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# import time
# count = 0
# time_count = True
# while time_count:
#     time.sleep(1)
#     count += 1
#     print(count)
#     if count == 30:
#         print("it's just 60 second, get up now and do something")
#         time_count = False

def count_down(count):
    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvass.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_button_function()
        marks = ""
        work_session = math.floor(reps / 2)
        for n in range(work_session):
            marks += "✔"
            check_mark_label.config(text=marks)


# # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvass = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoeimage = PhotoImage(file="tomato.png")
canvass.create_image(100, 112, image=tomatoeimage)

timer_text = canvass.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvass.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg="green", bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = Label(text="", foreground="green", bg=YELLOW)
check_mark_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_button_function)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
