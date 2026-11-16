# ממשק תכנות היישומים (Python API) של CarboxMol

האובייקטים הציבוריים העיקריים מיוצאים מתוך חבילת העל `carboxmol`. עמוד זה מרכז את המודולים ונקודות הכניסה הנפוצות ביותר.

---

## 1. מבנים וגאומטריה מרחבית

```python
from carboxmol.core.structure import Structure, measure_distance

st = Structure.from_file("4LGN")      # נתיב לקובץ מקומי או קוד PDB
print(st.pdb_id, len(st.atoms))
```

| מודול | אובייקטים עיקריים |
| :--- | :--- |
| `carboxmol.core.structure` | `Atom`, `Residue`, `Structure`, `ResidueSpec`, `measure_distance`, `measure_angle`, `measure_dihedral` |
| `carboxmol.core.geometry` | `calculate_center_of_mass`, `calculate_rmsd`, `calculate_bounding_box`, `calculate_inertia_tensor`, `kabsch_superpose` |
| `carboxmol.core.selection` | `SelectionQuery`, `select_structure_atoms` |
| `carboxmol.core.symmetry` | `UnitCell`, `SymmetryEngine` |
| `carboxmol.io` | `PDBIO`, `CIFIO`, `CXLIO`, `MapIO` |

---

## 2. אימות סטריאוכימי

| מודול | אובייקטים עיקריים |
| :--- | :--- |
| `carboxmol.validation` | `run_validation_suite(atoms, resolution=1.80)` — מנוע הבדיקה של `carboxmol validate` |
| `carboxmol.geometry` | `RamachandranValidator`, `RotamerEvaluator`, `OutlierDetector`, `StericClash`, `CBetaValidator`, `KabschAligner`, `GeometricMetrics` |

---

## 3. קואורדינציה של מתכות

```python
from carboxmol.core.structure import Structure
from carboxmol.modeling.metal import find_all_metal_coordination_sites

sites = find_all_metal_coordination_sites(Structure.from_file("4LGN"), cutoff=3.10)
for s in sites:
    print(s.element, s.chain, s.resi, s.coordination_number, s.geometry)
```

---

## 4. אינטראקציות חלבון-ליגנד

```python
from carboxmol.interactions import analyze_protein_ligand_interactions
report = analyze_protein_ligand_interactions(atoms, ligand_resn="LIG")
```

---

## 5. עידון ורגולריזציה במרחב האמיתי

| מודול | אובייקטים עיקריים |
| :--- | :--- |
| `carboxmol.refinement` | `real_space_regularize(atoms, chain=None, resi_start=None, resi_end=None, iterations=40)`, `export_pdb_string(atoms)` |
| `carboxmol.ideal` | `StereochemicalEnergy`, `AnalyticalGradients`, `RealSpaceMinimizer` |
| `carboxmol.restraints` | `ExternalRestraints`, `ProtonationRestraints`, `HBondRestraints`, `CovalentLinkRestraints`, `AceDRGLinkGenerator` |
| `carboxmol.refine` | `RefinementPipeline`, `RefinementAdapter`, `OmitMapGenerator` |

---

## 6. מפות צפיפות אלקטרונים

| מודול | אובייקטים עיקריים |
| :--- | :--- |
| `carboxmol.io.maps` | פענוח כותרות מפות CCP4/MRC |
| `carboxmol.density.map_parser` | `CCP4MapHeader` |
| `carboxmol.density.isosurface` | `DensityIsosurface.extract_mesh(grid, cell_dimensions, iso_level, origin)`, `IsosurfaceMesh` |

---

## 7. תסריטי CXL ודינמיקה מולקולרית GROMACS

| מודול | אובייקטים עיקריים |
| :--- | :--- |
| `carboxmol.macro` | `parse_cxl_script`, `validate_cxl_script`, `CxlScript`, `CxlCommand` |
| `carboxmol.scripting` | `CXLInterpreter`, `MacroGenerator`, `HTMLReportGenerator` |
| `carboxmol.session.session_manager` | `SessionManager` |
| `carboxmol.gromacs` | `GromacsPipeline`, `PipelineConfig`, `GromacsMdpBuilder`, `GromacsProcessRunner`, `GromacsTrajectoryEngine`, `GromacsEnv` |
