# Hangman

## Introduction

Welcome to the Hangman Game Project! This classic word-guessing game has entertained players for generations, blending strategy, vocabulary, and a dash of suspense. The objective is simple: guess the hidden word by suggesting letters within a limited number of attempts. Each incorrect guess brings the player closer to losing, while each correct letter gradually reveals the mystery word.

In this project, we are implementing a digital version of Hangman where both human players and the computer can participate. Players can compete against the computer, which will randomly select words and make guesses, adding an exciting twist to the traditional gameplay. Additionally, users can challenge themselves against different difficulty levels and a diverse word bank, enhancing the educational value of the game.

This documentation will guide you through the development process, detailing the game's design, features, and technical specifications. Join us as we explore the world of Hangman and create a memorable gaming experience for everyone involved!

# Project Overview

This project aims to develop a digital version of the classic Hangman game using Python, the Tkinter graphical user interface (GUI) toolkit, and a MySQL database.

## Game Modes

We offer two engaging gaming modes:

### 1. Player vs. Computer

In this mode, the user attempts to guess a word randomly selected by the computer. The process is as follows:

- The computer generates a random word from the database.
- The program displays the length of the word using empty spaces for each letter.
- The user is prompted to guess letters that may be present in the word.
- The computer provides feedback on the guesses, filling in the correct letters in their corresponding positions.
- The game tracks the number of attempts remaining.
- Players win by guessing the word within eight attempts; otherwise, they lose.

### 2. Computer vs. User

In this mode, the user thinks of a word, and the program attempts to guess it. Here’s how it works:

- The user selects a word and inputs its length.
- The program generates random character guesses and asks the user for feedback on each letter's presence and position.
- Initially, the program uses common, frequently occurring letters for its guesses. Based on the user's feedback, it shifts to more educated guesses, filtering potential words from the database that match the letters already identified.
- This iterative guessing process continues until the program narrows down to a single word based on the user's responses.

The Tkinter GUI toolkit enhances the user experience by providing an interactive and user-friendly interface, ensuring smooth gameplay and making it accessible for players of all ages.

