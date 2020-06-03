# Import the framework
from flask import Flask
import markdown
import os

# Create and instance of Flask
app = Flask (__name__)

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    readme_file = os.path.dirname(app.root_path) + '/README.md'
    with open(readme_file, 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)