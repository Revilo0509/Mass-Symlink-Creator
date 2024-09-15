import customtkinter
from tkinter import filedialog

#-----------------GUI Functions-----------------

def BrowseFile(FileEntry):
    file_path = filedialog.askopenfilename()
    if file_path:
        FileEntry.delete(0, customtkinter.END)
        FileEntry.insert(0, file_path)

#-----------------GUI-----------------

Root = customtkinter.CTk()

Frame = customtkinter.CTkFrame(master=Root)
Frame.pack(pady=20, padx=20, fill="both", expand=True)


#FILE INPUT 1

FileInputLabel1 = customtkinter.CTkLabel(master=Frame, text="File 1:")
FileInputLabel1.pack(pady=10, padx=10)

FileInput1 = customtkinter.CTkEntry(master=Frame)
FileInput1.pack(pady=10, padx=10)

BrowseButton1 = customtkinter.CTkButton(master=Frame, text="Browse", command=lambda: BrowseFile(FileInput1))
BrowseButton1.pack(pady=10, padx=10)


#FILE INPUT 2

FileInputLabel2 = customtkinter.CTkLabel(master=Frame, text="File 2:")
FileInputLabel2.pack(pady=10, padx=10)

FileInput2 = customtkinter.CTkEntry(master=Frame)
FileInput2.pack(pady=10, padx=10)

BrowseButton2 = customtkinter.CTkButton(master=Frame, text="Browse", command=lambda: BrowseFile(FileInput2))
BrowseButton2.pack(pady=10, padx=10)

Root.mainloop()


print("GUI Loaded")