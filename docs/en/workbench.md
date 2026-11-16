# CarboxMol 3D Workbench & WebGL Studio

**Interactive Macromolecular Crystallography Visualization, Coordinate Editing & Real-Space Inspection**

---

## 1. Introduction to the Workbench

The **CarboxMol Workbench** provides a high-performance, WebGL-accelerated 3D environment engineered specifically for structural biology, macromolecular crystallography, and cryo-EM model inspection. It is available both as an embedded local server (`carboxmol server`) and as a standalone Progressive Web Application (PWA) at [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html).

### Primary Architecture
* **Hardware-Accelerated WebGL Engine:** Capable of rendering complex assemblies (>100,000 atoms) at 60 FPS using instanced geometry and optimized GLSL shaders.
* **Dual Projection Modes:** Instant toggling between Perspective projection (for structural exploration and presentation) and Orthographic projection (for precise geometric alignment and crystallographic measurements).
* **Progressive Web App (PWA):** Fully functional offline with client-side caching of coordinate parsers, color palettes, and shader pipelines.
* **Local File System Integration:** Direct drag-and-drop loading of `.pdb`, `.cif`, `.mmcif`, `.ccp4`, `.mrc`, and `.cxl` files with zero server round-trips.

---

## 2. Rendering Representations

CarboxMol Studio supports multiple simultaneous representation modes that can be targeted to specific chains, residues, or atom selections:

| Representation | Rendering Target | Primary Use Case |
| :--- | :--- | :--- |
| **Cartoon Ribbons** | Backbone C$\alpha$ trace with $\alpha$-helix cylinders and $\beta$-sheet arrows | Global protein fold and topology visualization |
| **Ball-and-Stick** | Atomic spheres with covalent bond cylinders | Ligand binding sites, catalytic residues, and active sites |
| **Wireframe / Lines** | Thin line vectors connecting bonded atoms | High-density backbone inspection and fast navigation |
| **CPK Spheres** | Full van der Waals atomic radii ($r_{\text{vdw}}$) | Steric clash detection and cavity filling analysis |
| **Solvent Surface** | Molecular surface (Connolly / Gaussian envelope) | Pocket shape, charge distribution, and hydrophobic patches |
| **Electron Density Mesh** | 3D wireframe isocontour at user-defined $\sigma$ | Real-space validation against experimental diffraction data |

---

## 3. Viewport Controls & Navigation

The 3D canvas supports intuitive multi-button mouse and touch gestures:

* **Rotate:** Left-click + Drag (or single-finger drag on touchscreens) rotates the camera around the current center of mass.
* **Translate (Pan):** Right-click + Drag (or two-finger drag) translates the camera in the screen-parallel plane.
* **Zoom:** Scroll wheel (or pinch-to-zoom) moves the camera along the view vector.
* **Center / Recenter:** Double-click on any atom or residue to re-center the camera rotation origin onto that coordinate.
* **Z-Clipping (Slab):** Shift + Scroll wheel adjusts the front and back clipping planes to isolate specific structural slices without visual occlusion.

---

## 4. Interactive Measurement Tools

### Distance Measurement
Clicking any two atoms activates the real-time distance ruler:
$$\Delta d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
The distance is displayed in Angstroms ($\text{Å}$) with sub-picometer precision alongside the interacting atom labels (e.g., `A:ASP25:OD2 -- A:GLU102:OE2: 2.45 Å`).

### Bond Angle & Torsion Angle Analysis
* **Angle:** Select three consecutive atoms ($A - B - C$) to calculate the inter-bond angle $\theta \in [0^\circ, 180^\circ]$.
* **Dihedral (Torsion):** Select four consecutive atoms ($A - B - C - D$) to calculate the dihedral angle $\phi \in [-180^\circ, +180^\circ]$, useful for validating peptide backbone $\phi, \psi$ angles against the Ramachandran distribution.

---

## 5. Multi-Model Handling & Superposition

CarboxMol Workbench provides native support for multi-model coordinate files:
* **NMR Ensembles:** Step through conformational ensembles sequentially or display all models superimposed with opacity blending.
* **Crystallographic Alternate Conformations:** Inspect alternate location identifiers (`altloc` A, B, C) with occupancy-weighted rendering.
* **Structure Alignment:** Superimpose homologous structures or wild-type/mutant pairs using Kabsch minimum-RMSD rotational superposition directly within the browser session.
