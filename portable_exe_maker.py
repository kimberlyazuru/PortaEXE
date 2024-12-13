import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Label, Entry, Button
import zipfile

class PortableEXEMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("PortaEXE - Portable EXE Maker")
        self.root.geometry("500x300")
        
        # Input fields for EXE and output folder
        Label(root, text="Executable File:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.exe_path = Entry(root, width=40)
        self.exe_path.grid(row=0, column=1, padx=10, pady=10)
        Button(root, text="Browse", command=self.browse_exe).grid(row=0, column=2, padx=10, pady=10)

        Label(root, text="Dependencies Folder (optional):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.dependencies_path = Entry(root, width=40)
        self.dependencies_path.grid(row=1, column=1, padx=10, pady=10)
        Button(root, text="Browse", command=self.browse_dependencies).grid(row=1, column=2, padx=10, pady=10)

        Label(root, text="Output Folder:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.output_path = Entry(root, width=40)
        self.output_path.grid(row=2, column=1, padx=10, pady=10)
        Button(root, text="Browse", command=self.browse_output).grid(row=2, column=2, padx=10, pady=10)

        # Create portable EXE button
        Button(root, text="Create Portable EXE", command=self.create_portable_exe).grid(row=3, column=0, columnspan=3, pady=20)

    def browse_exe(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
        if file_path:
            self.exe_path.delete(0, tk.END)
            self.exe_path.insert(0, file_path)

    def browse_dependencies(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.dependencies_path.delete(0, tk.END)
            self.dependencies_path.insert(0, folder_path)

    def browse_output(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, folder_path)

    def create_portable_exe(self):
        exe_file = self.exe_path.get()
        dependencies_folder = self.dependencies_path.get()
        output_folder = self.output_path.get()

        if not exe_file or not output_folder:
            messagebox.showerror("Error", "Please specify the EXE file and output folder.")
            return

        # Create the portable package
        try:
            portable_folder = os.path.join(output_folder, "Portable_EXE")
            if os.path.exists(portable_folder):
                shutil.rmtree(portable_folder)
            os.makedirs(portable_folder)

            # Copy EXE file
            shutil.copy(exe_file, portable_folder)

            # Copy dependencies, if provided
            if dependencies_folder and os.path.exists(dependencies_folder):
                deps_folder = os.path.join(portable_folder, "Dependencies")
                shutil.copytree(dependencies_folder, deps_folder)

            # Create ZIP package
            portable_zip = os.path.join(output_folder, "Portable_EXE.zip")
            with zipfile.ZipFile(portable_zip, 'w') as zipf:
                for root, dirs, files in os.walk(portable_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, portable_folder)
                        zipf.write(file_path, arcname)

            messagebox.showinfo("Success", f"Portable EXE created successfully at {portable_zip}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PortableEXEMaker(root)
    root.mainloop()
