import sys
import scrython
from scrython import *
import re

def format_args(string):
    start = '|arg|type|description|\n|:---:|:---:|:---:|'

    names = re.findall(r'(\w*\s\([\w,\s]*\):)', string)

for _class in scrython.__all__:

    intro = """These docs will likely not be as detailed as the official Scryfall Documentation, and you should reference that for more information.

    >In the event that a key isn't found or has been changed, you can access the full JSON output with the `scryfallJson` variable (`{}().scryfallJson`).
    """.format(eval(_class).__name__)

    class_docstring = repr(re.sub(r'\n+', '', eval(_class).__doc__)) # removes newlines

    remove_extra_spaces = re.sub(' +', ' ', class_docstring)

    args = re.findall(r'(?<=Args:)(.*)(?=Returns:)', remove_extra_spaces)[0]
    format_args(args)

    returns = re.findall(r'(?<=Returns:)(.*)(?=Raises:)', remove_extra_spaces)[0]

    raises = re.findall(r'(?<=Raises:)(.*)(?=Examples:)', remove_extra_spaces)[0]

    examples = re.findall(r'(?<=Examples:)(.*)', remove_extra_spaces)[0]

    # match = list(filter(None, (token.strip() for token in re.findall(r'[^\n]*', eval(_class).__doc__))))

    # with open('{}.md'.format(eval(_class).__name__), 'w') as f:
    #     f.write('# **class** `{}()`\n'.format(eval(_class).__name__))
    #     f.write(intro)
    #     for token in match:
    #         if re.findall(r'[A-Z][a-z].*:', token) and ':' in re.findall(r':.*', token): # Match section header
    #             f.write('\n\n## {}\n\n'.format(token.replace(':', '')))
    #             if 'Example' in token:
    #                 f.write(token)
    #             else:
    #                 f.write('| arg | description |\n|:---:|:---:|')
    #         elif re.findall(r'[\w]+\s\(.+\):', token): # Match args description
    #             if 'Defaults' in token:
    #                 f.write(token)
    #             else:
    #                 f.write('\n|{}|'.format(token))
    #         else:
    #             f.write('\n|{}|'.format(token))
    break
