import customtkinter

import sender


class ExampleApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        #self.customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        #self.customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        self.file = ''
        self.window = ''

        self.geometry("580x300")
        self.title("PCtoPI-STP")

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.entry_host = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Host")
        self.entry_host.pack(padx=20, pady=10)

        self.entry_username = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Username")
        self.entry_username.pack(padx=20, pady=10)

        self.entry_password = customtkinter.CTkEntry(master=self.frame_1, show='*', placeholder_text="Password", )
        self.entry_password.pack(padx=20, pady=10)

        self.entry_destpath = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Destination Directory")
        self.entry_destpath.pack(padx=20, pady=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_1, text="Set", command=self.button_settings)
        self.button_1.pack(pady=10, padx=10)

    def button_settings(self):

        self.window = customtkinter.CTkToplevel(self)
        self.window.geometry("400x200")

        frame_1 = customtkinter.CTkFrame(master=self.window)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, text="File: ", justify=customtkinter.LEFT)
        label_1.pack(pady=10, padx=10)

        button_2 = customtkinter.CTkButton(master=frame_1, text="Select File", command=self.open_files)
        button_2.pack(pady=10, padx=10)

        button_1 = customtkinter.CTkButton(master=frame_1, text="Send Video", state='disabled',
                                           command=sender.send_video)
        button_1.pack(pady=10, padx=10)

    def open_files(self):
        ask_file = customtkinter.filedialog.askopenfile()
        self.file = ask_file



app = ExampleApp()
app.mainloop()
