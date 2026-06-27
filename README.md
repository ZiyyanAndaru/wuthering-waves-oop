# Wuthering Waves OOP Practice

A simple command-line Python script that models character data from the game Wuthering Waves. This project serves as my first GitHub repository to practice beginner Object-Oriented Programming (OOP).

## What is this Project?
This script simulates a character manager for the game. It allows you to:
* Create characters with specific stats like HP, Element, and Weapon types.
* Track equipped Echoes in a dynamic list.
* Simulate taking damage safely without health dropping below 0.
* Save and load character profile data locally to a text file.

## What I Practiced
Building this project helped me apply the concepts from Tech with Tim's OOP tutorial:

* **Classes and Objects:** Using instance variables (`self`) to track changing data like current HP vs Max HP.
* **Inheritance:** Creating a `Character` class that inherits from `Resonator` and uses `super().__init__()` to add game-specific stats like the Resonance Chain.
* **Class Methods (`@classmethod`):** Using `.from_dict()` as an alternative way to load character data cleanly.
* **Static Methods (`@staticmethod`):** Creating a utility tool (`calculate_damage`) to run math without needing instance data.
* **Error Handling & File I/O:** Using `try/except` blocks to read and write data to a local `stats.txt` file safely.

## Prerequisites
- Python 3.6 or above installed

## How to Run It

1. Open your terminal inside the project folder.
2. Run the script using Python:
```bash
python resonator.py
```
