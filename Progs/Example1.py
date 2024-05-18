#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def writefile():
    # open the file2.txt in append mode. Create a new file if no such file exists.
    fileptr = open("file2.txt", "w")
    # appending the content to the file
    fileptr.write(
        "Python is a very cool language.\n"
        "With it you can make so much stuff you could not even imagine about"
    )
    # closing the opened the file
    fileptr.close()

def writefile2():
    # open the file2.txt in append mode. Create a new file if no such file exists.
    with open("file2.txt", "w") as fileptr:
    # appending the content to the file
        fileptr.write(
            "Python is a very cool language.\n"
            "With it you can make so much stuff you could not even imagine about"
    )
def main():
    writefile()
    writefile2()

if __name__ == "__main__":
    main()