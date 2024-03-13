#!/usr/bin/python3
def remove_char_at(some_str, n):
    # Check if the index is within the bounds of the string
    if 0 <= n < len(some_str):
        # Use slicing to create a copy of the string without the character at index n
        new_str = some_str[:n] + some_str[n + 1:]
        return new_str
    else:
        # return some string 
        return some_str
