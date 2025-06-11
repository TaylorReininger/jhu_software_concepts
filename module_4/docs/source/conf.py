# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Import some libraries
import os
import sys
import shutil

# Some pathing
sys.path.append(os.path.abspath("../.."))
sys.path.append(os.path.abspath(".."))

# Copy images into the Sphinx working folder so that MystParser can use
# them in the README
shutil.copytree("../../figs", "./figs", dirs_exist_ok=True)

# Project meta data
project = 'Module4'
copyright = '2025, Taylor J. Reininger'
author = 'Taylor J. Reininger'
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'myst_parser']
source_suffix = ['.rst', '.md']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# Set a logo for the documentation
html_logo = "../../figs/pizza_image.jpg"

