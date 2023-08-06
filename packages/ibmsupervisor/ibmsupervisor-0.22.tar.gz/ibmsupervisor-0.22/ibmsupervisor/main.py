#!/usr/bin/env python3
"""
Extract the supervisor password from an IBM ThinkPad 365XD EEPROM dump
"""
# SPDX-FileCopyrightText: 2022 Eloy Degen <degeneloy@gmail.com>
# SPDX-License-Identifier: MIT

import sys
import os
import argparse

# pylint: disable=missing-function-docstring
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help="EEPROM dump file to analyze")

    # Print help if no arguments are given
    if len(sys.argv) < 2:
        # Print the *full* help, not the suggestions
        parser.print_help()
        # Exit with error
        sys.exit(1)

    args = parser.parse_args()

    if not os.path.exists(args.file):
        sys.exit("File not found")

    with open(args.file, 'rb') as file:
        # Keyboard scancodes retrived from
        # https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
        scancodes = {
            0x1e: "a",
            0x30: "b",
            0x2e: "c",
            0x20: "d",
            0x12: "e",
            0x21: "f",
            0x22: "g",
            0x23: "h",
            0x17: "i",
            0x24: "j",
            0x25: "k",
            0x26: "l",
            0x32: "m",
            0x31: "n",
            0x18: "o",
            0x19: "p",
            0x10: "q",
            0x13: "r",
            0x1f: "s",
            0x14: "t",
            0x16: "u",
            0x2f: "v",
            0x11: "w",
            0x2d: "x",
            0x15: "y",
            0x2c: "z",
            0xb: 0,  # Removed leading hexadecimal zero because list(file.read())
            0x2: 1,  # removes them when reading the file
            0x3: 2,
            0x4: 3,
            0x5: 4,
            0x6: 5,
            0x7: 6,
            0x8: 7,
            0x9: 8,
            0xa: 9
        }
        file_list = list(file.read())

        # Use backup password and filesize to validate file is correct
        if file_list[56:64] != file_list[64:72] or len(file_list) != 128:
            # pylint: disable=line-too-long
            sys.exit("[error] Either this is the wrong file, or the flash hasn't been correctly dumped. Try again.")

        print("[info] The password is case-insensitive")
        print("Supervisor password: ")

        file_list = file_list[56:64]

        # Swap every two bytes, 4 times in total
        for i in range(0, 7, 2):
            file_list[i], file_list[i+1] = file_list[i+1], file_list[i]

        # Password is 7 alphanumeric characters at most, break if it's shorter
        for i in range(7):
            password_char = scancodes.get(file_list[i])
            if password_char is None:
                # Lookup failed because it is not an alphanumeric scancode
                break
            print(password_char, end='')
        print()

if __name__ == '__main__':
    main()
