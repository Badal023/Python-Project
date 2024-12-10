import tkinter as tk

# Function to start the countdown
def start_timer():
    try:
        # Get the time in seconds from the input fields
        total_seconds = int(entry.get()) 
        countdown(total_seconds)
    except ValueError:
        label.config(text="Please enter a valid number")

# Function for countdown logic
def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_display = f"{mins:02}:{secs:02}"
        label.config(text=time_display)
        root.after(1000, countdown, seconds - 1)
    else:
        label.config(text="Time's up!")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Create the label for displaying time
label = tk.Label(root, text="00:00", font=("Helvetica", 40), width=10)
label.pack(pady=20)

# Create an entry box for the user to input time in seconds
entry_label = tk.Label(root, text="Enter time in seconds:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button to start the countdown
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop(
