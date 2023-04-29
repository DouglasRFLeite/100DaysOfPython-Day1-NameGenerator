from io import StringIO
import sys
import pytest 
import src.name_generator as name_generator

def test_name_generator(monkeypatch):
    user_input = "Salvador\nPandora"
    expected_output = """Welcome to the Band Name Generator.
What's the name  of the city you grew up in?
What's your pet's name?
Your band name could be Salvador Pandora
"""
    
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    
    # Use StringIO to capture output from print() statements
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the function and check the output
    name_generator.generate_name()
    assert captured_output.getvalue() == expected_output, f'Should be: \n {expected_output} \n, was:\n {captured_output.getvalue()}'
