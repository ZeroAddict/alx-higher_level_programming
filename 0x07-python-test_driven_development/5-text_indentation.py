#!/usr/bin/python3
"""Module: for text_indentation method"""


def text_indentation(text):
"""
Method: for text_indentation to display text
    Args:
        text: string text
    Raises:
         TypeError: if text is not a string
"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:"
#ultimate goal is to add delim and...
# join a stripped line (line.strip(" "))
# to... for line in withtext.split (delim)
#goal is to printargs(delim, 
#split text with text.split(delim))
#we make use of .join([line.strip()textTosplit.split(delim)])
          textToSplit = (delim + "\n\n").join(
              [line.strip(" ") for line in (text.split(delim))])  
    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
