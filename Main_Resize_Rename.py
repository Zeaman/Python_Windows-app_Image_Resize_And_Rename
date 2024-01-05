# Import required dependencies:
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def resize_images(source_folder, target_size):
    for folder_name in os.listdir(source_folder):
        folder_path = os.path.join(source_folder, folder_name)

        if os.path.isdir(folder_path):
            # Initialize a counter
            counter = 1

            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    image_path = os.path.join(folder_path, filename)

                    # Open image using PIL
                    original_image = Image.open(image_path)

                    # Resize image
                    resized_image = original_image.resize(target_size)

                    # Create a new name using the counter
                    new_image_name = f"{folder_name}_{counter}.jpg"

                    # Modify the destination path to include the folder
                    new_image_path = os.path.join(folder_path, new_image_name)

                    # Save resized image
                    resized_image.save(new_image_path)

                    # Increment the counter for the next file
                    counter += 1

    # Display a notice when all files are resized
    messagebox.showinfo("Success!", "All files have been successfully resized and saved in their respective folders.")

def close_window(root):
    root.destroy()

def get_user_input():
    root = tk.Tk()
    root.title("Resize and Rename Images")

    # Set the size of the window
    root.geometry("400x300")  # Width x Height

    def on_entry_click(event, entry_widget, default_text):
        if entry_widget.get() == default_text:
            entry_widget.delete(0, tk.END)
            entry_widget.config(fg="black")  # Change text color to black

    # Entry for source folder
    source_folder_label = tk.Label(root, text="Source Folder:")
    source_folder_label.pack()
    source_folder_default_text = "Enter source folder path"
    source_folder_entry = tk.Entry(root, fg="grey")
    source_folder_entry.insert(0, source_folder_default_text)
    source_folder_entry.bind("<FocusIn>",
                             lambda event: on_entry_click(event, source_folder_entry, source_folder_default_text))
    source_folder_entry.pack(pady=5)

    # Button to browse source directory
    browse_source_button = tk.Button(root, text="Browse Source", command=lambda: browse_directory(source_folder_entry))
    browse_source_button.pack(pady=5)  # vertical spacing

    # Entry for target width
    target_width_label = tk.Label(root, text="Target Width:")
    target_width_label.pack()
    target_width_entry = tk.Entry(root)
    target_width_entry.pack(pady=5)

    # Entry for target height
    target_height_label = tk.Label(root, text="Target Height:")
    target_height_label.pack()
    target_height_entry = tk.Entry(root)
    target_height_entry.pack(pady=5)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: resize_and_close(root, source_folder_entry,
                                                                                  target_width_entry, target_height_entry))
    submit_button.pack(pady=20)  # vertical spacing

    # Close button
    close_button = tk.Button(root, text="Close", command=lambda: close_window(root))
    close_button.pack(pady=10)

    root.mainloop()

def browse_directory(entry_widget):
    directory = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)  # Clear the entry widget
    entry_widget.insert(0, directory)  # Insert the selected directory into the entry widget

def resize_and_close(root, source_folder_entry, target_width_entry, target_height_entry):
    source_folder = source_folder_entry.get()
    target_width = int(target_width_entry.get())
    target_height = int(target_height_entry.get())
    target_size = (target_width, target_height)

    if source_folder:
        resize_images(source_folder, target_size)
        close_window(root)

# Get user input using Tkinter GUI
get_user_input()
