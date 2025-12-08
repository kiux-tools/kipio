#!/usr/bin/env python3
"""
Advanced Features Demo - All Kipio capabilities
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_

def advanced_demo():
    print_("ADVANCED KIPIO FEATURES", timestamp=True)
    print_("=" * 60)
    
    # 1. Bytes output
    print_("\n1. Bytes Output Demo:")
    data = print_("Hello in bytes", _bytes_=True, return_string=True)
    print_(f"Bytes output: {data}")
    
    # 2. Silent mode with file logging
    print_("\n2. Silent Mode with File Logging:")
    print_("This won't show on console", silent=True)
    print_("But will log to file", file="advanced.log", mode="w", silent=True)
    
    # 3. Multiple return types
    print_("\n3. Return Types Demo:")
    
    # Return as string
    as_string = print_("Test", return_string=True, silent=True)
    print_(f"As string: '{as_string}'")
    
    # Return as bytes
    as_bytes = print_("Test", _bytes_=True, return_string=True, silent=True)
    print_(f"As bytes: {as_bytes}")
    
    # 4. Complex input with all options
    print_("\n4. Complex Input Demo:")
    answer = input_(
        "Choose wisely: ",
        choices=["A", "B", "C"],
        default="B",
        show_choices=True,
        lower=True,
        strip=True,
        required=True
    )
    print_(f"You chose: {answer.upper()}")
    
    # 5. Error handling demonstration
    print_("\n5. Error Handling Demo:")
    result = print_("", file="nonexistent.txt", mode="r", return_string=True, silent=True)
    if "Error" in result:
        print_("Error handling works correctly")
    
    print_("\n" + "=" * 60)
    print_("All advanced features demonstrated successfully!")
    print_("=" * 60)

if __name__ == "__main__":
    advanced_demo()
