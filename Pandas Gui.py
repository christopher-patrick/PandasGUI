import customtkinter
import pandas as pd

def option_menu_select(choice):
    if choice == opt_values[0]:
        # Load the CSV file for "Application Gateway"
        df = pd.read_excel(r"C:\Users\Christopher\Desktop\Capability_Q2_RequirementsLibrary.xlsx", sheet_name="App Gateway")

        # Create textbox with AppGateway data
        text_widget = customtkinter.CTkTextbox(app, state="disabled", height=350, width=900)
        text_widget.grid(row=1, column=0, padx=20, pady=10)
        text_widget.configure(state="normal")
        text_widget.insert("0.0", df)
        text_widget.configure(state="disabled")

    elif choice == opt_values[1]:
        # Load the CSV file for "Application Gateway"
        df = pd.read_excel(r"C:\Users\Christopher\Desktop\Capability_Q2_RequirementsLibrary.xlsx", sheet_name="Key Vault")

        # Create textbox with AppGateway data
        text_widget = customtkinter.CTkTextbox(app, state="disabled", height=350, width=900)
        text_widget.grid(row=1, column=0, padx=20, pady=10)
        text_widget.configure(state="normal")
        text_widget.insert("0.0", df)
        text_widget.configure(state="disabled")
    elif choice == opt_values[2]:
        # Load the CSV file for "Application Gateway"
        df = pd.read_excel(r"C:\Users\Christopher\Desktop\Capability_Q2_RequirementsLibrary.xlsx", sheet_name="Azure Blob Storage")

        # Create textbox with AppGateway data
        text_widget = customtkinter.CTkTextbox(app, state="disabled", height=350, width=900)
        text_widget.grid(row=1, column=0, padx=20, pady=10)
        text_widget.configure(state="normal")
        text_widget.insert("0.0", df)
        text_widget.configure(state="disabled")

app = customtkinter.CTk()
app.title("Pandas Gui")
app.geometry("950x500")



opt_values = ["Application Gateway", "Key Vault", "Azure Blob Storage"]
variable = customtkinter.StringVar()
variable.set("Select Requirements")

optionmenu = customtkinter.CTkOptionMenu(app, variable=variable, values=opt_values, command=option_menu_select)
optionmenu.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()
