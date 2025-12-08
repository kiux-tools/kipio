#!/usr/bin/env python3
"""
CLI Application Demo - Full command-line interface
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_

def cli_menu():
    while True:
        print_("\n" + "=" * 50)
        print_("MAIN MENU", timestamp=True)
        print_("=" * 50)
        print_("1. User Registration")
        print_("2. File Operations")
        print_("3. System Info")
        print_("4. Exit")
        
        choice = input_("Select option (1-4): ", 
                       choices=["1", "2", "3", "4"],
                       required=True)
        
        if choice == "1":
            register_user()
        elif choice == "2":
            file_operations()
        elif choice == "3":
            system_info()
        elif choice == "4":
            print_("Goodbye!", timestamp=True, flush=True)
            sys.exit(0)

def register_user():
    print_("\nUSER REGISTRATION")
    name = input_("Full name: ", required=True)
    email = input_("Email: ", required=True)
    
    print_(f"Registered: {name} <{email}>", 
           file="users.log", 
           mode="a",
           timestamp=True)

def file_operations():
    print_("\nFILE OPERATIONS")
    action = input_("Action (read/write/append): ",
                   choices=["read", "write", "append"],
                   default="read")
    
    if action == "read":
        content = print_("", file="demo.txt", mode="r", return_string=True)
        print_(f"Content:\n{content}")
    else:
        text = input_("Enter text: ")
        print_(text, file="demo.txt", mode=action[0])  # 'w' or 'a'

def system_info():
    import platform
    print_("\nSYSTEM INFORMATION")
    print_(f"Python: {platform.python_version()}")
    print_(f"OS: {platform.system()} {platform.release()}")
    print_(f"Kipio: Import successful", timestamp=True)

if __name__ == "__main__":
    cli_menu()
