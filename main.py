import tkinter as tk
import os

def connect_to_wifi():
    wifi_name = ssid_entry.get()
    wifi_password = password_entry.get()
    command = f'sudo raspi-config nonint do_wifi_ssid_passphrase {wifi_name} {wifi_password}'
    os.system(command)

def select(value):
    global shift
    global spec
    global active_entry
    if not active_entry:  # if no Entry is active, we don't do anything
        return
    if value == "<-":
        txt = active_entry.get()
        active_entry.delete(0, tk.END)
        active_entry.insert(0, txt[:-1])
    elif value == "Shift":
        if shift:
            buttons(0, 0, button_values)
            shift = False
            spec = False
        else:
            buttons(0, 0, button_values_shift)
            shift = True
            spec = False
    elif value == "Spec":
        if spec:
            buttons(0, 0, button_values)
            spec = False
            shift = False
        else:
            buttons(0, 0, button_values_spec)
            spec = True
            shift = False
    else:
        active_entry.insert(tk.END, value)

def make_active(entry):
    global active_entry
    active_entry = entry

def cancel_command():
    root.destroy()

shift = False
spec = False
root = tk.Tk()

# Create frames
frame1 = tk.Frame(root)
frame1.pack()
frame2 = tk.Frame(root)
frame2.pack()

active_entry = None  # A global variable to keep track of the active Entry

ssid_label = tk.Label(frame1, text="Enter WiFi Name:")
ssid_label.grid(row=0, column=0)
ssid_entry = tk.Entry(frame1)
ssid_entry.grid(row=0, column=1)
ssid_entry.bind("<FocusIn>", lambda e: make_active(ssid_entry))  # make active when focused
ssid_entry.focus_set()

password_label = tk.Label(frame1, text="Enter WiFi Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(frame1)
password_entry.grid(row=1, column=1)
password_entry.bind("<FocusIn>", lambda e: make_active(password_entry))  # make active when focused

connect_button = tk.Button(frame1, text="Connect", command=connect_to_wifi)
connect_button.grid(row=2, column=0)

cancel_button = tk.Button(frame1, text="Cancel", command=cancel_command)  # cancel button
cancel_button.grid(row=2, column=1)

button_values = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','<-',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', ',', '.', '/', '-', ' ', 'Shift', 'Spec'
]
button_values_shift = [
    '+', '\"', '*', 'ç', '%', '&', '/', '(', ')', '?', '<-',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', ';', ':', '\\', '_', ' ', 'Shift', 'Spec'
]
button_values_spec = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '<-',
    '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '.',
    '/', ':', ';', '=', '?', '@', '[', ']', '^', '_', '`',
    '{', '|', '}', '~', '\\', 'ç', ' ', ' ', ' ', 'Shift', 'Spec'
]

row_val = 0
col_val = 0
BUTTON_WIDTH, BUTTON_HEIGHT = 4, 2  # specify the width and height

def buttons(row_val, col_val, button_vals):
    for button in button_vals:
        command = lambda x=button: select(x)
        if button == "<-":
            btn = tk.Button(frame2, text=button, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=command, bg='red')
            btn.grid(row=row_val, column=col_val, sticky="ew")
            col_val += 1
        elif button == "Shift":
            btn = tk.Button(frame2, text=button, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=command, bg='yellow')
            btn.grid(row=row_val, column=col_val, sticky="ew")
            col_val += 1
        elif button == "Spec":
            btn = tk.Button(frame2, text=button, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=command, bg='yellow')
            btn.grid(row=row_val, column=col_val, sticky="ew")
            col_val += 1
        else:
            btn = tk.Button(frame2, text=button, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=command)
            btn.grid(row=row_val, column=col_val, sticky="ew")
            col_val += 1

        if col_val > 10:
            col_val = 0
            row_val += 1

buttons(row_val, col_val, button_values)

root.title("Wifi Connect")
root.mainloop()