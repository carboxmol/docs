# CarboxMol Documentation

**Universal 3D Macromolecular Crystallography Workbench, Interactive WebGL Studio & GROMACS MD Simulation Suite**

**Authors:** Suleiman M. Hajizadeh & Prof. Garib N. Murshudov  
*Version:* 0.4.5  
*Platform:* CarboxMol Structural Biology Platform  
*Corresponding Author:* `suleyman.hacizade1@gmail.com`  
*Official Web Studio:* [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html)  
*Documentation Portal:* [https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)

---

## 1. Overview

**CarboxMol** is an open-source, universal 3D macromolecular crystallography workbench, real-space refinement engine, interactive WebGL visualization studio, and molecular dynamics simulation suite. It is engineered for crystallographers, biophysicists, and structural biologists who require rigorous atomic coordinate analysis, interactive electron density map carving, bioinorganic coordination geometry classification, and automated molecular dynamics workflows.

### Core Capabilities
* **Interactive 3D WebGL Studio & PWA:** High-performance hardware-accelerated molecular rendering supporting secondary structure cartoons, ribbons, sticks, CPK van der Waals spheres, transparent solvent-accessible surfaces, and clipping planes.
* **Electron Density Map Viewing & Carving:** Native binary CCP4/MRC/DSym map reading, dynamic $\sigma$-contour level slicing, and real-space local map carving ($2mF_o - DF_c$ and $mF_o - DF_c$) around selected residues, ligands, and catalytic sites.
* **Bioinorganic Metal Coordination Engine:** Automated detection and classification of transition and divalent metal coordination polyhedra ($\text{Zn}^{2+}, \text{Mg}^{2+}, \text{Ca}^{2+}, \text{Fe}^{2+}/\text{Fe}^{3+}, \text{Mn}^{2+}, \text{Cu}^{2+}$) into 4-fold (tetrahedral, square planar) and 6-fold (octahedral) geometries.
* **Non-Covalent Interaction Analysis (PLI):** Quantitative detection of salt bridges, $\pi\text{--}\pi$ stacking, cation--$\pi$ interactions, and hydrogen bonding networks.
* **Real-Space Geometric Refinement:** Torsion-angle and bond-distance regularization with iterative convergence reporting.
* **GROMACS Molecular Dynamics Suite:** End-to-end automated pipelines for structure topology generation, solvation, ionization, energy minimization (steepest descent / conjugate gradient), NVT/NPT equilibrations, and production MD trajectories.
* **CarboxMol Crystallographic Language (CXL):** Scriptable macro execution language for automated, reproducible batch modeling and structure manipulation.
* **Headless Terminal CLI & Microservices Server:** Direct command-line utility (`carboxmol`) and local server daemon for structural workflows.

---

## 2. Architecture & Data Model

CarboxMol is built on a hierarchical, memory-efficient atomic data model:

```text
Structure (PDB/mmCIF Entry, Space Group, Unit Cell)
  └── Model (NMR Ensemble or Crystallographic Alternate States)
        └── Chain (Polypeptide, Nucleic Acid, Solvent, Heterogen)
              └── Residue (Standard Amino Acid, Nucleotide, Ligand)
                    └── Atom (Coordinates [x, y, z], B-Factor, Occupancy, Element)
```

### Module Organization
* `carboxmol.core.structure`: Core object hierarchy with spatial KD-tree indexing for neighbor searches.
* `carboxmol.refinement`: Real-space geometric refinement and stereochemical regularization engine.
* `carboxmol.modeling.metal`: Polyhedral geometry classifier for metalloprotein active sites.
* `carboxmol.interactions`: Non-covalent protein-ligand and residue-residue contact network analyzer.
* `carboxmol.macro`: Interpreter and runtime parser for `.cxl` macro scripts.
* `carboxmol.density`: Binary CCP4/MRC parser, isocontour surface generator, and map carver.
* `carboxmol.gromacs`: GROMACS pipeline orchestrator and parameter generator.

---

## 3. Installation

### Prerequisites
* Python 3.9 through 3.14
* C++17 compatible compiler (optional, for accelerated coordinate routines)
* Node.js 18+ (for WebGL Studio build tools, optional)

### Standard Installation via Pip
```bash
pip install carboxmol
```

### Installation from Source Repository
```bash
git clone https://github.com/carboxmol/carboxmol.git
cd carboxmol
pip install -e .
```

### Verification
Verify the installation by querying version metadata and running self-checks:
```bash
carboxmol --version
python -c "import carboxmol; print('CarboxMol version:', carboxmol.__version__)"
```

---

## 4. Quickstart: Launching the Workbench

To launch the interactive 3D WebGL studio with a specific PDB structure directly from your terminal:

```bash
# Fetch and open human carbonic anhydrase II (PDB: 4LGN) in default browser
carboxmol 4LGN
```

To run a headless geometric validation on a local coordinate file:
```bash
carboxmol validate structure.pdb
```

To inspect metal coordination polyhedra:
```bash
carboxmol metal structure.pdb
```

---

## 5. Web Studio & Graphical Resources

* **Interactive WebGL Studio:** [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html)
* **Official Web Portal:** [https://carboxmol.github.io/](https://carboxmol.github.io/)
* **Source Code Repository:** [https://github.com/carboxmol/carboxmol](https://github.com/carboxmol/carboxmol)
