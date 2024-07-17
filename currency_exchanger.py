import requests
import tkinter as tk
from tkinter import ttk, messagebox

API_KEY = "5dd227fc68b9656c98e5a35d2f07e222"
BASE_URL = 'http://data.fixer.io/api/latest'

def get_exchange_rates():
    url = f"{BASE_URL}?access_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if data['success']:
        return data['rates']
    else:
        print(f"Error: {data['error']['info']}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'EUR':
        amount = amount / rates[from_currency]
    converted_amount = amount * rates[to_currency]
    return converted_amount

def perform_conversion():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()
        rates = get_exchange_rates()
        
        if rates:
            if from_currency in rates and to_currency in rates:
                converted_amount = convert_currency(amount, from_currency, to_currency, rates)
                result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            else:
                messagebox.showerror("Error", "One of the currencies is not supported.")
        else:
            messagebox.showerror("Error", "Failed to retrieve exchange rates.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Set up the GUI
root = tk.Tk()
root.title("Currency Converter")

# Amount Entry
tk.Label(root, text="Enter the amount to be converted:").grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# From Currency Combobox
tk.Label(root, text="From Currency (EUR, USD):").grid(row=1, column=0, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=['USD','EUR','AUD','CHF','CNY','GBP','JPY'])
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
from_currency_combobox.current(0)

# To Currency Combobox
tk.Label(root, text="To Currency (USD, CAD):").grid(row=2, column=0, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=['USD','EUR','AUD','CHF','CNY','GBP','JPY'])
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
to_currency_combobox.current(0)

# convert
convert_button = tk.Button(root, text="Convert", command=perform_conversion)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
