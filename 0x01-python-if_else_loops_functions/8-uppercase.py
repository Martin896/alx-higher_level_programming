#!/usr/bin/python3

def print_last_digit(number):
    last_digit = number % 10

    print(last_digit)
    return last_digit


result = print_last_digit(12345)
print("Value of the last digit:", result)
