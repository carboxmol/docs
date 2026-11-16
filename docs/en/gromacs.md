# GROMACS Molecular Dynamics

CarboxMol drives a locally installed GROMACS (`gmx`) through the `carboxmol.gromacs` package and exposes the same pipeline in the Studio through the local server. GROMACS itself is not bundled and must be available on `PATH` (or passed via `gmx_path`).

---

## 1. Pipeline Stages

`GromacsPipeline` runs eight stages:

| Stage | Method | GROMACS step |
| :--- | :--- | :--- |
| 1 | `stage_1_prepare_topology` | `pdb2gmx` topology with the chosen force field and water model |
| 2 | `stage_2_define_box` | `editconf` simulation box |
| 3 | `stage_3_solvate` | `solvate` |
| 4 | `stage_4_neutralize_and_add_salt` | `genion` neutralisation and salt |
| 5 | `stage_5_energy_minimization` | steepest-descent EM |
| 6 | `stage_6_nvt_equilibration` | NVT equilibration |
| 7 | `stage_7_npt_equilibration` | NPT equilibration |
| 8 | `stage_8_production_md` | production MD |

`run_full_pipeline(input_pdb)` executes all stages in order.

---

## 2. Configuration (`PipelineConfig`)

| Field | Default |
| :--- | :--- |
| `job_name` | `"carboxmol_md"` |
| `forcefield` | `"amber99sb-ildn"` |
| `water_model` | `"spce"` |
| `box_type` | `"cubic"` |
| `box_clearance_nm` | `1.0` |
| `salt_concentration_m` | `0.15` |
| `positive_ion` / `negative_ion` | `"NA"` / `"CL"` |
| `temperature_k` | `300.0` |
| `pressure_bar` | `1.0` |
| `em_nsteps` / `em_tolerance` | `500` / `1000.0` |
| `nvt_duration_ps` / `npt_duration_ps` | `10.0` / `100.0` |
| `prod_duration_ns` | `1.0` |
| `write_interval_ps` | `10.0` |
| `ignore_hydrogens` | `True` |
| `posres_heavy_atoms` | `True` |

---

## 3. Python Example

```python
from carboxmol.gromacs import GromacsPipeline, PipelineConfig

cfg = PipelineConfig(forcefield="amber99sb-ildn", water_model="spce",
                     prod_duration_ns=1.0)
pipe = GromacsPipeline(workdir="md_4LGN", config=cfg)
result = pipe.run_full_pipeline("4LGN.pdb")
```

---

## 4. Server Endpoints

When `carboxmol server` is running, the Studio uses:

| Method | Endpoint | Purpose |
| :--- | :--- | :--- |
| `GET` | `/api/gromacs/info` | Detect the local GROMACS installation |
| `POST` | `/api/gromacs/run` | Start a job (`pdb_id` or `pdb_text`, `forcefield`, `water_model`, `box_type`, `box_clearance_nm`, `salt_conc`, `duration_ns`, `stages`) |
| `GET` | `/api/gromacs/status/<job_id>` | Job progress and logs |
| `POST` | `/api/gromacs/cancel` | Cancel a running job |
| `POST` | `/api/gromacs/script` | Generate an equivalent shell script |
| `GET` | `/api/gromacs/file/<job_id>/<name>` | Download output files |
