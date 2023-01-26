import customtkinter

import sender


class ExampleApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # self.customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        # self.customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        self.button_send = None
        self.button_select = None
        self.label_1 = None
        self.frame_secondframe = None
        self.file = None
        self.window = None

        self.geometry("580x300")
        self.title("PCtoPI-STP")

        self.frame_mainframe = customtkinter.CTkFrame(master=self)
        self.frame_mainframe.pack(pady=20, padx=60, fill="both", expand=True)

        self.entry_host = customtkinter.CTkEntry(master=self.frame_mainframe, placeholder_text="Host")
        self.entry_host.pack(padx=20, pady=10)

        self.entry_username = customtkinter.CTkEntry(master=self.frame_mainframe, placeholder_text="Username")
        self.entry_username.pack(padx=20, pady=10)

        self.entry_password = customtkinter.CTkEntry(master=self.frame_mainframe, show='*',
                                                     placeholder_text="Password", )
        self.entry_password.pack(padx=20, pady=10)

        self.entry_destpath = customtkinter.CTkEntry(master=self.frame_mainframe,
                                                     placeholder_text="Destination Directory")
        self.entry_destpath.pack(padx=20, pady=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_mainframe, text="Set", command=self.button_settings)
        self.button_1.pack(pady=10, padx=10)

    def button_settings(self):
        self.withdraw()
        self.window = customtkinter.CTkToplevel(self)
        self.window.geometry("400x200")
        self.window.protocol("WM_DELETE_WINDOW", self.callback)

        self.frame_secondframe = customtkinter.CTkFrame(master=self.window)
        self.frame_secondframe.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_secondframe, text="File: ",
                                              justify=customtkinter.LEFT)
        self.label_1.pack(pady=10, padx=10)

        self.button_select = customtkinter.CTkButton(master=self.frame_secondframe, text="Select File",
                                                     command=self.open_files)
        self.button_select.pack(pady=10, padx=10)

        self.button_send = customtkinter.CTkButton(master=self.frame_secondframe, text="Send Video", state='disabled',
                                                   command=sender.send_video)
        self.button_send.pack(pady=10, padx=10)

    def open_files(self):
        ask_file = customtkinter.filedialog.askopenfile()
        self.file = ask_file
        if len(ask_file.name) >= 0:
            self.label_1.configure(text="File: " + self.file.name)
            self.button_send.configure(state="normal")

    def callback(self):
        self.window.destroy()
        self.deiconify()


app = ExampleApp()
app.mainloop()

