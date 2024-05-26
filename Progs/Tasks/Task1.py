#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает английский текст из файла и выводит на экран
# слова текста, начинающиеся и оканчивающиеся на гласные буквы.


def check(word):
    check = "AEIOUaeiou"
    return len(word) > 1 and word[0] in check and word[-1] in check


def split(text):
    for char in '.,!?;:':
        text = text.replace(char, ' ')
    words = text.split()
    return words


def readeng():
    with open("task1.txt", "r") as fileptr:
        text = fileptr.read()
    words = split(text)

    for word in words:
        if check(word):
            print(word)


def main():
    readeng()


if __name__ == "__main__":
    main()
