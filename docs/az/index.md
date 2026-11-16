# CarboxMol Sənədləşməsi

**Universal 3D Makromolekulyar Kristalloqrafiya İş Masası, İnteraktiv WebGL Studio və GROMACS MD Simulyasiya Paketi**

**Müəlliflər:** Süleyman M. Hacızadə və Prof. Qərib N. Mürşüdov  
*Versiya:* 0.4.5  
*Platforma:* CarboxMol Hesablamalı Struktur Biologiya Platforması  
*Əlaqədar Müəllif:* `suleyman.hacizade1@gmail.com`  
*Rəsmi Web Studio:* [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html)  
*Sənədləşmə Portalı:* [https://carboxmol.readthedocs.io/en/latest/](https://carboxmol.readthedocs.io/en/latest/)

---

## 1. İcmal

**CarboxMol** kristalloqraflar, biofiziklər və struktur bioloqları üçün hazırlanmış universal 3D makromolekulyar kristalloqrafiya iş masası, real fəza dəqiqləşdirmə (refinement) mühərriki, interaktiv WebGL vizuallaşdırma studiyası və molekulyar dinamika simulyasiya paketidir.

### Əsas İmkanlar
* **İnteraktiv 3D WebGL Studio və PWA:** 100,000-dən artıq atomu 60 FPS sürəti ilə render edən, karikatura lentləri (cartoon), çubuqlar (sticks), CPK sferaları və həlledici səthlərini dəstəkləyən aparat təminatlı mühərrik.
* **Elektron Sıxlığı Xəritələrinin İzlənməsi və Kəsilməsi (Carving):** İkili CCP4/MRC/DSym xəritələrinin oxunması, dinamik $\sigma$-səviyyəli izokonturların çəkilməsi və seçilmiş qalıqlar ətrafında real fəzada yerli kəsmə ($2mF_o - DF_c$ və $mF_o - DF_c$).
* **Bioqeyri-üzvi Metal Koordinasiya Mühərriki:** Keçid və ikivalentli metal ionlarının ($\text{Zn}^{2+}, \text{Mg}^{2+}, \text{Ca}^{2+}, \text{Fe}^{2+}/\text{Fe}^{3+}, \text{Mn}^{2+}, \text{Cu}^{2+}$) 4-qat (tetraedral, kvadrat planar) və 6-qat (oktaedral) koordinasiya həndəsəsinin avtomatik təsnifatı.
* **Qeyri-Kovalent Qarşılıqlı Təsirlər (PLI):** Duz körpülərinin, $\pi\text{--}\pi$ stekinqin, kation--$\pi$ təsirlərinin və hidrogen rabitəsi şəbəkələrinin kəmiyyət analizi.
* **Real Fəza Həndəsi Dəqiqləşdirməsi:** Torsion bucaqlarının və rabitə məsafələrinin nizamlanması və requlyarizasiyası.
* **GROMACS Molekulyar Dinamika Paketi:** Topologiyanın generasiyası, solvasiya, ionlaşma, enerjinin minimallaşdırılması, NVT/NPT tarazlaşdırılması və istehsalat MD simulyasiyaları üçün avtomatlaşdırılmış boru xətti.
* **CarboxMol Kristalloqrafik Dili (CXL):** Təkrarolunan skriptləşdirmə və avtomatlaşdırma dili (`.cxl`).
* **Terminal CLI və Yerli Xidmət Serveri:** Birbaşa əmr sətri aləti (`carboxmol`) və yerli server demonu.

---

## 2. Arxitektura və Məlumat Modeli

CarboxMol yaddaş baxımından optimal, iyerarxik məlumat modelinə əsaslanır:

```text
Structure (PDB/mmCIF Girişi, Fəza Qrupu, Elementar Qəfəs)
  └── Model (NMR Ansamblı və ya Alternativ Hallar)
        └── Chain (Polipeptid, Nuklein Turşusu, Həlledici, Liqand)
              └── Residue (Standart Amin Turşusu, Nukleotid, Liqand)
                    └── Atom (Koordinatlar [x, y, z], B-Faktor, Tutulma, Element)
```

---

## 3. Quraşdırma

### Pip vasitəsilə Quraşdırma
```bash
pip install carboxmol
```

### Mənbə Kodundan Quraşdırma
```bash
git clone https://github.com/carboxmol/carboxmol.git
cd carboxmol
pip install -e .
```

### Yoxlama
```bash
carboxmol --version
python -c "import carboxmol; print('CarboxMol versiyası:', carboxmol.__version__)"
```

---

## 4. Sürətli Başlanğıc

PDB kodunu daxil edərək 3D WebGL Studio-nu brauzerdə açmaq:
```bash
carboxmol 4LGN
```

Koordinat faylının həndəsi validasiyasını icra etmək:
```bash
carboxmol validate struktur.pdb
```

Metal koordinasiya sferasını təhlil etmək:
```bash
carboxmol metal struktur.pdb
```

---

## 5. Veb Studio və Qrafik Resurslar

* **İnteraktiv WebGL Studio:** [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html)
* **Rəsmi Veb Portalı:** [https://carboxmol.github.io/](https://carboxmol.github.io/)
* **Mənbə Kodu Repozitoriyası:** [https://github.com/carboxmol/carboxmol](https://github.com/carboxmol/carboxmol)
