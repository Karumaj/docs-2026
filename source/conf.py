# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'kj-sphinx-26'
copyright = '2026, kj'
author = 'kj'
release = '2026-10-15'
spelling_lang = 'en_GB'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
   # 'sphinxcontrib.spelling'
]
try:
    import sphinxcontrib.spelling  # noqa: F401
    extensions.append("sphinxcontrib.spelling")
except ImportError:
    pass
    
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'diataxis': ('https://diataxis.fr', None)
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
