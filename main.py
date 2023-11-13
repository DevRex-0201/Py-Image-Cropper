# Import necessary libraries
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Class definition for the ImageProcessor
class ImageProcessor:
    # Constructor method, initializes the GUI and variables
    def __init__(self, root):
        # Set the root window
        self.root = root
        # Set the title of the window
        self.root.title("Image Processor")

        # Variables to store user inputs
        self.folder_path = tk.StringVar()  # Path of the folder containing images
        self.result_file_prefix = tk.StringVar()  # Prefix for result file names
        self.cropped_height = tk.StringVar()  # Height to be cropped from images
        self.image_count = tk.StringVar()  # Number of images to process

        # UI Elements

        # Labels and Entry widgets for folder path
        self.label_folder = tk.Label(root, text="Folder Path:")
        self.entry_folder = tk.Entry(root, textvariable=self.folder_path)
        self.button_browse = tk.Button(root, text="Browse", command=self.browse_folder)

        # Labels and Entry widgets for result file prefix
        self.label_prefix = tk.Label(root, text="Result File Prefix:")
        self.entry_prefix = tk.Entry(root, textvariable=self.result_file_prefix)

        # Labels and Entry widgets for cropped height
        self.label_cropped_height = tk.Label(root, text="Cropped Height:")
        self.entry_cropped_height = tk.Entry(root, textvariable=self.cropped_height)

        # Labels and Entry widgets for image count
        self.label_image_count = tk.Label(root, text="Image Count:")
        self.entry_image_count = tk.Entry(root, textvariable=self.image_count)

        # Button to trigger image processing
        self.button_process = tk.Button(root, text="Process Images", command=self.process_images)

        # Layout - Grid layout to organize the UI elements
        self.label_folder.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.entry_folder.grid(row=0, column=1, columnspan=2, pady=5)
        self.button_browse.grid(row=0, column=3, pady=5)

        self.label_prefix.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.entry_prefix.grid(row=1, column=1, columnspan=2, pady=5)

        self.label_cropped_height.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.entry_cropped_height.grid(row=2, column=1, columnspan=2, pady=5)

        self.label_image_count.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.entry_image_count.grid(row=3, column=1, columnspan=2, pady=5)

        self.button_process.grid(row=4, column=0, columnspan=4, pady=10)

    # Method to handle browsing for a folder
    def browse_folder(self):
        # Open a dialog to select a folder and set the selected path to the variable
        folder_selected = filedialog.askdirectory(title="Select Folder")
        if folder_selected:
            self.folder_path.set(folder_selected)

    # Method to process images based on user inputs
    def process_images(self):
        # Get user inputs from the GUI
        folder_path = self.folder_path.get()
        result_prefix = self.result_file_prefix.get()
        cropped_height = int(self.cropped_height.get())
        image_count = int(self.image_count.get()) if self.image_count.get() else None

        # Check if the folder path exists
        if not os.path.exists(folder_path):
            messagebox.showerror("Error", "Invalid folder path.")
            return

        # Loop through each file in the selected folder
        for filename in os.listdir(folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Build the full path of the input image
                input_path = os.path.join(folder_path, filename)

                # Open the image using PIL
                img = Image.open(input_path)

                # Convert the image to RGBA
                img = img.convert('RGB')

                # Crop the bottom part of the image
                img = img.crop((0, 0, img.width, img.height - cropped_height))

                # Resize the image to a new height while maintaining the aspect ratio
                new_height = 800
                ratio = new_height / img.height
                new_width = int(img.width * ratio)
                img = img.resize((new_width, new_height), Image.BILINEAR)

                # Save the processed image as JPEG with a new filename
                output_filename = f"{result_prefix}_{filename}"
                output_path = os.path.join("output/", output_filename)
                img.save(output_path, format="JPEG")

                # Update image count if specified
                if image_count is not None:
                    image_count -= 1
                    if image_count <= 0:
                        break

        # Display a success message
        messagebox.showinfo("Success", "Images processed successfully!")

# Main block - create a Tkinter root window and the ImageProcessor instance
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessor(root)
    root.mainloop()
