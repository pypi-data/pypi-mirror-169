import os
import sys
sys.path.insert(0, os.path.abspath("../src"))

import very_simple_wordle_server

project = 'Very Simple Wordle Server'
copyright = "2022, zluudg"
author = 'zluudg'
release = 'very_simple_wordle_server.__version__'
version = 'very_simple_wordle_server.__version__'

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
templates_path = ['_templates']
exclude_patterns = ["dist", ".tox", ".pytest_cache", "build", "venv"]

html_theme = 'alabaster'
html_static_path = ['_static']

nitpicky = True
