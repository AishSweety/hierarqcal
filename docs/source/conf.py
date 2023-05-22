import sys
import os
import sphinx_rtd_theme
from distutils.dir_util import copy_tree


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "HierarQcal"
copyright = "2023, Matt Lourens"
author = "Matt Lourens"
release = "2023"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]
templates_path = ["_templates"]
exclude_patterns = []
napoleon_google_docstring = True
napoleon_use_param = False
napoleon_use_ivar = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ["_static"]
html_favicon = "./img/dalle_img.png"

# =================== #
# For installing sphynx
# Install sphynx (cd into hierarqcal), run: pip install -r /docs/requirements.txt
# For generating the API docs:
# cd into docs and run:
# sphinx-apidoc -f -E -e -M -P -o source/generated/ ../../hierarqcal/
# sphinx-build -b html source build
# =================== #

autodoc_default_options = {"special-members": "__call__, __add__, __mul__"}
nb_execution_mode = "off"

copy_tree('img', '../build/img')


sys.path.append("../../hierarqcal")
# This should be the repository root
sys.path.append("../../")
sys.path.append("../")
sys.path.append("../../../")
sys.path.append("/github/workspace")
import hierarqcal