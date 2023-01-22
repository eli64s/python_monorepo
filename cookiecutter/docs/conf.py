"""Sphinx configuration."""
project = "Python Monorepo"
author = "Eli"
copyright = "2023, Eli"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
