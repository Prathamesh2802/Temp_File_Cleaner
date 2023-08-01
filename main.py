import tkinter
import customtkinter
import tempfile
import os


def temp():
    try:
        temp_directory = tempfile.gettempdir()
        for root, _, files in os.walk(temp_directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"{(file_path)} +removed")
                except Exception as e:
                    print(f"Failed to Delete {(file_path)} Error {(e)}")
        print("Successfully Cleared the Files from "+temp_directory)
    except Exception as e:
        print(f"Error: ({e})")


def prefetch():
    try:
        prefetch_directory = r"C:\\Windows\\Prefetch"
        for root, _, files in os.walk(prefetch_directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete: {file_path}, Error: {e}")

        print(f"Successfully cleared contents of {prefetch_directory}")
    except Exception as e:
        print(f"Error clearing Prefetch directory: {e}")


def windowtemp():
    try:
        windows_temp_directory = r"C:\\Windows\\Temp"
        for root, _, files in os.walk(windows_temp_directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete: {file_path}, Error: {e}")

        print(f"Successfully cleared contents of {windows_temp_directory}")
    except Exception as e:
        print(f"Error clearing Windows Temp directory: {e}")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x200")
app.title("Temp File Cleaner")


# Add Ui Elements

title = customtkinter.CTkLabel(
    app, text="Select which Folder which you want to Clear")
title.pack(padx=10, pady=10)


# Folder Options

link1 = customtkinter.CTkButton(
    app, text="Local Temp", hover_color="blue", fg_color="coral", command=temp)
link1.pack()


link2 = customtkinter.CTkButton(
    app, text="Prefetch", hover_color="Grey", fg_color="coral", command=prefetch)
link2.pack(padx=15, pady=12)

link3 = customtkinter.CTkButton(
    app, text="Windows Temp", fg_color="coral", hover_color="red", command=windowtemp)
link3.pack()

# Run App

app.mainloop()
