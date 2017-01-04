# -*- coding: utf-8 -*-
#
# Cloudmesh Classes documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 23 15:46:26 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))



on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    bootstrap_theme = False
    foundation_theme = False
    rtd_them = True
else:
    bootstrap_theme = False
    foundation_theme = True
    rtd_theme = False

if bootstrap_theme:
    import sphinx_bootstrap_theme
elif foundation_theme:
    import foundation_sphinx_theme
    
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.bibtex',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinx-prompt'
]

if foundation_theme:
    sys.path[0:0] = [os.path.abspath('_themes/foundation-sphinx-theme')]
    extensions += ['foundation_sphinx_theme']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Big Data Classes'
copyright = u'2016, Gregor von Laszewski, Badi Abdul-Wahid'
author = u'Gregor von Laszewski'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
pygments_style = 'monokai'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

if not on_rtd and rtd_theme:  # only import and set the theme if we're building docs locally

    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

elif bootstrap_theme:

    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

elif foundation_theme:

    html_theme = 'foundation_sphinx_theme'
    html_theme_path = foundation_sphinx_theme.HTML_THEME_PATH
    

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

if foundation_theme:
    
   html_theme_options = {
        'motto': 'Long description which appears next to logo.',

        # Your stylesheet relative to the _static dir.
        # Default is 'foundation/css/basic.css'
        #'stylesheet': '/path/to/your/stylesheet.css',
        # Default is 'foundation/css/basic.css'        
        'stylesheet': 'foundation/css/cards.css',

        # Logo image in SVG format. If the browser doesn't support SVG
        # It will try to load JPG with the same name.
        'logo_screen': '',

        # Logo for small screens. If ommited, logo_screen will be used.
        'logo_mobile': '',

        # Path to your favicon.ico file relative to the _static dir.
        'favicon': '',

        # Use this if the top-level items of the toctree don't fit in the top-bar navigation.
        # If True, the whole toctree will be placed inside a single top-level item.
        'top_bar_force_fit': True,

        # The title of the aformentioned top-level item. Default is "Sections"
        'top_bar_content_title': 'Sections',

        # If set, Google Analytics code will be appended to body of each page.
        #'google_analytics_id': 'your-google-analytics-id',

        # The "og:title", "og:type", "og:url", "og:site_name" and "og:description" Open Graph tags
        # will be generated automatically, but you should specify the
        # path to the image that you want to be used
        # in the required "og:image" property relative to the _static dir.
        #'opengraph_image': 'path/to/your/opengraph-image.jpg',

        # Any custom additional OG tags
        #'opengraph_tags': {
        #        'foo': 'bar', # will be rendered as <meta property="og:foo" content="bar" />
        #},

        # The "description" meta tag will be created automatically, but
        # you can specify additional meta tags here.
        'meta_tags': {
                'foo': 'bar', # will be rendered as <meta name="foo" content="bar">
        },

        # The value for "description" and "og:description" metatags.
        # If omitted, the value of "motto" will be used.
        'seo_description': 'This is an example of the Foundation Sphinx Theme output.',

        # Use this as the base for Open Graph URLs without trailing slash.
        'base_url': 'http://cloudmesh.org/classes',

        # If true a bar with Facebook, Google+ and Twitter social buttons will be displayed
        # underneath the header.
        #'social_buttons': True,

        # ID of your Facebook app associated with the Facebook Like button.
        #'facebook_app_id': '123456789',

        # A Twitter ID used for the via mention of the Twitter button.
        #'twitter_id': 'FoundationSphinx',

        # Flattr button settings.
        #'flattr_id': 'andypipkin', # Your Flattr ID
        #'flattr_title': '', # If missing docstitle or title will be used.
        #'flattr_description': '', # If missing seo_description or motto will be used.
        #'flattr_tags': '', # Optional.


        # If "author" and "copyright_year" are set they will override the "copyright" setting.

        # Author's name.
        'author': 'Gregor von Laszeski, Badi Abdhul-Wahid',

        # Author's link.
        'author_link': 'http://gregor.cyberaide.org',

        # Year to be used in the copyright statement.
        'copyright_year': '2017',

        # Author's Google+ id. If set a G+ authorship link will be added.
        #'google_plus_id': '117034840853387702598',


        # Fork me on GitHub ribbon will be displayed if "github_user", "github_repo" and "github_ribbon_image" are set:
        # https://github.com/blog/273-github-ribbons
        # Ribbons are hidden on small screens!

        # Your GitHub ID.
        #'github_user': 'foundation-sphinx-theme',

        # The repository slug.
        #'github_repo': 'foundation-sphinx-theme',

        # Path to the ribbon image relative to the "_static" directory.
        #'github_ribbon_image': 'my-github-ribbon.png',

        # Position of the ribbon "left" or "right".
        #'github_ribbon_position': 'right',
   }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = u'Cloudmesh Classes v1.0'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'CloudmeshClassesdoc'




# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'CloudmeshClasses.tex', u'Cloudmesh Classes Documentation',
     u'Gregor von Laszewski', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'cloudmeshclasses', u'Cloudmesh Classes Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'CloudmeshClasses', u'Cloudmesh Classes Documentation',
     author, 'CloudmeshClasses', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
# epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#
# epub_tocdepth = 3

# Allow duplicate toc entries.
#
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#
# epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#
# epub_fix_images = False

# Scale large images.
#
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# epub_show_urls = 'inline'

# If false, no index is generated.
#
# epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
