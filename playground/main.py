import socket
import subprocess
import json
from tkinter import *
from functools import partial
from tkinter import messagebox

DEEP_BLUE = "#004080"
ACCENT_ORANGE = "#ffa500"
STEEL_GREY = "#9a9a9a"
CHARCOAL = "#333333"
SKY_BLUE = "#87ceeb"
ACCENT_GREEN = "#00b33c"


def run_ps(powershell_script, expect_json=True):
    try:
        process = subprocess.Popen(
            ["powershell", "-ExecutionPolicy", "Bypass", "-Command", powershell_script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            messagebox.showerror(title="PowerShell Error",
                                 message=f"PowerShell command failed with return code {process.returncode}")
            return None

        if expect_json:
            try:
                return json.loads(stdout)
            except json.JSONDecodeError as json_error:
                messagebox.showinfo(title="JSONDecode ERROR", message=str(json_error))
                return None
        else:
            return stdout

    except Exception as ex:
        messagebox.showerror(title="Error:", message=str(ex))
        return None


def get_ip_by_hostname():
    hostname = hostname_entry.get().strip()
    try:
        ip_address = socket.gethostbyname(hostname)
        print(ip_address)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None


def get_hostname_by_ip():
    ip_addr = ip_entry.get().strip()
    print(ip_addr)
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_addr)
        print(socket.gethostbyaddr(ip_addr))
        print(hostname)
        return hostname
    except socket.herror as e:
        print(f"Error: {e}")
        return None


window = Tk()
window.title("NetOpsAssistant")
window.config(bg=DEEP_BLUE, pady=10, padx=20)

# LOOK UP SECTION =============================================================================================
lookup_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                             highlightbackground=ACCENT_ORANGE)
lookup_section_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

hostname_entry = Entry(lookup_section_frame, width=30)
hostname_entry.config(highlightthickness=2, highlightcolor=STEEL_GREY, justify="left")
hostname_entry.grid(row=0, column=0, pady=5, padx=5)

search_by_hostname_btn = Button(lookup_section_frame, text="Search Host", width=29, bg=CHARCOAL, fg="white",
                                command=get_ip_by_hostname)
search_by_hostname_btn.config(font=("Arial", 9, "bold"))
search_by_hostname_btn.grid(row=0, column=1, pady=5, padx=2)

ip_entry = Entry(lookup_section_frame, width=30)
ip_entry.focus()
ip_entry.config(highlightthickness=2, highlightcolor=STEEL_GREY, justify="left")
ip_entry.grid(row=1, column=0, pady=5, padx=5)

search_by_ip_btn = Button(lookup_section_frame, text="Search IP", width=29, bg=CHARCOAL, fg="white",
                          command=get_hostname_by_ip)
search_by_ip_btn.config(font=("Arial", 9, "bold"))
search_by_ip_btn.grid(row=1, column=1, pady=5, padx=2)

# COMMAND SECTION =============================================================================================
command_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                              highlightbackground=ACCENT_ORANGE)
command_section_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

# DELETE USER SECTION =============================================================================================
delete_user_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                                  highlightbackground=ACCENT_ORANGE)
delete_user_section_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

window.mainloop()
