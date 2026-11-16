# CarboxMol Command-Line Interface (CLI)

The `carboxmol` command is installed together with the Python package (`pip install -e .` inside the `carboxmol` repository). All subcommands accept either a local PDB/mmCIF file or a 4-character PDB ID, which is fetched from the RCSB PDB.

```bash
carboxmol [--version] [--host HOST] [--port PORT] [--no-browser] [SUBCOMMAND | PDB_ID] ...
```

| Subcommand | Purpose |
| :--- | :--- |
| `server` | Launch the CarboxMol WebGL2 3D Studio server |
| `validate` | Geometry, Ramachandran, rotamer and clash validation |
| `pli` | Protein-ligand interaction profiling |
| `metal` | Classification of 4-fold and 6-fold metal coordination spheres |
| `refine` | Real-space geometry regularization of a structure or zone |
| `script` | Parse, validate and execute a `.cxl` macro script |

---

## 1. Launching the Studio

```bash
# Start the Studio on http://127.0.0.1:8050 and open the browser
carboxmol

# Shorthand: start the Studio with a PDB entry preloaded
carboxmol 4LGN

# Equivalent explicit form with a custom host/port and no browser
carboxmol server 4LGN --host 0.0.0.0 --port 8080 --no-browser
```

Any first argument that is not a known subcommand is treated as a PDB ID and passed to `carboxmol server`.

> **Troubleshooting:** if the shell reports `ModuleNotFoundError: No module named 'carboxmol'`, the `carboxmol` launcher was installed by a different Python interpreter than the one that has the package. Reinstall inside the intended environment (`python -m pip install -e .` from the repository root) or run `python -m carboxmol.cli 4LGN` with that interpreter.

---

## 2. `carboxmol validate`

```bash
carboxmol validate 4LGN
carboxmol validate model.cif
```

Reports the overall quality verdict, clashscore, Ramachandran and rotamer favoured percentages, bond-length and bond-angle RMSZ, mean/max B-factor and short carboxyl dyads with suggested restraints.

---

## 3. `carboxmol pli`

```bash
carboxmol pli 4LGN --ligand 017
carboxmol pli model.pdb --ligand LIG --chain A --resi 401
```

| Option | Meaning |
| :--- | :--- |
| `--ligand` | 3-letter ligand residue name |
| `--chain` | Chain ID of the ligand |
| `--resi` | Residue number of the ligand |

If no ligand is specified, the first organic heterogen in the file is profiled.

---

## 4. `carboxmol metal`

```bash
carboxmol metal 4LGN
carboxmol metal model.pdb --cutoff 2.80
```

`--cutoff` sets the maximum donor-metal distance in Å (default `3.10`). For each metal centre the output lists the coordination number, geometry class with angular RMSD, mean bond distance, coordinating ligands (carboxyl, imidazole, water or other donor) and suggested restraints.

---

## 5. `carboxmol refine`

```bash
carboxmol refine 4LGN --chain A --start 20 --end 30 --cycles 40 -o 4LGN_reg.pdb
```

| Option | Default | Meaning |
| :--- | :--- | :--- |
| `--chain` | all | Chain to regularize |
| `--start`, `--end` | all | Residue range |
| `--cycles` | `40` | Refinement cycles |
| `--iterations` | — | Explicit iteration count (overrides cycles) |
| `--target-dist` | — | Target O–O restraint distance (Å) for short carboxyl contacts |
| `--weight-geom` | `1.5` | Geometric restraint weight |
| `-o`, `--out`, `--output` | — | Output PDB path |

---

## 6. `carboxmol script`

```bash
carboxmol script examples/pipeline.cxl
```

Validates the script syntax and recognised commands, then executes it. See the CXL chapter for the language.
