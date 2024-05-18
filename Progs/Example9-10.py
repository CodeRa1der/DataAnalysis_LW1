#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def main():
    a = int(input("Choose example (9, 10): "))

    if a == 9:
        # rename file2.txt to file3.txt
        os.rename("file2.txt", "file3.txt")

    elif a == 10:
        # deleting the file named file3.txt
        os.remove("file3.txt")

if __name__ == "__main__":
    main()