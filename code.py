import tkinter as tk
from tkinter import ttk
from datetime import datetime

class House:
    def __init__(self, address, price):
        self.address = address
        self.price = price

    def notify_price(self):
        return f"The price of {self.address} has changed to ₹{self.price}"

def update_prices():
    user_date = user_date_entry.get()
    if user_date == "":
        result_text.insert(tk.END, "Please fill in the date.\n", "error")
    else:
        for house in houses:
            new_price = generate_random_price(house.price)
            if new_price != house.price:
                house.price = new_price
                result_text.insert(tk.END, house.notify_price() + "\n", "update")

def generate_random_price(current_price):
    return current_price + 10000

def start_notification():
    global houses
    houses = [
        House("HOUSE:-150,DELHI,Shanti Niketan", 100000),
        House("HOUSE:-169,DELHI,Ganga Kutir", 200000),
        House("HOUSE:-180,DELHI,Raj Maha", 300000),
        House("HOUSE:-160,DELHI,Krishna Vatika", 400000),
        House("HOUSE:-260,DELHI,Gharonda", 500000),
        House("HOUSE:-143,DELHI,Prakriti Kunj", 600000),
        House("HOUSE:-163,DELHI,Udaan Bhavan", 700000),
        House("HOUSE:-083,DELHI,Chhaya Ghar", 800000),
        House("HOUSE:-333,DELHI,Swarg Nivas", 900000),
        House("HOUSE:-343,DELHI,Sundar Vihar", 1000000),
        House("HOUSE:-283,DELHI,Amrita Bhavan", 1100000),
        House("HOUSE:-143,DELHI,Vasant Vihar", 1200000),
        House("HOUSE:-293,DELHI,Gokul Dham", 1300000),
        House("HOUSE:-213,DELHI,Pushpanjali", 1400000),
        House("HOUSE:-173,DELHI,Anand Lok", 1500000),
        House("HOUSE:-123,DELHI,Yamuna View", 1600000),
        House("HOUSE:-193,DELHI,Anmol Residency", 1700000),
        House("HOUSE:-233,DELHI,Roshan Mahal", 1800000),
        House("HOUSE:-343,DELHI,Harmony House", 1900000),
        House("HOUSE:-153,DELHI,Surya Bhavan", 2000000),
        House("HOUSE:-203,DELHI,Himalaya Residency", 2100000),
        House("HOUSE:-223,DELHI,Swarna Bhumi", 2200000),
        House("HOUSE:-443,DELHI,Chitrakoot Abode", 2300000),
        House("HOUSE:-993,DELHI,Gulmohar Enclave", 2400000),
        House("HOUSE:-873,DELHI,Parijat Villa", 2500000),
    ]
    update_prices()

def clear_result():
    result_text.delete(1.0, tk.END)
    user_date_entry.delete(0, tk.END)
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_label.config(text=f"Current Date: {current_date}")

def get_user_date():
    user_date = user_date_entry.get()
    try:
        datetime.strptime(user_date, "%Y-%m-%d")
        date_label.config(text=f"User Date: {user_date}")
    except ValueError:
        date_label.config(text="Invalid Date Format")

root = tk.Tk()
root.title("House Price Notification")

frame = ttk.Frame(root, padding="30", style="My.TFrame")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

style = ttk.Style()
style.configure("My.TFrame", background='#ADD8E6')  # Light Blue

style.configure("TButton", background='#00FF00')  # Green (Update Button)
style.map("TButton", background=[('active', '#00FF00')])

start_button = ttk.Button(frame, text="Start Notifications", command=start_notification, style="TButton")
start_button.grid(row=0, column=0, pady=(0, 10))

update_button = ttk.Button(frame, text="Update Prices", command=update_prices, style="TButton")
update_button.grid(row=1, column=0, pady=(10, 10))

clear_button = ttk.Button(frame, text="Clear", command=clear_result)
clear_button.grid(row=1, column=1, pady=(10, 10))

user_date_label = ttk.Label(frame, text="Enter Date (YYYY-MM-DD):", font=("Arial", 12, "bold"))
user_date_label.grid(row=2, column=0, pady=(10, 0))

user_date_entry = ttk.Entry(frame, font=("Arial", 12))
user_date_entry.grid(row=2, column=1, pady=(10, 0))

get_user_date_button = ttk.Button(frame, text="Get User Date", command=get_user_date)
get_user_date_button.grid(row=3, column=1, pady=(10, 0))

style.configure("TButton", background='#FF0000')  # Red (Start Button)

result_text = tk.Text(frame, height=25, width=120)
result_text.grid(row=4, column=0, pady=(10, 0), columnspan=2)

# Define tag configurations
result_text.tag_configure("update", background="lightgreen", foreground="black")  # Green for update notifications
result_text.tag_configure("reset", font=('Arial', 12, 'bold'), foreground="black", background="lightblue")  # Reset tag
result_text.tag_configure("error", foreground="red")  # Red for error messages

# Add "Notification" label with tags
result_text.insert(tk.END, "Notification", "reset")

# Add date section
current_date = datetime.now().strftime("%Y-%m-%d")
date_label = ttk.Label(frame, text=f"Current Date: {current_date}", font=("Arial", 12, "bold"))
date_label.grid(row=5, column=0, pady=(10, 0), columnspan=2)

root.mainloop()
