from tkinter import *
FONT = ("Arial", 12, "normal")


def calculate():
    value = int(input.get())
    value *= 1.609344
    convert_value_txt.config(text=f"{round(value, 2)}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)  # space around window or items

# input
input = Entry(width=10)
input.grid(column=1, row=0)

# Miles
miles_txt = Label(text="Miles", font=FONT)
miles_txt.grid(column=2, row=0)
miles_txt.config(padx=10, pady=10)

# is_equal
is_equal_txt = Label(text="is equal to", font=FONT)
is_equal_txt.grid(column=0, row=1)
is_equal_txt.config(padx=10, pady=10)

# convert_value
convert_value_txt = Label(text="0", font=FONT)
convert_value_txt.grid(column=1, row=1)
convert_value_txt.config(padx=10, pady=10)

# km
km_txt = Label(text="Km", font=FONT)
km_txt.grid(column=2, row=1)
km_txt.config(padx=10, pady=10)

# calculate
calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=3)

window.mainloop()
