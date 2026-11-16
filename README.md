# CarboxMol Documentation

Official Scientific and Technical Documentation Repository for the CarboxMol Structural Biology Platform.

## 1. Author and Scientific Direction

* **Suleiman M. Hajizadeh** (Author and Developer): Institute of Molecular Biology, Ministry of Science and Education of the Republic of Azerbaijan; Western Caspian University, Baku, Azerbaijan
* **Prof. Garib N. Murshudov** (Scientific Advisor): MRC Laboratory of Molecular Biology (LMB), Cambridge Biomedical Campus, Cambridge, United Kingdom
* **Live Documentation (Read the Docs):** [https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)
* **Official Web Studio:** [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html)
* **Primary Contact:** [suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com)

## 2. Content Overview

This repository hosts the Sphinx documentation source files (`.rst` and MyST `.md`) for **CarboxMol**:

1. **Trilingual Manuals:**
   * **English (`docs/en/`):** Index, 3D Workbench & WebGL Studio, CLI, GROMACS MD Suite, Electron Density Maps, CXL Scripting, Python API, Citation.
   * **Azerbaijani (`docs/az/`):** İcmal, 3D İş Masası və WebGL Studio, CLI, GROMACS MD Simulyasiya Paketi, Elektron Sıxlığı Xəritələri, CXL ilə Skriptləşdirmə, Python API, İstinad.
   * **Hebrew (`docs/he/`):** מבוא, שולחן עבודה WebGL Studio, ממשק CLI, דינמיקה מולקולרית GROMACS, מפות צפיפות אלקטרונים, שפת תסריטי CXL, ממשק Python API, ציטוט מדעי.
2. **3D Crystallography Workbench & WebGL Studio:** High-performance hardware-accelerated molecular graphics supporting over 100,000 atoms at 60 FPS, with secondary structure cartoons, CPK spheres, ribbons, and solvent surfaces.
3. **Crystallographic Validation Suite:** MolProbity-style stereochemical audits, Ramachandran distributions, sidechain rotamers, steric clashscores, and covalent geometry RMSZ.
4. **Real-Space Geometric Refinement:** Torsion-angle regularization and harmonic restraint minimization.
5. **Bioinorganic Metal Coordination Engine:** Quantitative classification of 4-fold (tetrahedral, square planar) and 6-fold (octahedral) coordination spheres.
6. **Protein-Ligand Interaction Profiling (PLI):** Automated detection of salt bridges, $\pi\text{--}\pi$ stacking, and hydrogen bonding networks.
7. **Electron Density Map Viewing & Carving:** CCP4/MRC binary map decoding, dynamic $\sigma$-contour leveling, and localized real-space map carving around active sites.
8. **GROMACS Molecular Dynamics Suite:** Automated 8-stage simulation pipelines from topology generation to production MD trajectories.
9. **CarboxMol Crystallographic Language (CXL):** Domain-specific plain-text macro language for reproducible batch modeling.
10. **Technical Reference Manual:** `CARBOXMOL_USER_MANUAL.md`.

## 3. Local Build Instructions

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install requirements
pip install -r docs/requirements.txt

# 3. Build HTML documentation
sphinx-build -b html docs docs/_build/html
```
