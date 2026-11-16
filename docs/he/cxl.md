# שפת התסריטים הקריסטלוגרפית (CXL)

**אוטומציית מאקרו, עיבוד אצוות ושחזור פרוטוקולים ב-CarboxMol**

---

## 1. מבוא ל-CXL

**CarboxMol Crystallographic Language (CXL)** היא שפת תסריטים הצהרתית למידול מולקולרי, אימות מבנה והפקת איורים גרפיים באיכות גבוהה.

```bash
carboxmol script pipeline.cxl
```

---

## 2. פקודות עיקריות

```text
# טעינת מבנה ומפה
LOAD 4LGN
LOAD MAP ./maps/4LGN_2fofc.ccp4

# בחירת שיירים
SELECT active_site "chain A and (resi 94, 96, 119, 262)"

# ייצוג וצביעה
REPRESENT "protein" CARTOON
COLOR "protein" SECONDARY
REPRESENT active_site STICK
COLOR active_site ELEMENT

# מדידת מרחק וזווית
DISTANCE A:ASP25:OD2 A:GLU102:OE2
ANGLE A:HIS94:NE2 A:ZN262:ZN A:HIS96:NE2

# גילוף מפה סביב יון אבץ
MAP CARVE CENTER A:ZN:262 RADIUS 6.0 SIGMA 1.5 COLOR CYAN

# רינדור תמונה ברזולוציה גבוהה
RENDER output_figure.png WIDTH 1920 HEIGHT 1080
```
