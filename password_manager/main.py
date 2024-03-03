from tkinter import *
from brain import Brain
import resources
FONT = ("Courier", 12, "normal")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_txt = Label(text="Website:", font=FONT)
website_txt.grid(row=1, column=0)
username_txt = Label(text="Email/Username:", font=FONT)
username_txt.grid(row=2, column=0)
passwd_txt = Label(text="Password:", font=FONT)
passwd_txt.grid(row=3, column=0)

# Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=51)
username_entry.insert(END, string=resources.DEFAULT_EMAIL)
username_entry.grid(row=2, column=1, columnspan=2)
passwd_entry = Entry(width=32)
passwd_entry.grid(row=3, column=1)

brain = Brain(passwd_entry, username_entry, website_entry)

# Buttons
search_btn = Button(text="Search", width=14, command=brain.search_website)
search_btn.grid(row=1, column=2)
passwd_btn = Button(text="Generate Password", command=brain.generate_passwd)
passwd_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=43, command=brain.save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
