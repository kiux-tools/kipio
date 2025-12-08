#!/usr/bin/env python3
"""
Basic Kipio Usage - Enhanced I/O operations
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_

def main():
    print_("=" * 50)
    print_("KIPIO DEMO: Basic Usage", timestamp=True)
    print_("=" * 50)
    
    # Simple input with validation
    name = input_("Enter your name: ", required=True, strip=True)
    
    # Input with choices
    role = input_("Select your role: ", 
                  choices=["admin", "user", "guest"],
                  show_choices=True,
                  default="user")
    
    # Enhanced output
    print_("\n" + "=" * 50)
    print_(f"Welcome, {name}!", timestamp=True, flush=True)
    print_(f"Role: {role}")
    print_("Registration completed successfully!")
    print_("=" * 50)

if __name__ == "__main__":
    main()
