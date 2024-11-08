import curses
import platform

# Function to display the banner
def display_banner(stdscr):
    stdscr.clear()
    banner = """
 .S    S.    .S_SSSs     .S S.   
.SS    SS.  .SS~SSSSS   .SS SS.  
S%S    S%S  S%S   SSSS  S%S S%S  
S%S    S%S  S%S    S%S  S%S S%S  
S%S SSSS%S  S%S SSSS%S  S%S S%S  
S&S  SSS&S  S&S  SSS%S   SS SS   
S&S    S&S  S&S    S&S    S_S    
S&S    S&S  S&S    S&S   SS~SS   
S*S    S*S  S*S    S&S  S*S S*S  
S*S    S*S  S*S    S*S  S*S S*S  
S*S    S*S  S*S    S*S  S*S S*S  
SSS    S*S  SSS    S*S  S*S S*S  
       SP          SP   SP       
       Y           Y    Y        

Halfhide's Admin eXtension
By Jonathan Halfhide
    """
stdscr.addstr(0, 0, banner)
    stdscr.refresh()

# Function to display a menu with options
def display_menu(stdscr, title, options):
    display_banner(stdscr)
    # Adjust the starting line for the menu based on the banner heig>
    start_line = 19  # Start a few lines below the banner
    stdscr.addstr(start_line, 0, title)
    for idx, option in enumerate(options):
        stdscr.addstr(start_line + 2 + idx, 2, f"{idx + 1}. {option}>
    stdscr.addstr(start_line + 2 + len(options) + 1, 0, "Select an o>
    stdscr.refresh()

# Main menu function
def main_menu(stdscr):
    main_options = [
        "System Overview", "Storage", "Networking", "Memory", 
        "CPU", "Services", "Security", "Logs", "Updates"
    ]
    while True:
        display_menu(stdscr, "Main Menu - Select an option below:", >
        key = stdscr.getch()

        if key == ord('q'):
            break
elif key == ord('1'):
            submenu(stdscr, "System Overview", system_overview_optio>
        elif key == ord('2'):
            submenu(stdscr, "Storage", storage_options)
        elif key == ord('3'):
            submenu(stdscr, "Networking", networking_options)
        # Add more elif cases for other options here

# Submenu options
system_overview_options = [
    "System Information", "Hardware Summary", "User and Session Info>
    "Process Overview", "Load Averages"
]
storage_options = [
    "Disk Usage", "Largest Files", "Disk Health Check", "Mount Point>
]
networking_options = [
    "Network Interfaces", "Bandwidth Usage", "Active Connections", 
    "Packet Loss and Latency", "Firewall Status", "DNS Resolution"
]
memory_options = [
    "Memory Usage", "Swap Usage", "Top Memory Consumers",
    "OOM (Out of Memory) History", "Clear Cache"
]
cpu_options = [
    "CPU Load", "Top CPU Consumers", "Interrupts and Context Switche>
    "CPU Frequency Scaling"
]
services_options = [
    "Service Status", "Start/Stop/Restart Services",
    "Failed Services Log", "Scheduled Tasks"
]
security_options = [
    "Firewall Rules", "SSH Status and Configuration",
    "User Permissions", "Password Policy", "Open Ports", "Audit Logs"
]
logs_options = [
    "System Logs", "Application Logs"
]
updates_options = [
    "Update Status", "Patch Management", "Kernel Updates"
]
# Define other submenus (memory, CPU, services, etc.) similarly

# Submenu handler
def submenu(stdscr, title, options):
    while True:
        display_menu(stdscr, title, options)
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('1'):
            # Call function to perform the action for the first subm>
            display_info(stdscr, "System Information", get_system_in>
        # Add more elif cases for other options in the submenu here

# Example functions to get system information
def get_system_info():
    uname = platform.uname()
    return f"OS: {uname.system} {uname.release}\nKernel: {uname.vers>

def display_info(stdscr, title, info):
    display_banner(stdscr)
    stdscr.addstr(19, 0, title)  # Adjusted to start below the banner
    stdscr.addstr(21, 0, info)
    stdscr.addstr(23, 0, "Press any key to go back")
    stdscr.refresh()
    stdscr.getch()

# Entry point
def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    main_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)