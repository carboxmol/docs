# Carbox & CarboxMol Documentation

### Official Scientific and Technical Documentation Repository

---

## 1. Authors and Academic Affiliations

* **Suleiman M. Hajizadeh**
  * *Institute of Molecular Biology, Ministry of Science and Education of the Republic of Azerbaijan*
  * *Western Caspian University, Baku, Azerbaijan*
* **Prof. Garib N. Murshudov**
  * *MRC Laboratory of Molecular Biology (LMB), Cambridge Biomedical Campus, Cambridge, United Kingdom*
* **Live Documentation (Read the Docs):** [https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)
* **Official Web Portal:** [https://carboxmol.github.io/](https://carboxmol.github.io/)
* **Primary Contact:** [suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com)

---

## 2. Content Overview

This repository hosts the Sphinx documentation source files (`.rst` and MyST `.md`), structured into:

1. **Trilingual Manuals:**
   * **English:** `docs/en/`
   * **Azerbaijani:** `docs/az/`
   * **Hebrew (RTL):** `docs/he/`
2. **Biophysical Theory:** Anomalous carboxyl protonation ($\Delta\text{p}K_a \ge +2.0$), low-barrier hydrogen bonds (LBHBs, $d \le 2.55\text{ \AA}$), and microenvironment dielectric shielding.
3. **Murshudov 6-Stage Validation Protocol:** Sub-angstrom resolution criteria, ground-state occupancy verification ($occ = 1.00$), thermal $B$-factor audit ($B_z \le 3.0\sigma$ and Tukey IQR fences), real-space density correlation ($\text{RSCC} \ge 0.85$), and 70-cation metal screening.
4. **Refinement Restraints:** AceDRG and REFMAC5 external distance restraints and Servalcat refinement configurations.
5. **Python API and CLI Reference:** Command-line options (`carbox` and `carboxmol`) and `.cxl` macro scripting.
6. **Master Manual and Golden Benchmarks:** `CARBOX_MASTER_MANUAL.md` with analytical benchmark records.

---

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

---

## 4. Private Code and Data Notice

The core scientific calculation algorithms, 3D WebGL rendering engine, and raw crystallographic datasets reside in the private repositories of the [CarboxMol Organization](https://github.com/carboxmol) and [Project Carbox Organization](https://github.com/project-carbox). To request access for academic research or peer review, please contact **[suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20CarboxMol%20Private%20Data)**.
