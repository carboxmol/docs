# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent
REPO_ROOT = DOCS_DIR.parent
sys.path.insert(0, str(REPO_ROOT))
if (REPO_ROOT / "carbox").exists():
    sys.path.insert(0, str(REPO_ROOT / "carbox"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CarboxMol'
copyright = '2026, Suleiman M Hajizadeh'
author = 'Suleiman M Hajizadeh'
release = '0.4.5'
version = '0.4.5'

# Base URL for canonical links and search engine discovery
html_baseurl = 'https://carboxmol.readthedocs.io/en/latest/'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx_sitemap',
]

# Sitemap configuration
sitemap_url_scheme = '{link}'

# Global metadata for Search Engine Optimization (SEO / Google / Bing / Yandex)
html_meta = {
    'google-site-verification': 'med3XHPJzcSjHLpdN-jmNKekn-MFZcQE8IwPeFbCk7o',
    'description': 'Official scientific documentation for CarboxMol & Carbox: Interactive 3D macromolecular crystallography workbench, GROMACS molecular dynamics studio, 2mFo-DFc electron density carving, anomalous carboxyl protonation, and Low-Barrier Hydrogen Bond (LBHB) discovery by Suleiman M Hajizadeh.',
    'keywords': 'CarboxMol, CarboxMol Studio, Carbox, Macromolecular Crystallography, 3D Molecular Viewer, GROMACS MD, Low Barrier Hydrogen Bonds, LBHB, Suleiman Hajizadeh, Garib Murshudov, Servalcat, REFMAC5, PDB validation, carboxyl protonation, pKa shifts, PROPKA, electron density map, 2Fo-Fc, structural biology, bioinformatics',
    'author': 'Suleiman M Hajizadeh',
    'robots': 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1',
    'googlebot': 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1',
    'bingbot': 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1',
    'og:site_name': 'CarboxMol Documentation',
    'og:title': 'CarboxMol & Carbox Documentation | 3D Macromolecular Crystallography & GROMACS Suite',
    'og:description': 'Official trilingual (EN/AZ/HE) scientific documentation for CarboxMol & Carbox: 3D WebGL crystallography workbench, GROMACS simulations, electron density validation, and LBHB discovery.',
    'og:type': 'website',
    'og:url': 'https://carboxmol.readthedocs.io/en/latest/',
    'og:image': 'https://carboxmol.github.io/assets/carboxmol_logo.png',
    'twitter:card': 'summary_large_image',
    'twitter:title': 'CarboxMol & Carbox Documentation | 3D Macromolecular Crystallography & GROMACS Suite',
    'twitter:description': 'Official scientific documentation for CarboxMol & Carbox: 3D crystallography workbench, GROMACS molecular dynamics, and LBHB validation.',
    'twitter:image': 'https://carboxmol.github.io/assets/carboxmol_logo.png',
}

# Mock scientific dependencies to ensure lightweight and reliable builds on Read the Docs
autodoc_mock_imports = [
    'gemmi',
    'numpy',
    'scipy',
    'pandas',
    'matplotlib',
    'seaborn',
    'tqdm',
    'propka',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

root_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', 'venv']
suppress_warnings = ['myst.header', 'misc.highlighting_failure']

# MyST Markdown Parser options
myst_enable_extensions = [
    'dollarmath',
    'amsmath',
    'deflist',
    'html_admonition',
    'html_image',
    'colon_fence',
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['assets']
html_extra_path = ['robots.txt']
html_title = 'CarboxMol & Carbox Documentation'
html_logo = 'assets/carboxmol_logo.png'
html_favicon = 'assets/carbox_logo.png'

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
}
