# Python API Arayışı

Əsas ictimai obyektlər ən yuxarı səviyyəli `carboxmol` paketindən ixrac olunur. Bu səhifədə ən çox istifadə edilən modullar və giriş nöqtələri təqdim edilir.

---

## 1. Strukturlar və Həndəsə

```python
from carboxmol.core.structure import Structure, measure_distance

st = Structure.from_file("4LGN")      # Yerli fayl yolu və ya PDB ID
print(st.pdb_id, len(st.atoms))
```

| Modul | Əsas Obyektlər |
| :--- | :--- |
| `carboxmol.core.structure` | `Atom`, `Residue`, `Structure`, `ResidueSpec`, `measure_distance`, `measure_angle`, `measure_dihedral` |
| `carboxmol.core.geometry` | `calculate_center_of_mass`, `calculate_rmsd`, `calculate_bounding_box`, `calculate_inertia_tensor`, `kabsch_superpose` |
| `carboxmol.core.selection` | `SelectionQuery`, `select_structure_atoms` |
| `carboxmol.core.symmetry` | `UnitCell`, `SymmetryEngine` |
| `carboxmol.io` | `PDBIO`, `CIFIO`, `CXLIO`, `MapIO` |

---

## 2. Validasiya

| Modul | Əsas Obyektlər |
| :--- | :--- |
| `carboxmol.validation` | `run_validation_suite(atoms, resolution=1.80)` — `carboxmol validate` arxitekturası |
| `carboxmol.geometry` | `RamachandranValidator`, `RotamerEvaluator`, `OutlierDetector`, `StericClash`, `CBetaValidator`, `KabschAligner`, `GeometricMetrics` |

---

## 3. Metal Koordinasiyası

```python
from carboxmol.core.structure import Structure
from carboxmol.modeling.metal import find_all_metal_coordination_sites

sites = find_all_metal_coordination_sites(Structure.from_file("4LGN"), cutoff=3.10)
for s in sites:
    print(s.element, s.chain, s.resi, s.coordination_number, s.geometry)
```

---

## 4. Qarşılıqlı Təsirlər

```python
from carboxmol.interactions import analyze_protein_ligand_interactions
report = analyze_protein_ligand_interactions(atoms, ligand_resn="LIG")
```

---

## 5. Dəqiqləşdirmə və Məhdudiyyətlər

| Modul | Əsas Obyektlər |
| :--- | :--- |
| `carboxmol.refinement` | `real_space_regularize(atoms, chain=None, resi_start=None, resi_end=None, iterations=40)`, `export_pdb_string(atoms)` |
| `carboxmol.ideal` | `StereochemicalEnergy`, `AnalyticalGradients`, `RealSpaceMinimizer` |
| `carboxmol.restraints` | `ExternalRestraints`, `ProtonationRestraints`, `HBondRestraints`, `CovalentLinkRestraints`, `AceDRGLinkGenerator` |
| `carboxmol.refine` | `RefinementPipeline`, `RefinementAdapter`, `OmitMapGenerator` |

---

## 6. Elektron Sıxlığı Xəritələri

| Modul | Əsas Obyektlər |
| :--- | :--- |
| `carboxmol.io.maps` | CCP4/MRC başlıq analizi |
| `carboxmol.density.map_parser` | `CCP4MapHeader` |
| `carboxmol.density.isosurface` | `DensityIsosurface.extract_mesh(grid, cell_dimensions, iso_level, origin)`, `IsosurfaceMesh` |

---

## 7. Skriptləşdirmə və GROMACS

| Modul | Əsas Obyektlər |
| :--- | :--- |
| `carboxmol.macro` | `parse_cxl_script`, `validate_cxl_script`, `CxlScript`, `CxlCommand` |
| `carboxmol.scripting` | `CXLInterpreter`, `MacroGenerator`, `HTMLReportGenerator` |
| `carboxmol.session.session_manager` | `SessionManager` |
| `carboxmol.gromacs` | `GromacsPipeline`, `PipelineConfig`, `GromacsMdpBuilder`, `GromacsProcessRunner`, `GromacsTrajectoryEngine`, `GromacsEnv` |
