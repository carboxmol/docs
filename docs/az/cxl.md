# Carbox Kristalloqrafik Dili (CXL) ilə Skriptləşdirmə

**Makro Avtomatlaşdırması, Qrup Halında Modelləşdirmə və Təkrarolunan Tədqiqat**

---

## 1. CXL Giriş

**Carbox Kristalloqrafik Dili (CXL)** CarboxMol daxilində avtomatlaşdırılmış molekulyar modelləşdirmə, koordinat manipulyasiyası və qrafik təsvirlərin generasiyası üçün yaradılmış deklarativ skript dilidir.

```bash
carboxmol script boru_xetti.cxl
```

---

## 2. Qrammatika və Əmrlər

CXL əmrləri böyük/kiçik hərfə həssas deyil. `#` ilə başlayan sətirlər şərh sayılır.

### Fayl Yükləmə
```text
LOAD 4LGN
LOAD MAP ./maps/4LGN_2fofc.ccp4
```

### Atom Seçimləri
```text
SELECT active_site "chain A and (resi 94, 96, 119, 262)"
SELECT zinc "element ZN"
SELECT pocket_water "element O and resn HOH and within 3.0 of active_site"
```

### Vizuallaşdırma
```text
REPRESENT "protein" CARTOON
COLOR "protein" SECONDARY

REPRESENT active_site STICK
COLOR active_site ELEMENT

REPRESENT "resn LIG" SURFACE
COLOR "resn LIG" CYAN OPACITY 0.6
```

### Həndəsi Analiz və Dəqiqləşdirmə
```text
DISTANCE A:ASP25:OD2 A:GLU102:OE2
ANGLE A:HIS94:NE2 A:ZN262:ZN A:HIS96:NE2
METAL DETECT CUTOFF 2.80
PLI ANALYZE LIGAND "resn LIG"
REFINE CYCLES 50 TOLERANCE 1e-4 OUTPUT refined.pdb
RENDER sekil.png WIDTH 1920 HEIGHT 1080
```
