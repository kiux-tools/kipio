#!/usr/bin/env python3
"""
Security Features Demo - Password handling and secure input
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_

def secure_login():
    print_("SECURE LOGIN SYSTEM", timestamp=True)
    print_("-" * 40)
    
    # Hidden password input with custom mask
    username = input_("Username: ", required=True)
    password = input_("Password: ", 
                      hidden=True, 
                      mask_char="•",
                      required=True)
    
    # Confirm password
    confirm = input_("Confirm password: ", 
                     hidden=True, 
                     mask_char="•",
                     required=True)
    
    if password != confirm:
        print_("Passwords do not match!", file="security.log", mode="a")
        return False
    
    # Log the attempt (without password)
    print_(f"Login attempt by: {username}", 
           file="security.log", 
           mode="a",
           timestamp=True,
           silent=True)
    
    print_("Login credentials accepted")
    return True

if __name__ == "__main__":
    secure_login()
