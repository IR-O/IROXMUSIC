import textwrap  # This import is used to wrap the lines of text to a specified width
from markdown import Markdown  # This import is used to convert Markdown syntax to HTML

# Assign a multi-line string containing help text to the variable HELP_TEXT
HELP_TEXT = """
# Admin commands
...
"""

# Initialize a new instance of the Markdown class and assign it to the variable md
md = Markdown()

# Convert the HELP_TEXT string to Markdown format and assign it to the variable help_message
help_message = md.convert(HELP_TEXT)
