# CARBOXMOL: THE DEFINITIVE TECHNICAL REFERENCE MANUAL

**3D Macromolecular Crystallography Workbench, WebGL Studio, Real-Space Refinement & GROMACS Molecular Dynamics Suite**

---

### Authors & Scientific Direction
* **Suleiman M. Hajizadeh** — Lead Software Architect & Computational Structural Biologist
* **Prof. Garib N. Murshudov** — Senior Scientific Advisor, Head of Computational Structural Biology, MRC Laboratory of Molecular Biology (Cambridge, UK)

**Version:** 0.4.5  
**License:** Mozilla Public License 2.0 (MPL-2.0)  
**Official Web Studio:** [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html)  
**Documentation Portal:** [https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)  
**Source Repository:** [https://github.com/carboxmol/carboxmol](https://github.com/carboxmol/carboxmol)

---

## TABLE OF CONTENTS

1. [Prolegomena & Executive Summary](#1-prolegomena--executive-summary)
2. [Macromolecular Coordinate Architecture & Data Models](#2-macromolecular-coordinate-architecture--data-models)
3. [Interactive 3D WebGL Studio & Rendering Pipeline](#3-interactive-3d-webgl-studio--rendering-pipeline)
4. [Crystallographic Geometry & Stereochemical Validation](#4-crystallographic-geometry--stereochemical-validation)
5. [Real-Space Geometric Refinement & Regularization](#5-real-space-geometric-refinement--regularization)
6. [Bioinorganic Chemistry: Metal Coordination Polyhedra](#6-bioinorganic-chemistry-metal-coordination-polyhedra)
7. [Non-Covalent Interactions & Protein-Ligand Profiling](#7-non-covalent-interactions--protein-ligand-profiling)
8. [Electron Density Maps & Real-Space Carving](#8-electron-density-maps--real-space-carving)
9. [GROMACS Molecular Dynamics Simulation Suite](#9-gromacs-molecular-dynamics-simulation-suite)
10. [Carbox Crystallographic Language (CXL) Macro Automation](#10-carbox-crystallographic-language-cxl-macro-automation)
11. [Command-Line Interface (CLI) & Local Server Operations](#11-command-line-interface-cli--local-server-operations)
12. [Academic Citation & Ecosystem Interoperability](#12-academic-citation--ecosystem-interoperability)

---

## 1. Prolegomena & Executive Summary

The **CarboxMol Structural Biology Platform** provides a modern, high-performance computational environment for 3D macromolecular crystallography, biophysical visualization, and molecular dynamics simulations. It bridges crystallographic models with experimental electron density distributions and solution-phase biophysical simulations.

### Key Pillars
* **Universal 3D Visualization:** In-browser WebGL Studio supporting assemblies of over 100,000 atoms at 60 FPS.
* **Crystallographic Validation:** MolProbity-style stereochemical audits, Ramachandran distributions, sidechain rotamer outliers, and steric clashscores.
* **Real-Space Refinement:** Torsion-angle and bond-length regularization via harmonic restraint minimization.
* **Metal Chemistry:** Quantitative classification of transition and divalent metal polyhedra (tetrahedral, square planar, octahedral).
* **GROMACS MD Pipeline:** Automated eight-stage simulation pipeline from topology generation to trajectory extraction.
* **CXL Scripting:** Domain-specific macro language for batch automation and reproducible scientific workflows.

---

## 2. Macromolecular Coordinate Architecture & Data Models

CarboxMol represents biological assemblies via an object hierarchy in `carboxmol.core`:

```text
Structure (PDB/mmCIF Entry, UnitCell, Space Group, Symmetry)
  └── Model (NMR Ensemble Index or Crystallographic State)
        └── Chain (Polypeptide, Nucleic Acid, Ligand, Solvent)
              └── Residue (ResidueSpec, Standard / Non-Standard)
                    └── Atom (Cartesian [x, y, z], Element, B-Factor, Occupancy)
```

### Primary Core Classes
* **`Structure` (`carboxmol.core.structure`):** Root macromolecular container. Instantiated via `Structure.from_file(path_or_pdb_id)`. Provides access to unit cell parameters, symmetry operations, chains, residues, and atom lists.
* **`Atom` (`carboxmol.core.structure`):** Represents an atomic centre with fractional and orthogonal coordinates, anisotropic displacement parameters, and occupancy values.
* **`UnitCell` & `SymmetryEngine` (`carboxmol.core.symmetry`):** Crystallographic unit cell dimensions ($a, b, c, \alpha, \beta, \gamma$), de-orthogonalization matrices, and crystallographic space group symmetry operators.
* **Spatial Geometry (`carboxmol.core.geometry`):** Minimum-RMSD Kabsch structural superposition, centre-of-mass calculation, bounding box analysis, and inertia tensor evaluation.

---

## 3. Interactive 3D WebGL Studio & Rendering Pipeline

The **CarboxMol Studio** (`studio.html`) is a hardware-accelerated WebGL application available both offline as a Progressive Web App (PWA) and served locally via `carboxmol server`.

### Visual Representations
* **Cartoon Ribbons:** Spline-interpolated backbone traces with $\alpha$-helix cylinders and $\beta$-strand directional arrows.
* **Ball-and-Stick / Sticks:** Covalent bonds rendered as instanced cylinders with atom-centred spheres.
* **CPK Spheres:** Van der Waals surfaces scaled to full atomic radii for steric clash evaluation.
* **Solvent-Accessible Surface:** Connolly and Gaussian molecular surfaces colored by electrostatic potential or hydrophobicity.
* **Electron Density Mesh:** Isosurface wireframes triangulated dynamically from 3D scalar density arrays.

### Navigation Controls
* **Left-Click Drag:** Rotates the model around the centre of mass.
* **Right-Click Drag:** Translates (pans) the camera within the viewing plane.
* **Scroll Wheel:** Zoom along the viewing axis.
* **Double Click:** Centers camera focus onto the selected atom.
* **Shift + Scroll:** Modifies front and back clipping planes (slab depth cuing).

---

## 4. Crystallographic Geometry & Stereochemical Validation

The validation engine in `carboxmol.validation` evaluates macromolecular structures against high-resolution empirical targets:

```python
from carboxmol.validation import run_validation_suite

report = run_validation_suite(atoms, resolution=1.80)
```

### Evaluation Metrics
* **Clashscore:** Number of serious steric overlaps ($> 0.40\,\text{Å}$) per 1,000 atoms.
* **Ramachandran Distribution:** Backbone $\phi, \psi$ dihedral evaluation against favored, allowed, and outlier regions.
* **Sidechain Rotamers:** $\chi_1, \chi_2, \chi_3, \chi_4$ torsion-angle evaluation against the Richardson rotamer library.
* **Covalent Geometry:** Root-mean-square $Z$-scores (RMSZ) for bond lengths and valence angles against Engh & Huber stereochemical dictionaries.
* **$B$-Factor Distribution:** Mean and maximum isotropic displacement parameters.

---

## 5. Real-Space Geometric Refinement & Regularization

Real-space regularization relieves non-physical steric contacts and optimizes bond geometries:

```python
from carboxmol.refinement import real_space_regularize

refined = real_space_regularize(atoms, chain="A", resi_start=20, resi_end=35, iterations=40)
```

### Minimization Methods
* **Stereochemical Restraint Functions:** Target bond lengths $d_0$, bond angles $\theta_0$, and planar groups are restrained harmonically:
  $$E_{\text{geom}} = \sum_{\text{bonds}} k_b (d - d_0)^2 + \sum_{\text{angles}} k_\theta (\theta - \theta_0)^2 + \sum_{\text{clashes}} k_{\text{rep}} (r_{\text{vdw}} - d)^4$$
* **Zone Selection:** Regularization can be targeted to specific chains or residue intervals (`--chain`, `--start`, `--end`).
* **LBHB Distance Restraints:** Optional target distance restraints (`--target-dist`) for anomalous carboxylate oxygen pairs ($d_{O\cdots O} \le 2.55\,\text{Å}$).

---

## 6. Bioinorganic Chemistry: Metal Coordination Polyhedra

CarboxMol classifies transition and divalent metal binding sites ($\text{Zn}^{2+}, \text{Mg}^{2+}, \text{Ca}^{2+}, \text{Fe}^{2+}/\text{Fe}^{3+}, \text{Mn}^{2+}, \text{Cu}^{2+}$):

```python
from carboxmol.core.structure import Structure
from carboxmol.modeling.metal import find_all_metal_coordination_sites

sites = find_all_metal_coordination_sites(Structure.from_file("4LGN"), cutoff=3.10)
```

### Polyhedral Geometries
* **4-Fold Polyhedra:** Evaluates tetrahedral ($T_d$, ideal angle $109.5^\circ$) versus square planar ($D_{4h}$, ideal angles $90^\circ, 180^\circ$) geometries using the $\tau_4$ geometry index:
  $$\tau_4 = \frac{360^\circ - (\alpha + \beta)}{141^\circ}$$
* **6-Fold Polyhedra:** Evaluates octahedral ($O_h$, ideal angles $90^\circ, 180^\circ$) coordination spheres.
* **Donor Classification:** Identifies carboxylate donors (Asp O$\delta$, Glu O$\varepsilon$), histidine imidazole nitrogens (N$\delta_1$, N$\varepsilon_2$), cysteine thiolates (S$\gamma$), and coordinating water molecules.

---

## 7. Non-Covalent Interactions & Protein-Ligand Profiling

The interaction profiler in `carboxmol.interactions` detects non-covalent contacts:

```python
from carboxmol.interactions import analyze_protein_ligand_interactions

report = analyze_protein_ligand_interactions(atoms, ligand_resn="LIG")
```

### Contact Classes
* **Salt Bridges:** Inter-atomic distance $d \le 4.0\,\text{Å}$ between basic nitrogen atoms (Arg N$\eta$, Lys N$\zeta$, His N$\varepsilon$) and acidic oxygens (Asp O$\delta$, Glu O$\varepsilon$).
* **Hydrogen Bonds:** Donor-acceptor distance $d \le 3.5\,\text{Å}$ with angular cutoff $> 120^\circ$.
* **$\pi\text{--}\pi$ Stacking:** Face-to-face and edge-to-face aromatic interactions between phenylalanine, tyrosine, tryptophan, and ligand aromatic rings.
* **Cation--$\pi$ Contacts:** Quaternary ammonium or guanidinium groups interacting with aromatic $\pi$-systems.

---

## 8. Electron Density Maps & Real-Space Carving

CarboxMol decodes standard binary CCP4/MRC density maps (Mode 2: 32-bit floating point) and generates real-space triangulated isosurfaces:

```python
from carboxmol.density.isosurface import DensityIsosurface

mesh = DensityIsosurface.extract_mesh(
    grid=density_3d_array,
    cell_dimensions=(a, b, c),
    iso_level=1.5,
    origin=(0.0, 0.0, 0.0)
)
```

### Active Site Density Carving
To optimize rendering performance, density maps can be carved locally around selected coordinates $\mathbf{r}_0$ within a radius $R_{\text{carve}}$ ($5.0 - 8.0\,\text{Å}$), isolating catalytic active sites or ligand pockets from the broader crystal unit cell.

---

## 9. GROMACS Molecular Dynamics Simulation Suite

CarboxMol drives local GROMACS installations via `carboxmol.gromacs.GromacsPipeline`:

```python
from carboxmol.gromacs import GromacsPipeline, PipelineConfig

cfg = PipelineConfig(
    forcefield="amber99sb-ildn",
    water_model="spce",
    box_type="cubic",
    box_clearance_nm=1.0,
    salt_concentration_m=0.15,
    prod_duration_ns=1.0
)
pipe = GromacsPipeline(workdir="md_workspace", config=cfg)
results = pipe.run_full_pipeline("structure.pdb")
```

### Eight Automated Stages
1. **`stage_1_prepare_topology`:** `pdb2gmx` topology construction with chosen force field and water model.
2. **`stage_2_define_box`:** `editconf` simulation cell definition with defined clearance.
3. **`stage_3_solvate`:** `solvate` water addition into the box.
4. **`stage_4_neutralize_and_add_salt`:** `genion` charge neutralization and physiological ionic strength (0.15 M NaCl).
5. **`stage_5_energy_minimization`:** Steepest-descent minimization ($F_{\text{max}} < 1000\,\text{kJ/mol/nm}$).
6. **`stage_6_nvt_equilibration`:** Canonical ensemble equilibration at 300 K.
7. **`stage_7_npt_equilibration`:** Isothermal-isobaric equilibration at 1.0 bar.
8. **`stage_8_production_md`:** Leap-frog MD integration with PME electrostatics and LINCS constraints.

---

## 10. Carbox Crystallographic Language (CXL) Macro Automation

CXL (`.cxl`) provides plain-text, scriptable macro automation for CarboxMol:

```text
# Macro script example
load 4LGN.cif
select active_site chain A and resi 94,96,119,262
measure distance A:ASP25:OD2 A:GLU102:OE2
metal 4LGN.cif --cutoff 3.10
refine 4LGN.cif --chain A --start 20 --end 30 --cycles 40 -o refined.pdb
```

Scripts are validated via `validate_cxl_script(text)` and executed either through `carboxmol script pipeline.cxl` or the `POST /api/cxl/run` HTTP endpoint.

---

## 11. Command-Line Interface (CLI) & Local Server Operations

The `carboxmol` command-line utility provides direct access to all major subsystems:

```bash
# Launch interactive 3D WebGL Studio
carboxmol 4LGN

# Run stereochemical and geometric validation
carboxmol validate 4LGN

# Profile protein-ligand interactions
carboxmol pli 4LGN --ligand 017

# Classify metal coordination polyhedra
carboxmol metal 4LGN --cutoff 2.80

# Perform real-space geometric refinement
carboxmol refine 4LGN --chain A --start 20 --end 30 -o refined.pdb

# Execute CXL macro script
carboxmol script pipeline.cxl

# Start headless microservices server
carboxmol server --host 127.0.0.1 --port 8050 --no-browser
```

---

## 12. Academic Citation & Ecosystem Interoperability

When utilizing CarboxMol in scientific investigations, cite:

> **Suleiman M. Hajizadeh & Prof. Garib N. Murshudov (2026).**  
> *CarboxMol: Universal 3D Macromolecular Crystallography Workbench, Interactive WebGL Studio, and GROMACS Molecular Dynamics Simulation Suite.*  
> **CarboxMol Structural Biology Platform**, v0.4.5.  
> [https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)

### Ecosystem Links
For algorithmic screening of anomalous carboxylate protonation states and low-barrier hydrogen bonds across large crystallographic archives, CarboxMol interoperates with **Project Carbox**. Documentation for Project Carbox is maintained separately at:  
[https://project-carbox.readthedocs.io/en/latest/](https://project-carbox.readthedocs.io/en/latest/)
