# CXL Macro Scripting

CXL (`.cxl`) is the plain-text macro language of CarboxMol. Scripts can be run from the terminal with `carboxmol script file.cxl`, from the Studio console, or through the local server endpoint `POST /api/cxl/run`.

---

## 1. Syntax

* One command per line; the first token is the command verb.
* Blank lines are ignored. Lines starting with `#` are comments; a comment of the form `# Key: value` is stored as script metadata.
* Arguments are split with shell-style quoting. Tokens of the form `--name=value` become keyword arguments (numbers and `true`/`false` are converted automatically); `--flag` alone is a boolean.

---

## 2. Recognised Commands

| Group | Verbs |
| :--- | :--- |
| Loading | `load`, `load_structure`, `load_cif`, `load_file`, `fetch`, `fetch_pdb`, `open` |
| Density | `density`, `density_map`, `load_density`, `map_fetch`, `map_contour` |
| Selection and camera | `select`, `select_pair`, `focus_pocket`, `focus_residue`, `zoom`, `zoom_pair`, `center`, `center_camera`, `set_active_site` |
| Measurement | `measure`, `measure_distance`, `measure_dist`, `distance`, `measure_angle`, `measure_dihedral` |
| Display | `style_cartoon`, `style_sticks`, `style_waters`, `color`, `show`, `hide`, `surface`, `set_view_preset`, `set_background_color`, `set` |
| Chemistry and validation | `protonate`, `model_protonation_state`, `set_proton_state`, `audit`, `audit_atoms`, `validate`, `metal`, `pli` |
| Restraints and refinement | `restrain`, `restraint_distance`, `export_restraints`, `refine`, `regularize`, `simulate` |
| Output | `export`, `save` |

Unrecognised verbs are reported as validation errors before execution.

---

## 3. Example (`examples/pipeline.cxl`)

```text
# CarboxMol Macro: Automated Active-Site Validation & Restraint Generation
# Workflow: 4LGN HIV-1 Protease Catalytic Dyad Audit
load 4LGN.cif
select carboxyl_dyad resn ASP,GLU and chain A and resi 25,214
measure distance carboxyl_dyad cutoff 3.20
audit carboxyl_dyad
restrain carboxyl_dyad target 2.49 sigma 0.02 out 4LGN_lbhb.txt
save session 4LGN_audit.cxs
```

---

## 4. Python Access

```python
from carboxmol.macro import parse_cxl_script, validate_cxl_script

text = open("examples/pipeline.cxl").read()
report = validate_cxl_script(text)      # {'is_valid', 'errors', 'warnings', 'command_count', 'metadata'}
script = parse_cxl_script(text)         # CxlScript with .commands and .metadata
print(script.to_json())

from carboxmol.scripting import CXLInterpreter
results = CXLInterpreter().execute_script(text)
```
