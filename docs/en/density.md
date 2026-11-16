# Electron Density Map Viewing & Real-Space Carving

**CCP4/MRC Binary Map Interpretation, $\sigma$-Contour Leveling & Active Site Carving**

---

## 1. Crystallographic Electron Density Maps

In macromolecular X-ray crystallography, atomic models are validated and refined against experimental electron density distributions $\rho(\mathbf{r})$ synthesized via Fourier transformation of observed structure factor amplitudes $|F_o|$ and model-calculated phases $\alpha_c$:

$$\rho(\mathbf{r}) = \frac{1}{V} \sum_{\mathbf{h}} |F(\mathbf{h})| \exp[-2\pi i \mathbf{h} \cdot \mathbf{r} + i \alpha(\mathbf{h})]$$

### Standard Map Types Supported
* **$2mF_o - DF_c$ Map (Maximum Likelihood Weighted):** Represents the primary reconstructed electron density, where $m$ is the figure of merit and $D$ is the Luzzati coordinate error factor. Standard visualization level is $1.0\sigma - 1.5\sigma$.
* **$mF_o - DF_c$ Difference Map:** Identifies discrepancies between the experimental diffraction data and the atomic model. Positive density ($+3.0\sigma$, green mesh) indicates unmodeled atoms, bound water molecules, or ions. Negative density ($-3.0\sigma$, red mesh) indicates model errors, erroneous atom placement, or partial occupancy.

---

## 2. Binary Map File Formats

CarboxMol natively decodes and visualizes industry-standard binary density formats:

| Format | Specification | Features |
| :--- | :--- | :--- |
| **CCP4** | Standard crystallographic map format (Mode 2: 32-bit floating point) | Header contains unit cell dimensions ($a, b, c, \alpha, \beta, \gamma$), grid size ($N_x, N_y, N_z$), space group number, and mean/RMS statistics. |
| **MRC / MRC2014** | Universal electron microscopy format | Fully compatible with single-particle cryo-EM reconstructions and tomograms. |
| **DSym** | Compact density format for web streaming | Lightweight compression optimized for rapid WebGL rendering in browser sessions. |

---

## 3. Real-Space Density Carving

Rendering entire macromolecular unit cells creates excessive GPU overhead and visual clutter. CarboxMol features a dynamic **Real-Space Map Carver** that extracts localized density spheres:

### Carving Algorithm
Given a selection center $\mathbf{r}_0$ and a user-defined carving radius $R_{\text{carve}}$ (typically $5.0 - 8.0\,\text{Å}$):
$$\mathcal{V}_{\text{carved}} = \{ \mathbf{r} \in \mathcal{V} \mid \|\mathbf{r} - \mathbf{r}_0\| \le R_{\text{carve}} \}$$

Density voxels outside the carving sphere are clipped, leaving a clean, focused isocontour cage centered precisely on:
* Catalytic dyads and active site residues.
* Coordinated transition metal polyhedra.
* Bound drugs, cofactors, and prospective small-molecule ligands.

---

## 4. WebGL Density Mesh Visualization

Within CarboxMol Studio, density maps are triangulated on-the-fly using an optimized Marching Cubes implementation:

```text
Density Voxel Grid (Nx x Ny x Nz)
  └── Trilinear Interpolation at query points
        └── Marching Cubes Surface Triangulation at user sigma
              └── Hardware-Accelerated Wireframe / Smooth Surface Shaders
```

### Studio Density Controls
* **$\sigma$-Level Slider:** Adjust the contour threshold continuously from $0.5\sigma$ to $6.0\sigma$.
* **Carving Radius:** Expand or contract the active site visualization sphere ($2.0 - 15.0\,\text{Å}$).
* **Color Customization:** Configure independent wireframe colors and opacities for $2mF_o - DF_c$ (default: cyan) and $mF_o - DF_c$ (default: green/red).
