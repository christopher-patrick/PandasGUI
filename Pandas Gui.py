import customtkinter
import pandas as pd

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set size of window
        self.geometry("500x300")
        self.title("Pandas Gui")
        self.minsize(400, 200)

        # Set the grid config
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Frame that occupies textbox space before selection
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        # Starting variable for the option menu dropdown
        self.variable = customtkinter.StringVar()
        self.variable.set("Select Requirements")

        # Option menu with selections and positioning
        self.opt_menu = customtkinter.CTkOptionMenu(master=self, variable=self.variable, values=["App Gateway", "Key Vault", "Azure Blob Storage"], command=self.option_menu_select)
        self.opt_menu.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

    def option_menu_select(self, choice):
        if choice == self.opt_menu._values[0]:

            # Read the Q2_excel file that you provide and select the App Gateway sheet
            self.dfA = pd.read_excel(r"C:\Users\Christopher_Patrick\OneDrive - Edwards Lifesciences\Desktop\Capability_Q2_RequirementsLibrary.xlsx", sheet_name="App Gateway")


            # Create the textbox with excel information to fit inside the frame created in the __init__ function
            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", self.dfA.to_records())
            self.textbox.configure(state="disabled")

            self.variable2 = customtkinter.StringVar()
            self.variable2.set("Select Instance")

            self.opt_menu2 = customtkinter.CTkOptionMenu(master=self, variable=self.variable2, values=["VNV", "FVNV", "Galaxy"], command=self.option_menu_filter_AG)
            self.opt_menu2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        elif choice == self.opt_menu._values[1]:

            # Read the Q2_excel file that you provide and select the Key Vault sheet
            self.dfK = pd.read_excel(r"C:\Users\Christopher_Patrick\OneDrive - Edwards Lifesciences\Desktop\Capability_Q2_RequirementsLibrary.xlsx", sheet_name="Key Vault")

            # Create the textbox with excel information to fit inside the frame created in the __init__ function
            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", self.dfK.to_records())
            self.textbox.configure(state="disabled")

            self.variable2 = customtkinter.StringVar()
            self.variable2.set("Select Instance")

            self.opt_menu2 = customtkinter.CTkOptionMenu(master=self, variable=self.variable2, values=["VNV", "FVNV", "Galaxy"], command=self.option_menu_filter_KV)
            self.opt_menu2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        elif choice == self.opt_menu._values[2]:

            # Read the Q2_excel file that you provide and select the Azure Blob Storage sheet
            self.dfB = pd.read_excel(r"C:\Users\Christopher_Patrick\OneDrive - Edwards Lifesciences\Desktop\Capability_Q2_RequirementsLibrary.xlsx", sheet_name="Azure Blob Storage")

            # Create the textbox with excel information to fit inside the frame created in the __init__ function
            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", self.dfB.to_records())
            self.textbox.configure(state="disabled")
    
            self.variable2 = customtkinter.StringVar()
            self.variable2.set("Select Instance")

            self.opt_menu2 = customtkinter.CTkOptionMenu(master=self, variable=self.variable2, values=["VNV", "FVNV", "Galaxy"], command=self.option_menu_filter_Blob)
            self.opt_menu2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def option_menu_filter_AG(self, filter):
        if filter == "VNV":
            pdf_filter1 = self.dfA.query("Instance == 'VNV'")


            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")
        elif filter == "FVNV":
            pdf_filter1 = self.dfA.query("Instance == 'FVNV'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")
        elif filter == "Galaxy":
            pdf_filter1 = self.dfA.query("Instance == 'Galaxy'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")

    def option_menu_filter_KV(self, filter):
        if filter == "VNV":
            pdf_filter1 = self.dfK.query("Instance == 'VNV'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")
        elif filter == "FVNV":
            pdf_filter1 = self.dfK.query("Instance == 'FVNV'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")
        elif filter == "Galaxy":
            pdf_filter1 = self.dfK.query("Instance == 'Galaxy'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")
        
    def option_menu_filter_Blob(self, filter):
        if filter == "VNV":
            pdf_filter1 = self.dfB.query("Instance == 'VNV'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")
        elif filter == "FVNV":
            pdf_filter1 = self.dfB.query("Instance == 'FVNV'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")
        elif filter == "Galaxy":
            pdf_filter1 = self.dfB.query("Instance == 'Galaxy'")

            self.textbox = customtkinter.CTkTextbox(master=self, state="disabled")
            self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", pdf_filter1.to_records())
            self.textbox.configure(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()