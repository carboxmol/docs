<div align="center">

# 📚 Carbox & CarboxMol Documentation

[![Read the Docs](https://img.shields.io/badge/📚_Documentation-carboxmol.readthedocs.io-0284c7?style=for-the-badge&logo=read-the-docs&logoColor=white)](https://carboxmol.readthedocs.io/en/latest/)
[![Organization](https://img.shields.io/badge/GitHub_Org-@carboxmol-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/carboxmol)
[![Live Studio](https://img.shields.io/badge/🌐_Live_Studio-carboxmol.github.io-06b6d4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://carboxmol.github.io)
[![License: MPL-2.0](https://img.shields.io/badge/License-MPL_2.0-blue?style=for-the-badge)](LICENSE)

### Official Scientific & Technical Documentation Repository for Carbox & CarboxMol

</div>

---

## 🌐 Live Documentation

The comprehensive Sphinx documentation is built automatically and hosted on **Read the Docs**:

👉 **[https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)**

---

## 📖 Content Overview

This repository hosts the Sphinx documentation source files (`.rst` and MyST `.md`), structured into:

1. **Trilingual Manuals (100% Parity):**
   - 🇬🇧 **English:** `docs/en/`
   - 🇦🇿 **Azərbaycan dili:** `docs/az/`
   - 🇮🇱 **עברית (RTL):** `docs/he/`
2. **Biophysical Theory:** Anomalous carboxyl protonation ($\Delta\text{p}K_a > 3.0$), low-barrier hydrogen bonds (LBHBs, $d \le 2.55\text{ \AA}$), and microenvironment dielectric shielding.
3. **Murshudov 6-Stage Gate Protocol:** Sub-angstrom resolution criteria, ground-state occupancy law ($occ = 1.00$), thermal $B$-factor audit ($B_z \le 5.0\sigma$), real-space density correlation ($\text{RSCC} \ge 0.80$), and 70-cation metal screening.
4. **Refinement Restraints:** AceDRG/REFMAC5 external distance restraints and Servalcat Cryo-EM formatting.
5. **Python API & CLI Reference:** Command-line options (`--pka`, `--geom`, `--batch`) and `.cxl` macro scripting.
6. **Master Manual & Golden Benchmarks:** `CARBOX_MASTER_MANUAL.md` with analytical dossiers for 3X2M, 5SAO, 8PO0, 8W8U, 1G33, and 1I10.

---

## 🛠️ Local Build Instructions

To build the documentation locally with Sphinx:

```bash
# 1. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install requirements
pip install -r docs/requirements.txt

# 3. Build HTML
sphinx-build -b html docs docs/_build/html

# 4. Open in browser
open docs/_build/html/index.html
```

---

## 🔒 Private Code & Data Notice

The core scientific calculation algorithms, 3D WebGL rendering engine, and raw crystallographic datasets reside in the private repositories of the **[CarboxMol Organization](https://github.com/carboxmol)**.

To request access for academic research or peer review:  
📧 **[suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20CarboxMol%20Private%20Data)**
