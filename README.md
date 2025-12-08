```markdown
## Kipio - Enhanced I/O Library for Python

A complete I/O solution packed into 88 elegant lines of Python code. Kipio provides enhanced input and output functions with validation, security features, and file operations.

## Overview

Kipio is a lightweight yet powerful I/O library that simplifies user input and output operations in Python. It's designed for developers who need robust I/O handling without external dependencies.

## Installation

```bash
pip install kipio
```

## Quick Start

```python
from kipio import input_, print_

# Enhanced input with validation
name = input_("Enter your name: ", required=True)

# Enhanced output with timestamp
print_(f"Hello {name}!", timestamp=True)
```

## Core Features

## Enhanced Input (input_())

· Input validation with allowed choices
· Default values and required fields
· Hidden input for passwords (masked)
· Case normalization and whitespace stripping
· Byte encoding support

## Enhanced Output (print_())

· File operations (read/write/append)
· Timestamp auto-insertion
· Silent mode for logging
· Return as string or bytes
· Custom separators and endings

Complete Documentation

## input_() Function

```python
def input_(prompt="", _bytes_=False, strip=True, lower=False, default=None,
           choices=None, encoding="utf-8", required=False,
           show_choices=False, hidden=False, mask_char="*"):
    """
    Enhanced input function with comprehensive options.
    
    Parameters:
    -----------
    prompt : str
        Display text before input
    _bytes_ : bool
        Return bytes instead of string
    strip : bool
        Strip whitespace from input
    lower : bool
        Convert input to lowercase
    default : any
        Default value if input is empty
    choices : list
        List of allowed input values
    required : bool
        Raise error if input is empty
    show_choices : bool
        Display available choices in prompt
    hidden : bool
        Hide input (for passwords)
    mask_char : str
        Character to display for hidden input
    
    Returns:
    --------
    str or bytes : User input
    """
```

## print_() Function

```python
def print_(*values, file=None, mode=None, end="\n", sep=" ", flush=False,
           silent=False, timestamp=False, return_string=False, 
           encOD='utf-8', _bytes_=False):
    """
    Enhanced print function with file operations.
    
    Parameters:
    -----------
    *values : any
        Values to print
    file : str
        File path for file operations
    mode : str
        File mode: 'r' (read), 'w' (write), 'a' (append), 'x' (exclusive create)
    end : str
        String appended after the last value
    sep : str
        String inserted between values
    flush : bool
        Whether to forcibly flush the stream
    silent : bool
        Don't print to console (useful for file-only operations)
    timestamp : bool
        Add timestamp before message
    return_string : bool
        Return string instead of printing
    encOD : str
        Encoding for bytes conversion
    _bytes_ : bool
        Return bytes instead of string
    
    Returns:
    --------
    None, str, or bytes : Depending on parameters
    """
```

## Usage Examples

## Basic Usage

```python
from kipio import input_, print_

# Simple input with validation
age = input_("Enter your age: ", required=True)

# Input with choices
color = input_("Favorite color: ", 
               choices=["red", "green", "blue"],
               show_choices=True)

# Output to console and file
print_("Processing data...", timestamp=True)
print_("Results:", 42, 3.14, sep=" | ")
```

## Security Features

```python
# Password input
password = input_("Password: ", hidden=True, mask_char="•")

# Confirmation
confirm = input_("Confirm password: ", hidden=True, required=True)
```

## File Operations

```python
# Write to file
print_("Log entry", file="app.log", mode="a", timestamp=True)

# Read from file
content = print_("", file="config.txt", mode="r", return_string=True)

# Silent logging (file only)
print_("Debug info", file="debug.log", mode="a", silent=True)
```

## Advanced Features

```python
# Return as string
message = print_("Hello", "World", sep=", ", return_string=True, silent=True)

# Return as bytes
data = print_("Binary data", _bytes_=True, return_string=True)

# Complex input with all options
config = input_("Setting: ",
                default="default_value",
                choices=["option1", "option2", "default_value"],
                show_choices=True,
                lower=True,
                required=True)
```

## Real-World Scenarios

## Configuration Setup

```python
config = {
    "username": input_("Username: ", required=True),
    "theme": input_("Theme: ", 
                    choices=["dark", "light", "auto"],
                    default="dark",
                    show_choices=True),
    "notifications": input_("Enable notifications? ",
                           choices=["yes", "no"],
                           default="yes") == "yes"
}
```

## CLI Application

```python
def main_menu():
    while True:
        print_("\n=== MAIN MENU ===")
        print_("1. Add User")
        print_("2. View Logs")
        print_("3. Settings")
        print_("4. Exit")
        
        choice = input_("Select (1-4): ", 
                       choices=["1", "2", "3", "4"],
                       required=True)
        
        if choice == "4":
            print_("Goodbye!", timestamp=True)
            break
```

## Error Handling

## Kipio includes built-in error handling:

```python
try:
    result = input_("Enter value: ", required=True)
except Exception as e:
    print_(f"Error: {e}")
    
# Or handle errors returned as string
result = print_("", file="nonexistent.txt", mode="r", return_string=True)
if "Error:" in result:
    print_("File not found")
```

## Performance

· Zero external dependencies
· Minimal memory footprint
· Efficient 88-line implementation
· Compatible with Python 3.7+

## Testing

Test files are available in the examples/ directory:

```bash
# Run basic example
python examples/basic_usage.py

# Test all features
python examples/advanced_features.py
```

## Contributing

Kipio is developed as part of the kiux-tools collection. Issues and contributions are welcome.

## Version History

· 1.0.0 - Initial release with complete I/O functionality

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Developed by kiux-tools - Cybersecurity and development labs.

## Links

· PyPI: https://pypi.org/project/kipio/
· Source Code: https://github.com/kiux-tools/kipio

```
