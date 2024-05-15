import math
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def start_button():
    global reps
    reps += 1
    work_session = WORK_MIN* 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break)
        label_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        label_title.config(text="Break" , fg=PINK)
    else:
        count_down(work_session)
        label_title.config(text="Work" , fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count% 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(countDown, text= f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_button()
        mark = ""
        session = math.floor(reps/2)
        for x in range(session):
            mark += "👍"
        check_mark.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def reseting():
    window.after_cancel(timer)
    #timer goes to 0 again
    canvas.itemconfig(countDown, text="00:00")
    #title label reset
    label_title.config(text="Timer")
    #marks removing
    check_mark.config(text="")
    #reset timing reps
    global reps
    reps = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Time Laps")
window.config(padx=100, pady=50,bg= YELLOW)

#creating the label for the title
label_title = Label(text= "Timer", fg=GREEN, bg= YELLOW, font=(FONT_NAME, 50))
label_title.grid(column=1, row=0)

#creating the canvas and the bg image
canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)

countDown = canvas.create_text(100,130, text="00.00" , fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_mark = Label(  fg=RED , bg=YELLOW , font=(FONT_NAME , 25))
check_mark.grid(column=1 , row=3)

start = Button(text="Start", highlightthickness=0, command=start_button)
start.grid(column= 0, row= 2)

end = Button(text="Reset", command= reseting)
end.grid(column=2, row= 2)


window.mainloop()