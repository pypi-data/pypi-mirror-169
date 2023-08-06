import os
import sys
sys.path.insert(0, os.path.abspath("../src"))

import wordle_probe

project = 'Wordle Probe'
copyright = "2022, zluudg"
author = 'zluudg'
release = 'wordle_probe.__version__'
version = 'wordle_probe.__version__'

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
templates_path = ['_templates']
exclude_patterns = ["dist", ".tox", ".pytest_cache", "build", "venv"]

html_theme = 'alabaster'
html_static_path = ['_static']

nitpicky = True
