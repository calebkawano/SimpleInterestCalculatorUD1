import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principle = float(principle_entry.get())
        rate = float(rate_entry.get()) /100
        time = float(time_entry.get())
        num_compounds = 12  # Assuming compounds monthly

        # Calculate compound interest
        amount = principle * (1 + rate / num_compounds) ** (num_compounds * time)

        # Display the result
        messagebox.showinfo("Compound Interest Calculator", 
                            f'After compounding for {time} years at {rate*100:.2f}% interest annually, '
                            f'your principle of ${principle:.2f} will total ${amount:.2f}')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def run_gui():
    global principle_entry, rate_entry, time_entry

    # Create the main window
    root = tk.Tk()
    root.title("Compound Interest Calculator")

    # Create labels and entry fields
    tk.Label(root, text="Principle amount:").pack()
    principle_entry = tk.Entry(root)
    principle_entry.pack()

    tk.Label(root, text="Annual interest rate (%):").pack()
    rate_entry = tk.Entry(root)
    rate_entry.pack()

    tk.Label(root, text="Years to compound:").pack()
    time_entry = tk.Entry(root)
    time_entry.pack()

    # Create calculate button
    calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
    calculate_button.pack()

    # Run the GUI main loop
    root.mainloop()

# Run GUI directly if this script is executed
if __name__ == "__main__":
    run_gui()