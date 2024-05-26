#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая будет открывать файл со списком
# слов, случайным образом выбирать два из них и сцеплять вместе для получения итогового
# пароля. При создании пароля нужно следовать следующему требованию: он должен состоять
# минимум из восьми символов и максимум из десяти, а каждое из используемых слов
# должно быть длиной хотя бы в три буквы. Кроме того, нужно сделать заглавными первые буквы
# обоих слов, чтобы легко можно было понять, где заканчивается одно и начинается другое.
# По завершении процесса полученный пароль должен быть отображен на экране.


import random


def generate(words):
    while True:
        word1, word2 = random.sample(words, 2)
        if len(word1) >= 3 and len(word2) >= 3:
            password = word1.capitalize() + word2.capitalize()
            if len(password) >= 8 and len(password) <= 10:
                return password


def passmaking():
    try:
        with open("task2.txt", "r") as fileptr:
            words = [line.strip() for line in fileptr.readlines()]

            password = generate(words)
            print("Generated password: ", password)
    except FileNotFoundError:
        print("File task2.txt not found. Create a new one and fill it with words (should be written apart on different lines)")
        


def main():
    passmaking()


if __name__ == "__main__":
    main()
