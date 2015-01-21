# -*- coding: utf-8 -*-
#
# MEGARA DRP documentation build configuration file, created by
# sphinx-quickstart on Mon Oct 28 19:05:57 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
              'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.mathjax']

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['_build']

project = u'MEGARA Data Reduction Pipeline'
copyright = u'2013-2015, Universidad Complutense de Madrid'
version = '0.4'
release = '0.4dev'
show_authors = True

# -- Options for HTML output ---------------------------------------------------
html_theme = 'default'
#html_theme_path = []
#html_theme_options = {}
html_static_path = ['_static']
#html_logo = None
#html_last_updated_fmt = '%b %d, %Y'
#html_use_smartypants = True
#html_sidebars = {}
#html_additional_pages = {'index': 'index.html'}

# Output file base name for HTML help builder.
htmlhelp_basename = 'megaradrpdoc'


latex_documents = [
  ('index', 'megaradrp.tex', u'MEGARA DRP Documentation',
   u'Sergio Pascual', 'manual', 1),
]
latex_logo = '_static/megara.png'
latex_elements = {
'papersize': 'a4paper',
#'pointsize': '10pt',
#'preamble': '',
}

latex_elements = {
    'fontpkg': '\\usepackage{palatino}',
    }
latex_show_urls = 'footnote'
latex_show_urls = 'footnote'
#latex_appendices = []
#latex_domain_indices = True

intersphinx_mapping = {
  'numina': ('http://numina.readthedocs.org/en/latest/', None)
}