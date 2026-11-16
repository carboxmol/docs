# CarboxMol Əmr Sətri İnterfeysi (CLI)

`carboxmol` əmri Python paketi ilə birlikdə quraşdırılır (`carboxmol` repozitoriyasında `pip install -e .`). Bütün alt əmrlər həm yerli PDB/mmCIF faylını, həm də RCSB PDB-dən avtomatik endirilən 4 simvollu PDB kodunu qəbul edir.

```bash
carboxmol [--version] [--host HOST] [--port PORT] [--no-browser] [ALT_ƏMR | PDB_KODU] ...
```

| Alt Əmr | Təyinatı |
| :--- | :--- |
| `server` | CarboxMol WebGL2 3D Studio serverini işə salmaq |
| `validate` | Həndəsə, Ramachandran, rotamer və toqquşma validasiyası |
| `pli` | Zülal-liqand qarşılıqlı təsirlərinin profillənməsi |
| `metal` | 4-qat və 6-qat metal koordinasiya sferalarının təsnifatı |
| `refine` | Struktur və ya zonanın real fəzada həndəsi requlyarizasiyası |
| `script` | `.cxl` makro skriptini yoxlamaq və icra etmək |

---

## 1. Studio-nu İşə Salmaq

```bash
# Studio-nu http://127.0.0.1:8050 ünvanında açmaq
carboxmol

# PDB strukturu ilə Studio-nu birbaşa açmaq
carboxmol 4LGN

# Server rejimində fərqli port və host ilə işə salmaq
carboxmol server 4LGN --host 0.0.0.0 --port 8080 --no-browser
```

Əgər daxil edilən birinci arqument məlum alt əmr deyilsə, o PDB kodu kimi qəbul edilir və birbaşa `carboxmol server` rejiminə ötürülür.

---

## 2. `carboxmol validate`

```bash
carboxmol validate 4LGN
carboxmol validate model.cif
```

Ümumi keyfiyyət qərarı, clashscore, Ramachandran və rotamer paylanması, rabitə uzunluğu və bucaq RMSZ göstəriciləri, orta B-faktoru və yaxın karboksil cütlərini təqdim edir.

---

## 3. `carboxmol pli`

```bash
carboxmol pli 4LGN --ligand 017
carboxmol pli model.pdb --ligand LIG --chain A --resi 401
```

| Seçim | Mənası |
| :--- | :--- |
| `--ligand` | Liqandın 3 hərfli qalıq adı |
| `--chain` | Liqandın zəncir identifikatoru |
| `--resi` | Liqandın qalıq nömrəsi |

Liqand göstərilmədikdə, fayldakı birinci üzvi heterogen təhlil edilir.

---

## 4. `carboxmol metal`

```bash
carboxmol metal 4LGN
carboxmol metal model.pdb --cutoff 2.80
```

`--cutoff` donor-metal məsafə həddini ($\text{Å}$ ilə, standart: `3.10`) müəyyən edir. Hər bir metal mərkəzi üçün koordinasiya sayı, həndəsə sinfi, bucaq RMSD, orta rabitə məsafəsi və donor qruplar (karboksil, imidazol, su) çıxarılır.

---

## 5. `carboxmol refine`

```bash
carboxmol refine 4LGN --chain A --start 20 --end 30 --cycles 40 -o 4LGN_reg.pdb
```

| Seçim | Standart | Mənası |
| :--- | :--- | :--- |
| `--chain` | hamısı | Dəqiqləşdiriləcək zəncir |
| `--start`, `--end` | hamısı | Qalıq intervalı |
| `--cycles` | `40` | Dəqiqləşdirmə tsiklləri |
| `--iterations` | — | Aşkar iterasiya sayı |
| `--target-dist` | — | Karboksil O–O məsafə hədəfi ($\text{Å}$) |
| `--weight-geom` | `1.5` | Həndəsi məhdudiyyət çəkisi |
| `-o`, `--out`, `--output` | — | Çıxış PDB faylının yolu |

---

## 6. `carboxmol script`

```bash
carboxmol script examples/pipeline.cxl
```

Skriptin sintaksisini və tanınan əmrlərini yoxlayır, daha sonra icra edir.
