#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


def main():
    a = int(input("Choose example (11, 12, 13, 14): "))

    if a == 11:
        # creating a new directory with the name new
        os.mkdir("new")

    if a == 12:
        path = os.getcwd()
        print(path)

    if a == 13:
        # Changing current directory with the new directiory
        os.chdir("/home/code_ra1der/")
        # It will display the current working directory
        print(os.getcwd())

    if a == 14:
        # removing the new directory
        os.rmdir("new")


if __name__ == "__main__":
    main()
