#!/usr/bin/python3
def uppercase(some_str):
    for char in some_str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()  # Add a new line at the end
