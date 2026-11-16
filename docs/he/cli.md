# ממשק שורת הפקודה של CarboxMol (CLI)

הפקודה `carboxmol` מותקנת יחד עם חבילת הפייתון (`pip install -e .` בתוך מאגר `carboxmol`). כל תת-הפקודות מקבלות נתיב לקובץ PDB/mmCIF מקומי או קוד PDB בן 4 תווים הנמשך אוטומטית מ-RCSB PDB.

```bash
carboxmol [--version] [--host HOST] [--port PORT] [--no-browser] [SUBCOMMAND | PDB_ID] ...
```

| תת-פקודה | ייעוד |
| :--- | :--- |
| `server` | הפעלת שרת הסטודיו CarboxMol WebGL2 3D |
| `validate` | אימות גאומטרי, חישוב התנגשויות (clashes), וגרפי Ramachandran/Rotamers |
| `pli` | אפיון אינטראקציות חלבון-ליגנד (PLI) |
| `metal` | סיווג גאומטריות של ספירות תיאום מתכת (4 ו-6 תיאומים) |
| `refine` | רגולריזציה ועידון גאומטרי במרחב האמיתי |
| `script` | בדיקת תחביר והרצת תסריט מאקרו `.cxl` |

---

## 1. הפעלת הסטודיו

```bash
# הפעלת הסטודיו בכתובת http://127.0.0.1:8050
carboxmol

# הפעלה עם טעינה ישירה של קוד PDB
carboxmol 4LGN

# הפעלה על פורט וכתובת מוגדרים ללא פתיחת דפדפן
carboxmol server 4LGN --host 0.0.0.0 --port 8080 --no-browser
```

---

## 2. אימות גאומטרי (`validate`)

```bash
carboxmol validate 4LGN
carboxmol validate model.cif
```

---

## 3. אינטראקציות חלבון-ליגנד (`pli`)

```bash
carboxmol pli 4LGN --ligand 017
carboxmol pli model.pdb --ligand LIG --chain A --resi 401
```

---

## 4. סיווג תיאום מתכות (`metal`)

```bash
carboxmol metal 4LGN
carboxmol metal model.pdb --cutoff 2.80
```

---

## 5. עידון גאומטרי במרחב האמיתי (`refine`)

```bash
carboxmol refine 4LGN --chain A --start 20 --end 30 --cycles 40 -o 4LGN_reg.pdb
```

---

## 6. הרצת תסריטי CXL (`script`)

```bash
carboxmol script examples/pipeline.cxl
```
