# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FRC Team 302 Sofware Documentation'
copyright = '2023, Team 302 '
author = 'Team 302 Software'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['static']
html_logo = "Team302LogoNew.png"

# -- Options for EPUB output
epub_show_urls = 'footnote'
