import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog

def safe_move(src, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    base = os.path.basename(src)
    name, ext = os.path.splitext(base)
    candidate = os.path.join(dst_dir, base)
    counter = 1
    while os.path.exists(candidate):
        candidate = os.path.join(dst_dir, f"{name} ({counter}){ext}")
        counter += 1
    shutil.move(src, candidate)

def organize_by_extension(folder_path):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Path does not exist!")
        return
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Please select a folder.")
        return

    moved_count = 0
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isdir(file_path):
            continue
        ext = os.path.splitext(file_name)[1][1:].lower()
        if not ext:
            ext = "no_extension"
        dest_dir = os.path.join(folder_path, ext)
        safe_move(file_path, dest_dir)
        moved_count += 1

    messagebox.showinfo("Done", f"✅ Organized {moved_count} files by extension.")

def on_submit():
    path = entry.get().strip('"')
    organize_by_extension(path)

def on_browse():
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)

# GUI setup
root = tk.Tk()
root.title("Folder Organizer by Extension")
root.geometry("500x150")
root.resizable(False, False)

label = tk.Label(root, text="Paste Folder Path or Browse:")
label.pack(pady=5)

entry = tk.Entry(root, width=55)
entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse...", command=on_browse)
browse_btn.pack(pady=2)

organize_btn = tk.Button(root, text="Organize", command=on_submit)
organize_btn.pack(pady=10)

root.mainloop()
