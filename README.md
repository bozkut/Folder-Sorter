📂 Folder-Sorter

Folder Sorter is a lightweight Python GUI tool that organizes files into subfolders by their extension.Paste or browse a folder path, and it instantly sorts files into neatly named directories.Simple, fast, and portable — can be run via Python or as a standalone Windows .exe built with PyInstaller.

📥 Installation & Usage

Option 1 – Windows EXE (No Python required)

Go to the Releases page.

Download folder_sorter.zip from the Assets section.

Extract the .zip file to any folder.

Double-click folder_sorter.exe to launch the app.

Paste a folder path or click Browse to select one, then click Organize.

Option 2 – Run with Python

Make sure you have Python 3.9+ installed.Download Python

Clone or download this repository:

git clone https://github.com/bozkut/Folder-Sorter.git
cd Folder-Sorter

If you want to create the .exe yourself:
pip install pyinstaller
pyinstaller --onefile --noconsole folder_sorter.py
