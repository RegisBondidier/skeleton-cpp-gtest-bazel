# Configuration file for the Sphinx documentation builder.
#

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'C++ squeleton'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_needs',
    'breathe',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgmath',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'matplotlib.sphinxext.plot_directive',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.test_reports',
    'm2r'
]

breathe_projects = {
  "TI_C66x_math_library": "@CMAKE_BINARY_DIR@/doxygen/xml",
}
breathe_default_project = "TI_C66x_math_library"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css'
]

# PlantUML options
plantuml_jar_root = os.getenv("PlantUml_ROOT")
if plantuml_jar_root is None:
    plantuml_jar = "/usr/share/plantuml/plantuml.jar"
else:
    plantuml_jar = os.path.join(plantuml_jar_root, "plantuml.jar")

plantuml = 'java -Djava.awt.headless=true -jar {}'.format(os.path.abspath(plantuml_jar))
plantuml_output_format = 'svg_img'

# Graphviz options
#graphviz_dot = 'neato' # The resulting graphs look like a graph factory exploded…
graphviz_output_format = 'svg'

# Math options
imgmath_image_format = 'svg'
imgmath_use_preview = True
imgmath_font_size = 14
imgmath_embed = True

todo_include_todos = True

# needs configuration
needs_title_optional = True

# need type definitions
needs_types = [
    dict(directive='req', title='Requirement', prefix='REQ_', color='#00FFC2', style='node'),
    dict(directive='comp', title='Component', prefix='COMP_', color='#FF4800', style='component'),
    dict(directive='test', title='Test', prefix='TEST_', color='#FFBD00', style='rectangle'),
]

# need link definitions
needs_extra_links = [
    {
       'option': 'requires',
       'incoming': 'is required by',
       'outgoing': 'requires'
    },
    {
       'option': 'implements',
       'incoming': 'is implemented by',
       'outgoing': 'implements'
    },
    {
       'option': 'tests',
       'incoming': 'is tested by',
       'outgoing': 'tests'
    },
 ]
