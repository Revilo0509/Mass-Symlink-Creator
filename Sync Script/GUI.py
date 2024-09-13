import customtkinter

#-----------------GUI-----------------

root = customtkinter.CTk()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

root.mainloop()


print("GUI Loaded")