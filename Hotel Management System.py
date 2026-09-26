import tkinter as tk
from tkinter import messagebox

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("800x650")
root.config(bg="lightgray")

# ---------------- Variables ----------------
name_var = tk.StringVar()
phone_var = tk.StringVar()
room_var = tk.StringVar()
days_var = tk.StringVar()
food_var = tk.StringVar()
total_var = tk.StringVar()

# ---------------- Functions ----------------

def calculate_bill():
    try:
        days = int(days_var.get())
        food = float(food_var.get() or 0)

        room_prices = {
            "Single": 1500,
            "Double": 2500,
            "Deluxe": 4000,
            "Suite": 6000
        }

        room_type = room_var.get()

        if room_type not in room_prices:
            messagebox.showerror("Error", "Please select a room type")
            return

        room_charge = room_prices[room_type] * days
        total = room_charge + food

        total_var.set(str(total))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid number of days")


def book_room():
    if name_var.get() == "":
        messagebox.showerror("Error", "Please enter customer name")
        return

    if phone_var.get() == "":
        messagebox.showerror("Error", "Please enter phone number")
        return

    if room_var.get() == "":
        messagebox.showerror("Error", "Please select room type")
        return

    calculate_bill()

    messagebox.showinfo(
        "Success",
        "Room booked successfully!\n\n"
        "Customer Name: " + name_var.get() +
        "\nRoom Type: " + room_var.get() +
        "\nTotal Bill: ₹" + total_var.get()
    )


def checkout():
    if name_var.get() == "":
        messagebox.showerror("Error", "No customer details found")
        return

    calculate_bill()

    messagebox.showinfo(
        "Checkout",
        "Customer checked out successfully!\n\n"
        "Customer: " + name_var.get() +
        "\nTotal Bill: ₹" + total_var.get()
    )


def clear_data():
    name_var.set("")
    phone_var.set("")
    room_var.set("")
    days_var.set("")
    food_var.set("")
    total_var.set("")


# ---------------- Heading ----------------

title = tk.Label(
    root,
    text="HOTEL MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold"),
    bg="darkblue",
    fg="white",
    pady=15
)
title.pack(fill="x")


# ---------------- Customer Details ----------------

frame = tk.Frame(root, bg="lightgray")
frame.pack(pady=20)

tk.Label(
    frame,
    text="Customer Details",
    font=("Arial", 18, "bold"),
    bg="lightgray"
).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(
    frame,
    text="Customer Name:",
    font=("Arial", 12),
    bg="lightgray"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

tk.Entry(
    frame,
    textvariable=name_var,
    width=30,
    font=("Arial", 12)
).grid(row=1, column=1, padx=10, pady=8)


tk.Label(
    frame,
    text="Phone Number:",
    font=("Arial", 12),
    bg="lightgray"
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

tk.Entry(
    frame,
    textvariable=phone_var,
    width=30,
    font=("Arial", 12)
).grid(row=2, column=1, padx=10, pady=8)


# ---------------- Room Details ----------------

tk.Label(
    frame,
    text="Room Type:",
    font=("Arial", 12),
    bg="lightgray"
).grid(row=3, column=0, padx=10, pady=8, sticky="w")

room_menu = tk.OptionMenu(
    frame,
    room_var,
    "Single",
    "Double",
    "Deluxe",
    "Suite"
)
room_menu.config(width=25, font=("Arial", 11))
room_menu.grid(row=3, column=1, padx=10, pady=8)


tk.Label(
    frame,
    text="Number of Days:",
    font=("Arial", 12),
    bg="lightgray"
).grid(row=4, column=0, padx=10, pady=8, sticky="w")

tk.Entry(
    frame,
    textvariable=days_var,
    width=30,
    font=("Arial", 12)
).grid(row=4, column=1, padx=10, pady=8)


tk.Label(
    frame,
    text="Food Charges:",
    font=("Arial", 12),
    bg="lightgray"
).grid(row=5, column=0, padx=10, pady=8, sticky="w")

tk.Entry(
    frame,
    textvariable=food_var,
    width=30,
    font=("Arial", 12)
).grid(row=5, column=1, padx=10, pady=8)


tk.Label(
    frame,
    text="Total Bill:",
    font=("Arial", 12, "bold"),
    bg="lightgray"
).grid(row=6, column=0, padx=10, pady=8, sticky="w")

tk.Entry(
    frame,
    textvariable=total_var,
    width=30,
    font=("Arial", 12),
    state="readonly"
).grid(row=6, column=1, padx=10, pady=8)


# ---------------- Buttons ----------------

button_frame = tk.Frame(root, bg="lightgray")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Book Room",
    command=book_room,
    width=15,
    font=("Arial", 12, "bold")
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Calculate Bill",
    command=calculate_bill,
    width=15,
    font=("Arial", 12, "bold")
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Check Out",
    command=checkout,
    width=15,
    font=("Arial", 12, "bold")
).grid(row=0, column=2, padx=10)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_data,
    width=15,
    font=("Arial", 12, "bold")
).grid(row=0, column=3, padx=10)


# ---------------- Room Price Information ----------------

price_label = tk.Label(
    root,
    text="Room Charges:  Single ₹1500 | Double ₹2500 | Deluxe ₹4000 | Suite ₹6000 per day",
    font=("Arial", 11, "bold"),
    bg="lightgray"
)
price_label.pack(pady=10)


root.mainloop()