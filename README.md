# 1Day-100DaysOfPythonGPT-BandNameGenerator
Day 1 of the 100 Days of Code with Python Bootcamp from Udemy.

## What is 100DaysOfPythonGPT?

100 Days of Python is a Python Bootcamp from Udemy that provides 100 days of Python pratical content with lessons and projects. The GPT part is something I'm adding to the course and infers that I shall use ChatGPT's engine and/or API in some way on each and every one of those 100 projects. Furthermore, I shall also practice using PyTest to test these projects and applications at least in some level.

## BandNameGenerator

Band Name Generator is the first project of the first Day of the bootcamp. It's original purpose is to develop the ability to play with basic strings, printing and reading input into variables. 

The actual project consists of reading from the console the name of a city and the name of a pet and concatenating them to create a band name.

I use ChatGPT's API only to create a more creative name than the mere concatenation of the two names, but the projects interface remains the same. 

I test only the "hard" contatenation function with PyTest.

## Project Structure

 - [src/](src/) - The `name_generator.py` file holds both the concatenation and the gpt-assisted name generation functions;
 - [test/](test/) - The `test_name_generator.py` file holds the test for the concatenation function;
 - [include/](include/) - The `gpt.py` file holds the `get_completion` function that accesses the ChatGPT API. 
