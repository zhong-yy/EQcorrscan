# -*- coding: utf-8 -*-
#
# EQcorrscan documentation build configuration file, created by
# sphinx-quickstart on Mon Mar 23 21:20:41 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex
sys.path.insert(0, os.path.abspath('../..'))
import matplotlib
import eqcorrscan

READ_THE_DOCS = os.environ.get('READTHEDOCS', None) == 'True'
import sphinx_bootstrap_theme
# Use mock to allow for autodoc compilation without needing C based modules
import mock
import glob
MOCK_MODULES = ['cv2', 'h5py', 'eqcorrscan.utils.libnames']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../core'))
sys.path.insert(0, os.path.abspath('../utils'))

sys.path = [os.path.dirname(__file__) + os.sep + '_ext'] + sys.path


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    # 'matplotlib.sphinxext.mathmpl',
    # 'matplotlib.sphinxext.only_directives',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    # local extensions
    'sphinx.ext.autosummary',
    'obspydoc',
    'nbsphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'EQcorrscan'
copyright = u'2015-2021: EQcorrscan developers'
author = u'EQcorrscan developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.4'
# The full version, including alpha/beta/rc tags.
release = eqcorrscan.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# File formats to generate.
plot_formats = [('png', 110), ('hires.png', 200)]
if READ_THE_DOCS:
    plot_formats += [('pdf', 200)]
plot_html_show_formats = True

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_theme_options = {
    'bootswatch_theme': "sandstone",
}

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'EQcorrscan'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = './EQcorrscan_logo.jpg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = './EQcorrscan_logo.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'EQcorrscandoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',

    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'EQcorrscan.tex', u'EQcorrscan Documentation',
   u'Calum John Chamberlain', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'EQcorrscan_logo.pdf'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'eqcorrscan', u'EQcorrscan Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'EQcorrscan', u'EQcorrscan Documentation',
   author, 'EQcorrscan', 'One line description of project.',
   'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/2.7/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('http://matplotlib.org/', None),
    'sqlalchemy': ('http://docs.sqlalchemy.org/en/latest/', None),
    'obspy': ('https://docs.obspy.org/', None),
}

# generate automatically stubs
autosummary_generate = glob.glob("submodules" + os.sep + "*.rst")

# Don't merge __init__ method in auoclass content
autoclass_content = 'class'

# This value is a list of autodoc directive flags that should be automatically
# applied to all autodoc directives. The supported flags are 'members',
# 'undoc-members', 'private-members', 'special-members', 'inherited-members' an
# 'show-inheritance'. Don't set it to anything !
autodoc_default_flags = ['show-inheritance']

# warn about *all* references where the target cannot be found
nitpicky = False

trim_doctest_flags = True
