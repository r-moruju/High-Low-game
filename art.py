"""
This file contains ascii arts.
"""
from colors import Color as col
LOGO = f"""{" " * 10}
  _            _         _                    __ _                            
 | |          (_)       | |                  / /| |                           
 | |__    ___  _   __ _ | |__    ___  _ __  / / | |  ___ __      __ ___  _ __ 
 | '_ \  / _ \| | / _` || '_ \  / _ \| '__|/ /  | | / _ \ \ \ /\ / // _ \| '__|
 | | | ||  __/| || (_| || | | ||  __/| |  / /   | || (_) | \ V  V /|  __/| |   
 |_| |_| \___||_| \__, ||_| |_| \___||_| /_/    |_| \___/   \_/\_/  \___||_|   
                   __/ |                                                          
                  |___/                                                           
"""


def print_logo():
    """
    Clear terminal and print logo
    """
    print("\033c")
    print(col.YELLOW + LOGO.center(80))
