# python-practice

## About The Project

This repository contains my solutions for CS50P, Harvard University's Introduction to Programming with Python.

Rather than just following tutorials, these files represent hands-on problem sets where I had to build working command-line applications from scratch. Through this course, I've learned how to structure logic, handle user input securely, catch errors, work with external data, and write professional unit tests.

---

## Skills & Technologies Demonstrated

- **Control Flow & Logic:** Complex loops and conditionals (`camel.py`, `coke.py`, `game.py`)
- **String Manipulation:** Processing and cleaning text inputs (`twttr.py`, `figlet.py`, `camel.py`)
- **Regular Expressions:** Pattern matching and text validation (`numb3rs.py`, `watch.py`, `um.py`, `working.py`)
- **Exception Handling:** Using `try/except` to prevent crashes (`fuel.py`, `taqueria.py`, `outdated.py`)
- **File I/O & CSV Processing:** Reading, writing, and reformatting data files (`scourgify.py`, `lines.py`)
- **Object-Oriented Programming:** Designing and implementing classes (`jar.py`)
- **Image & PDF Processing:** Overlaying images and generating PDFs (`shirt.py`, `shirtificate.py`)
- **External Libraries & APIs:** Fetching live data from the internet (`bitcoin.py`) and using libraries like `inflect`, `fpdf2`, `Pillow`, and `validators`
- **Unit Testing:** Writing thorough tests with `pytest` (`test_plates.py`, `test_fuel.py`, `test_um.py`, `test_seasons.py`, `test_working.py`, `test_numb3rs.py`)

---

## Highlights

Here are a few specific projects that demonstrate what I built:

- **`bitcoin.py`** — Queries the CoinCap v3 API in real time to get the current Bitcoin price and calculates the cost of a user-specified number of coins.
- **`professor.py`** — A math quiz application that generates random addition problems, tracks the user's score across 10 questions, and handles invalid inputs gracefully.
- **`figlet.py`** — Takes user text and converts it into large ASCII art using command-line arguments and external Python libraries.
- **`scourgify.py`** — Reads a CSV file with combined name fields, cleans and reformats the data, and writes a new structured CSV output.
- **`seasons.py`** — Prompts the user for their date of birth and calculates their age in minutes, expressed in English words.
- **`jar.py`** — An object-oriented cookie jar implementation with deposit, withdraw, and capacity management using Python classes and properties.
- **`numb3rs.py`** — Validates IPv4 addresses using regular expressions and thoroughly tested with `pytest`.
- **`shirtificate.py`** — Generates a personalized CS50 certificate PDF with the user's name overlaid on a shirt image using `fpdf2`.

---

## How to Run

You will need Python 3 installed on your machine. Clone this repository, navigate to the folder, and run any script with:
python filename.py

Some scripts require additional libraries. Install them with:
pip install requests inflect fpdf2 Pillow validators emoji pyfiglet

---

## Testing

Several projects include unit tests written with `pytest`. To run them:
pip install pytest
pytest test_filename.py

---

*Built as part of [CS50P — Harvard University's Introduction to Programming with Python](https://cs50.harvard.edu/python)*
