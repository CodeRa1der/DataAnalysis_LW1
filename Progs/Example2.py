#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def writefile():
    # open the file.txt in write mode.
    fileptr = open("file2.txt", "a")

    # overwriting the content of the file
    fileptr.write(" Python has an easy syntax and user-friendly interaction.")

    # closing the opened file
    fileptr.close()

def writefile2():
    # open the file2.txt in write mode.
    with open("file2.txt", "a") as fileptr:
        # overwriting the content of the file
        fileptr.write(" Python has an easy syntax and user-friendly interaction.")
def main():
    writefile()
    writefile2()

if __name__ == "__main__":
    main()