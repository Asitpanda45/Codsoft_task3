from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
    userid = userid_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "userid": userid,
        "password": password
    }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUserid:{userid} "
                                                              f"\nPassword:{password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("records.json", "r") as all_records:
                    # Reading old data
                    data = json.load(all_records)
            except FileNotFoundError:
                with open("records.json", "w") as all_records:
                    json.dump(new_data, all_records,indent=4)
            else:
                data.update(new_data)
                with open("records.json", "w") as all_records:
                    # Writing the new data
                    json.dump(data, all_records, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(110, 90, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

userid_entry = Entry(width=53)
userid_entry.grid(row=2, column=1, columnspan=2)
userid_entry.insert(END, "xyzG@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21, )
password_entry.grid(sticky=EW, column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
