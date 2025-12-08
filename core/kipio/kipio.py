# Enhanced I/O Library for Python

def input_(prompt="", _bytes_=False, strip=True, lower=False, default=None,
           choices=None, encoding="utf-8", required=False,
           show_choices=False, hidden=False, mask_char="*"):
    """
    Enhanced input function with validation and options.
    """
    try:
        prompt = prompt.rstrip()
        
        # Normalize choices if lower=True
        normalized_choices = None
        if choices:
            normalized_choices = [choice.lower() for choice in choices] if lower else choices
        
        # Prepare prompt with choices or default
        if choices and show_choices:
            full_prompt = f"{prompt} [{' / '.join(choices)}] "
        elif default is not None:
            default_str = str(default).lower() if lower else str(default)
            full_prompt = f"{prompt} [{default_str}] "
        else:
            full_prompt = f"{prompt} "

        while True:
            # Get user input
            if hidden:
                try:
                    from getpass import getpass
                    user_input = getpass(full_prompt)
                    if mask_char and user_input:
                        print(mask_char * len(user_input))
                except Exception:
                    user_input = input(full_prompt)
            else:
                user_input = input(full_prompt)
            
            # Strip if requested
            if strip:
                user_input = user_input.strip()
            
            # Process input
            processed_input = user_input.lower() if lower else user_input
            
            # Handle empty input with default
            if not processed_input and default is not None:
                processed_input = str(default).lower() if lower else str(default)
                user_input = str(default)
            # Validate against choices (using normalized list)
            if normalized_choices and processed_input not in normalized_choices:
                print(f"Must be one of: {', '.join(choices)}")
                continue
            
            # Check required field
            if required and not processed_input:
                print("This field is required")
                continue
            
            # Return final value
            final_value = processed_input if lower else user_input
            return final_value.encode(encoding) if _bytes_ else final_value
            
    except Exception as e:
        return f"Error: {e}"


def print_(*values, file=None, mode=None, end="\n", sep=" ", flush=False,
           silent=False, timestamp=False, return_string=False, 
           encOD='utf-8', _bytes_=False):
    """
    Enhanced print function with file operations.
    """
    try:
        import os
        
        # Prepare text
        text = sep.join(str(v) for v in values) if values else ""
        
        # Add timestamp if requested
        if timestamp:
            from datetime import datetime
            text = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}"
        
        full_text = text + end
        
        # Handle file operations
        if file is not None:
            if mode is None:
                mode = "a"
            
            if mode == "r":
                with open(file, "r", encoding=encOD) as f:
                    return f.read()
                    
            elif mode in ("w", "a", "x"):
                if mode == "x" and os.path.exists(file):
                    raise FileExistsError(f"File '{file}' already exists")
                
                with open(file, mode, encoding=encOD) as f:
                    f.write(full_text)
                
                if not silent:
                    print(text, end=end, flush=flush)
                    
            else:
                raise ValueError(f"Unsupported mode: {mode}")
            
            # Return appropriate value for file operations
            if return_string:
                return full_text
            if _bytes_:
                return full_text.encode(encOD)
            return None
            
        # Handle console output
        if not silent:
            print(text, end=end, flush=flush)
        
        # Return based on parameters
        if return_string:
            return full_text
        
        if _bytes_:
            return full_text.encode(encOD)
            
    except Exception as e:
        error_msg = f"Error: {e}"
        if not silent:
            print(error_msg)
        return error_msg
