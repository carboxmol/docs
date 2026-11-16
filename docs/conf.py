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
if (REPO_ROOT / "carboxmol").exists():
    sys.path.insert(0, str(REPO_ROOT / "carboxmol"))

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
    'google-site-verification-secondary': 'lbqn6nIPchEP3d12Vf4UQmQpyKhJ1Mzq-di2S-t3rF0',
    'description': 'Official scientific documentation for CarboxMol (v0.4.5): Universal 3D macromolecular crystallography workbench, interactive WebGL Studio, GROMACS molecular dynamics simulation suite, real-space geometric refinement, electron density map carving (2mFo-DFc), bioinorganic metal coordination analysis, and CXL macro scripting by Suleiman M. Hajizadeh & Prof. Garib N. Murshudov.',
    'keywords': 'CarboxMol, CarboxMol Studio, CarboxMol Workbench, CarboxMol PWA, CarboxMol Documentation, CarboxMol CLI, CarboxMol WebGL, CarboxMol GROMACS, CarboxMol Python API, CarboxMol 4LGN, carboxmol server, carboxmol validate, carboxmol refine, carboxmol metal, carboxmol pli, carboxmol script, CXL macro scripting, CarboxMol Crystallographic Language, macromolecular crystallography workbench, interactive 3D molecular viewer, browser molecular graphics, WebGL protein visualization, electron density map viewer, 2mFo-DFc map carving, mFo-DFc difference map, CCP4 map reader, MRC2014 density format, real-space density carving, isocontour surface mesh, Marching Cubes molecular surface, cartoon ribbon representation, CPK van der Waals spheres, solvent accessible surface area, bioinorganic chemistry software, metal coordination polyhedra classifier, transition metal binding sites, zinc coordination sphere, tetrahedral geometry tau4 index, octahedral geometry tau6, protein-ligand interaction profiler, non-covalent contact detection, salt bridge analysis, pi-pi stacking aromatic interactions, hydrogen bond network analysis, real-space geometric refinement, stereochemical regularization, harmonic restraint minimization, MolProbity clashscore, Ramachandran plot validation, sidechain rotamer outliers, Richardson rotamer library, Engh Huber covalent geometry, B-factor thermal distribution, isotropic temperature factors, Kabsch superposition alignment, RMSD structural superposition, GROMACS automated simulation pipeline, pdb2gmx topology builder, AMBER99SB-ILDN force field, CHARMM27 CHARMM36m, OPLS-AA/L, GROMOS 54a7, TIP3P water model, SPC/E water, steepest descent energy minimization, NVT canonical equilibration, NPT isothermal isobaric equilibration, production MD trajectory, RMSF residue fluctuation, radius of gyration Rg, hydrogen bond persistence, structural biology software, bioinformatics tools, Suleiman M Hajizadeh, Suleiman Hajizadeh, Süleyman Hacızadə, Garib N Murshudov, Garib Murshudov, Qərib Mürşüdov, MRC Laboratory of Molecular Biology, MRC LMB Cambridge, Institute of Molecular Biology, Western Caspian University, Elm və Təhsil Nazirliyi Molekulyar Biologiya İnstitutu, Qərbi Kaspi Universiteti, makromolekulyar kristalloqrafiya, 3D zülal strukturu vizuallaşdırma, molekulyar dinamika simulyasiyası, GROMACS Azərbaycan, bioinformatika alətləri, elektron sıxlığı xəritəsi, biofiziki tədqiqat proqramı, Süleyman Hacızadə bioinformatika, kristalloqrafik analiz proqramı',
    'author': 'Suleiman M. Hajizadeh & Prof. Garib N. Murshudov',
    'robots': 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1',
    'googlebot': 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1',
    'bingbot': 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1',
    'og:site_name': 'CarboxMol Documentation',
    'og:title': 'CarboxMol Documentation | 3D Macromolecular Crystallography & GROMACS Suite',
    'og:description': 'Official trilingual (EN/AZ/HE) scientific documentation for CarboxMol: 3D WebGL crystallography workbench, GROMACS simulations, electron density validation, real-space refinement, and CXL scripting by Suleiman M. Hajizadeh & Prof. Garib N. Murshudov.',
    'og:type': 'website',
    'og:url': 'https://carboxmol.readthedocs.io/en/latest/',
    'og:image': 'https://carboxmol.github.io/assets/carboxmol_logo.png',
    'twitter:card': 'summary_large_image',
    'twitter:title': 'CarboxMol Documentation | 3D Macromolecular Crystallography & GROMACS Suite',
    'twitter:description': 'Official scientific documentation for CarboxMol: 3D crystallography workbench, GROMACS molecular dynamics, and electron density analysis.',
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
html_extra_path = ['robots.txt', 'a8f4c2e91b7d3065e4a1f9c82d6b0731.txt']
html_title = 'CarboxMol Documentation'
html_logo = 'assets/carboxmol_logo.png'
html_favicon = 'assets/carboxmol_logo.png'

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
