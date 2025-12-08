#!/usr/bin/env python3
"""
File Operations Demo - Reading and writing files
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_
def file_demo():
    print_("FILE OPERATIONS DEMO", timestamp=True)
    
    # Create a new file
    print_("Creating 'demo.txt'...")
    username = input_("Your name: ", required=True)
    password = input_("Your password: ", hidden=True, default="1234")
    message = input_("Your message: ", default="test")
    print_(f"user: {username}", file="demo.txt", mode="w")
    print_(f"password: {password}", file="demo.txt", mode="a")
    print_(f"message: {message}", file="demo.txt", mode="a")
    
    # Read from file using print_ in read mode
    try:
        content = print_(file="demo.txt", mode="r")
        print_("\nFile Contents:")
        print_(content, silent=False)
    except Exception as e:
        print_(f"Error reading file: {e}")
    
    # Silent logging
    print_("Operation completed", 
           file="app.log", 
           mode="a", 
           timestamp=True,
           silent=True)
    
    # Cleanup
    if os.path.exists("demo.txt"):
        os.remove("demo.txt")
    
    print_("File operations completed")

if __name__ == "__main__":
    file_demo()
