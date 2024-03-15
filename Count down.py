import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime, time, date
from datetime import timedelta

root = tk.Tk()
root.title("Exam Countdown")
root.config(bg="#000000")

# Initialize exam information
exam_name = tk.StringVar()

# Function to update the countdown
def update_countdown(exam_datetime, exam_name):
    # Calculate the time remaining until the exam
    time_remaining = exam_datetime - datetime.now()
    if time_remaining <= timedelta(0):
        # If time is up, display a message
        countdown_label.config(text="Time's up!")
    else:
        # Otherwise, update the countdown label with exam name and time remaining
        time_remaining_str = str(time_remaining).split(".")[0]  # Remove microseconds
        countdown_label.config(text="{0}: {1}".format(exam_name, time_remaining_str))
        # Schedule the next update after 1 second
        root.after(1000, update_countdown, exam_datetime, exam_name)

# Function to delete countdown
def delete_countdown(countdown_frame):
    countdown_frame.destroy()

# Set the font and color of the countdown label
countdown_frame = tk.Frame(root, bg="#000000")
countdown_frame.pack(pady=50, fill=tk.BOTH, expand=1)
countdown_label = tk.Label(countdown_frame, font=("fenwick outline", 40), fg="#00FF00", bg="#000000")
countdown_label.pack(side=tk.LEFT)

# Add delete button to countdown frame
delete_button = tk.Button(countdown_frame, text="Delete", font=("fenwick outline", 20), bg="#000000", fg="#FF0000", command=lambda: delete_countdown(countdown_frame))
delete_button.pack(side=tk.RIGHT, padx=10)

# Add entry fields for exam information
exam_frame = tk.Frame(root, bg="#000000")
exam_frame.pack(pady=(10,0))

# Add entry fields for exam information
exam_frame = tk.Frame(root, bg="#000000")
exam_frame.pack(pady=(10,0))

# Function to save exam information
def save_exam(exam_name, exam_datetime_str, exam_window):
    # Create a datetime object from the exam date and time strings
    exam_datetime = datetime.strptime(exam_datetime_str, "%Y-%m-%d %I:%M %p")

    # Update the countdown with the new exam information
    update_countdown(exam_datetime, exam_name)

    # Close the exam window
    exam_window.destroy()

# Function to add a new exam
def add_exam():
    # Create a new window for selecting the exam date and time
    exam_window = tk.Toplevel(root)
    exam_window.title("Add Exam")
    exam_window.config(bg="#000000")

    # Add a label and entry field for the exam name
    exam_name_label = tk.Label(exam_window, text="Exam Name:", fg="#FFFFFF", bg="#000000")
    exam_name_label.pack(pady=(10,0))
    exam_name_entry = tk.Entry(exam_window)
    exam_name_entry.pack()

    # Add a calendar for selecting the exam date
    exam_date_label = tk.Label(exam_window, text="Exam Date:", fg="#FFFFFF", bg="#000000")
    exam_date_label.pack(pady=(10,0))
    exam_date_picker = DateEntry(exam_window, date_pattern="yyyy-mm-dd")
    exam_date_picker.pack()

    # Add a dropdown menu for selecting the exam time
    exam_time_label = tk.Label(exam_window, text="Exam Time:", fg="#FFFFFF", bg="#000000")
    exam_time_label.pack(pady=(10,0))
    exam_time_picker = ttk.Combobox(exam_window, values=["{0:02d}:00 AM".format(i) for i in range(1, 13)] + ["{0:02d}:00 PM".format(i) for i in range(1, 13)], state="readonly")
    exam_time_picker.pack()

    # Add a button to save the exam information and close the window
    save_button = tk.Button(exam_window, text="Save", command=lambda: save_exam(exam_name_entry.get(), exam_date_picker.get(), exam_time_picker.get(), exam_window))
    save_button.pack(pady=(10,0))


# Add a button to open the window for adding a new exam
add_exam_button = tk.Button(root, text="Add Exam", font=("fenwick outline", 20), bg="#000000", fg="#FFFFFF", command=add_exam)
add_exam_button.pack(pady=(10,0))

# Run the main event loop
root.mainloop()




# Function to save exam information
def save_exam(exam_name, exam_date, exam_time, exam_window):
    # Combine the exam date and time into a datetime object
    exam_datetime_str = "{0} {1}".format(exam_date, exam_time)
    exam_datetime = datetime.strptime(exam_datetime_str, "%Y-%m-%d %I:%M %p")

    # Update the countdown with the new exam information
    update_countdown(exam_datetime, exam_name)

    # Close the exam window
    exam_window.destroy()

# Add a button to open the window for adding a new exam
add_exam_button = tk.Button(root, text="Add Exam", font=("fenwick outline", 20), bg="#000000", fg="#FFFFFF", command=add_exam)
add_exam_button.pack(pady=(10,0))

# Run the main event loop
root.mainloop()
