# Read Please
# Web Page Loader and SimHash Comparison
## Project Overview

This project consists of two Python modules:

---

## Project1 – Web Page Loader

Project1 contains the logic to:

- Accept a URL from the command line
- Fetch the web page content
- Extract and display:
  - Page Title (without HTML tags)
  - Page Body Text (plain text only)
  - All anchor tag links (`href` values)

It uses `requests` to fetch the page and `BeautifulSoup` for HTML parsing.

---

## Project2 – SimHash Comparison

Project2 implements document similarity detection using the SimHash algorithm.

It includes functions to:

- Clean and tokenize body text
- Compute word frequencies
- Generate a 64-bit SimHash fingerprint
- Compare the SimHash of two URLs
- Output the number of matching bits (similarity measure)

This module accepts two URLs from the command line and compares their similarity based on page content.

---

## Requirements

Other than that
---
Nothing Much, Just Make sure to run requirements.txt

pip install -r requirements.txt
---

## How to Run

### Run Project1

python Project1.py `<URL>`

### Run Project2

python Project2.py `<URL1>` `<URL2>`
