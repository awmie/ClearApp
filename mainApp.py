import os
import shutil
from tkinter import *
import tkinter as tk
from getpass import getpass
import subprocess

def clear_mac_cache():
    cache_folders = [
        "~/Library/Caches",
        "~/Library/Preferences",
        "~/Library/Saved Application State"
    ]
    
    for folder in cache_folders:
        folder_path = os.path.expanduser(folder)
        try:
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                print(f"Deleted contents of {folder_path}")
            else:
                print(f"{folder_path} does not exist")
        except Exception as e:
            print(f"Error occurred while clearing cache: {str(e)}")
            return

def clearRam():
    command = 'sudo purge'
    try:
        subprocess.call(['osascript', '-e', f'tell app "Terminal" to do script "{command}"'])
        print(f"Opened Terminal and wrote command successfully: {command}")
    except Exception as e:
        print(f"Error occurred while clearing RAM: {str(e)}")
        return


def clear_cache_and_ram():
    clear_mac_cache()
    clearRam()

# Tkinter GUI
def clear_cache():
    clear_mac_cache()

def clear_ram():
    clearRam()


root = Tk()

root.title("Clear Cache and RAM")
root.geometry("300x200")

# Center the window on the screen
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Set the window icon
img = tk.PhotoImage(file='icon.gif')
root.iconphoto(True, img)

cache_button = tk.Button(root, text="Clear Cache", command=clear_cache)
cache_button.pack(pady=10)

ram_button = tk.Button(root, text="Clear RAM", command=clear_ram)
ram_button.pack(pady=10)

cache_ram_button = tk.Button(root, text="Clear Cache and RAM", command=clear_cache_and_ram)
cache_ram_button.pack(pady=10)

root.mainloop()
