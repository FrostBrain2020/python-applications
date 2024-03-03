from random import shuffle, randint, choice
from tkinter import messagebox
from tkinter.constants import END
import pyperclip
import resources
import json


class Brain:
    def __init__(self, passwd_entry, username_entry, website_entry):
        self.passwd_entry = passwd_entry
        self.username_entry = username_entry
        self.website_entry = website_entry

    def generate_passwd(self):
        self.passwd_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.username_entry.insert(0, string=resources.DEFAULT_EMAIL)

        password_letters = [choice(resources.ALPHABET) for _ in range(randint(8, 10))]
        password_numbers = [choice(resources.NUMBERS) for _ in range(randint(2, 4))]
        password_symbols = [choice(resources.SYMBOLS) for _ in range(randint(2, 4))]
        password_list = password_letters + password_numbers + password_symbols
        shuffle(password_list)

        passwd = "".join(password_list)
        self.passwd_entry.insert(0, passwd)
        pyperclip.copy(passwd)

    def search_website(self):
        try:
            with open(resources.FILE_NAME, mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Oops", message="You don't have any saved passwords")
        else:
            website = self.website_entry.get()
            if website in data:
                passwd = data[website]["password"]
                username = data[website]["email"]
                pyperclip.copy(passwd)
                messagebox.showinfo(title=f"Data for {website}", message=f"Username: {username}\nPassword: {passwd}")
            else:
                messagebox.showinfo(title=f"Search result",
                                    message=f"Website {website} wasn't found in data")

    def save_data(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        passwd = self.passwd_entry.get()
        new_data = {
            website: {
                "email": username,
                "password": passwd,
            }
        }

        if website == "" or username == "" or passwd == "":
            messagebox.showerror(title="Oops", message="Please don't leave any fields")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n "
                                                                  f"Email: {username}\n Password: {passwd}\n"
                                                                  f"It ok to save?")
            if is_ok:
                file_name = resources.FILE_NAME
                try:
                    with open(file_name, mode="r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    with open(file_name, mode="w") as file:
                        json.dump(new_data, file, indent=4)
                else:
                    data.update(new_data)
                    with open(file_name, mode="w") as file:
                        json.dump(data, file, indent=4)
                finally:
                    self.website_entry.delete(0, END)
                    self.passwd_entry.delete(0, END)
                    self.username_entry.delete(0, END)
                    self.username_entry.insert(0, string=resources.DEFAULT_EMAIL)