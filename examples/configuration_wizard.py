#!/usr/bin/env python3
"""
Configuration Wizard - Interactive setup with validation
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_

def setup_config():
    print_("CONFIGURATION WIZARD", timestamp=True)
    print_("=" * 50)
    
    config = {}
    
    # Collect configuration with various options
    config["app_name"] = input_("Application name: ", 
                                default="MyApp",
                                required=True)
    
    config["environment"] = input_("Environment: ",
                                   choices=["development", "staging", "production"],
                                   default="development",
                                   show_choices=True)
    
    config["debug"] = input_("Enable debug mode? ",
                            choices=["yes", "no"],
                            default="no",
                            lower=True) == "yes"
    
    config["port"] = input_("Server port: ",
                           default="8080",
                           required=True)
    
    config["log_level"] = input_("Log level: ",
                                choices=["debug", "info", "warning", "error"],
                                default="info",
                                show_choices=True)
    
    # Display configuration
    print_("\n" + "=" * 50)
    print_("CONFIGURATION SUMMARY", timestamp=True)
    for key, value in config.items():
        print_(f"{key:15}: {value}")
    
    # Save to file
    print_("\nSaving configuration...")
    for key, value in config.items():
        print_(f"{key}={value}", file="config.ini", mode="a")
    
    print_("Configuration saved to 'config.ini'")
    return config

if __name__ == "__main__":
    setup_config()
