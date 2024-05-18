#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def generate(words):
    while True:
        word1, word2 = random.sample(words, 2)
        if len(word1) >= 3 and len(word2) >= 3:
            password = word1.capitalize() + word2.capitalize()
            if len(password) >= 8 and len(password) <= 10:
                return password
def passmaking():
    with open("task2.txt", "r") as fileptr:
        words = [line.strip() for line in fileptr.readlines()]

        password = generate(words)
        print("Generated password: ", password)

def main():
    passmaking()

if __name__ == "__main__":
    main()