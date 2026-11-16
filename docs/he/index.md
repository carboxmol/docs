# תיעוד CarboxMol

**שולחן עבודה קריסטלוגרפי תלת-ממדי, סטודיו WebGL אינטראקטיבי וחבילת סימולציות GROMACS MD**

**מחברים:** סולימאן מ. חג'יזאדה ופרופ' גריב נ. מורשודוב  
*גרסה:* 0.4.5  
*פלטפורמה:* פלטפורמת ביולוגיה מבנית CarboxMol  
*אימייל מחבר מתכתב:* `suleyman.hacizade1@gmail.com`  
*סטודיו רשמי ברשת:* [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html)  
*פורטל תיעוד:* [https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)

---

## 1. סקירה כללית

**CarboxMol** היא פלטפורמת קוד פתוח מתקדמת עבור קריסטלוגרפיה מקרו-מולקולרית תלת-ממדית, עידון במרחב האמיתי (Real-Space Refinement), הדמיית WebGL מואצת בחומרה וסימולציות דינמיקה מולקולרית (MD) מבוססות GROMACS.

### יכולות ליבה
* **סטודיו WebGL אינטראקטיבי ו-PWA:** תצוגת סרטים (Cartoon), כדורים ומקלות (Ball-and-stick), ספירות CPK ומשטחי ממס עבור מודלים המכילים מעל 100,000 אטומים ב-60 FPS.
* **צפייה וחיתוך מפות צפיפות אלקטרונים (Carving):** קריאה של מפות בינאריות (CCP4/MRC/DSym), חיתוך איזו-קווי מתאר לפי סטיות תקן ($\sigma$), וגילוף מפה מקומי עבור אתרים קטליטיים ($2mF_o - DF_c$ ו-$mF_o - DF_c$).
* **מנוע קואורדינציה של מתכות ביו-אי-אורגניות:** סיווג גאומטריות של יוני מתכת ($\text{Zn}^{2+}, \text{Mg}^{2+}, \text{Ca}^{2+}, \text{Fe}^{2+}/\text{Fe}^{3+}$) ל-4 תיאומים (טטרהדרלי, מישורי-מרובע) ו-6 תיאומים (אוקטהדרלי).
* **ניתוח אינטראקציות לא-קוולנטיות (PLI):** זיהוי גשרי מלח, קשרי מימן, וערימת $\pi\text{--}\pi$.
* **שפת תסריטים קריסטלוגרפית (CXL):** אוטומציה של תהליכי מידול באמצעות שפת מאקרו ייעודית (`.cxl`).
* **ממשק שורת פקודה (CLI) ושרת מיקרו-שירותים:** כלי פקודה ישיר (`carboxmol`) לתהליכי עבודה מהירים.

---

## 2. התקנה

```bash
pip install carboxmol
```

התקנה מתוך מאגר הקוד:
```bash
git clone https://github.com/carboxmol/carboxmol.git
cd carboxmol
pip install -e .
```

אימות התקנה:
```bash
carboxmol --version
```

---

## 3. קישורים חיצוניים ומערכות קשורות

לחישובים ותסריטי סקירה של מצבי פרוטונציה חריגים בספריות PDB רחבות, עיינו בתיעוד הייעודי של **Project Carbox**:
[https://project-carbox.readthedocs.io/en/latest/](https://project-carbox.readthedocs.io/en/latest/)
