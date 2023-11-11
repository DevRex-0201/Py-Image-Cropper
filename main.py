import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        # Variables
        self.folder_path = tk.StringVar()
        self.result_file_prefix = tk.StringVar()
        self.cropped_height = tk.StringVar()
        self.image_count = tk.StringVar()

        # UI Elements
        self.label_folder = tk.Label(root, text="Folder Path:")
        self.entry_folder = tk.Entry(root, textvariable=self.folder_path)
        self.button_browse = tk.Button(root, text="Browse", command=self.browse_folder)

        self.label_prefix = tk.Label(root, text="Result File Prefix:")
        self.entry_prefix = tk.Entry(root, textvariable=self.result_file_prefix)

        self.label_cropped_height = tk.Label(root, text="Cropped Height:")
        self.entry_cropped_height = tk.Entry(root, textvariable=self.cropped_height)

        self.label_image_count = tk.Label(root, text="Image Count:")
        self.entry_image_count = tk.Entry(root, textvariable=self.image_count)

        self.button_process = tk.Button(root, text="Process Images", command=self.process_images)

        # Layout
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

    def browse_folder(self):
        folder_selected = filedialog.askdirectory(title="Select Folder")
        if folder_selected:
            self.folder_path.set(folder_selected)

    def process_images(self):
        folder_path = self.folder_path.get()
        result_prefix = self.result_file_prefix.get()
        cropped_height = int(self.cropped_height.get())
        image_count = int(self.image_count.get()) if self.image_count.get() else None

        if not os.path.exists(folder_path):
            messagebox.showerror("Error", "Invalid folder path.")
            return

        for filename in os.listdir(folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(folder_path, filename)

                # Open image
                img = Image.open(input_path)

                # Crop bottom part
                img = img.crop((0, 0, img.width, img.height - cropped_height))

                # Resize
                new_height = 800
                ratio = new_height / img.height
                new_width = int(img.width * ratio)
                img = img.resize((new_width, new_height), Image.BILINEAR )

                # Save as JPEG
                output_filename = f"{result_prefix}_{filename}"
                output_path = os.path.join("output/", output_filename)
                img.save(output_path, format="JPEG")

                # Update image count
                if image_count is not None:
                    image_count -= 1
                    if image_count <= 0:
                        break

        messagebox.showinfo("Success", "Images processed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessor(root)
    root.mainloop()
