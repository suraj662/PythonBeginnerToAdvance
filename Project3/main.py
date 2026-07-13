#create a Text Editor application ----
# import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox, mainloop

#main window code--
root = tk.Tk()
root.title("My first GUI - Text Editor")
root.geometry("800x600")

#create text area--
text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Helvetica", 12),
    bg = "white",
    fg = "black"
)

text.pack(expand=True, fill="both")

#main logic starts now---
#function 1-create a new file
def new_file():
    text.delete("1.0", tk.END)

#function2 - open new file
def open_file():
    #open file dialog
    file_path = filedialog.askopenfilename(
       defaulttextextension = ".txt",
       fileType = [("Text Files", ".txt")]
    )

    if file_path:
        #open file
        with open(file_path, "r") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END , f.read())

#function3 - save the file
def save_file():
    #open save file dialogue
    file_path= filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved successfully")

# Create Menu Bar
menu= tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)

# New, Open File, Save , Exit

# add filemenu to menu bar
menu.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)



#starts and keep the window
root.mainloop()
