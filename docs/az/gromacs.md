# GROMACS Molekulyar Dinamika Simulyasiya Paketi

**Avtomatlaşdırılmış Simulyasiya Boru Xətti, Qüvvə Sahələri və Trayektoriya Analizi**

---

## 1. İcmal

CarboxMol statik kristalloqrafik koordinatları məhlul fazasında dinamik biofizika ilə əlaqələndirən **GROMACS Molekulyar Dinamika (MD)** paketini ehtiva edir.

### Dəstəklənən Qüvvə Sahələri
* **AMBER99SB-ILDN:** Zülalların qatlanması və yan zəncir rotamer dinamikası üçün optimallaşdırılmışdır.
* **CHARMM27 / CHARMM36m:** Zülal-nuklein turşusu kompleksləri üçün tövsiyə olunur.
* **OPLS-AA/L:** Tarazlaşdırılmış torsion potensiallı bütün-atom parametrləri.
* **GROMOS 54a7:** Geniş zaman miqyaslı konformasiya nümunələməsi üçün effektiv birləşmiş-atom sahəsi.

---

## 2. Avtomatlaşdırılmış Simulyasiya Mərhələləri

```text
Mərhələ 1: Topologiyanın Hazırlanması (pdb2gmx)
  └── Aşkar protonasiya təyini (ASH, GLH, LYS, ARG, HIS tautomerləri)
Mərhələ 2: Qutunun Qurulması və Solvasiya
  └── TIP3P / SPC/E su modelləri ilə dodekaedral və ya kub qutu
Mərhələ 3: Neytrallaşdırma və İonlaşma
  └── Fizioloji ion gücü (0.15 M NaCl)
Mərhələ 4: Enerjinin Minimallaşdırılması və İkimərhələli Tarazlaşdırma
  └── Ən dik eniş (Steepest Descent) -> NVT (300 K) -> NPT (1.0 bar)
Mərhələ 5: İstehsalat Molekulyar Dinamikası
  └── Leap-frog inteqratoru, 2 fs addım, LINCS məhdudiyyətləri, PME elektrostatikası
```

---

## 3. Python API ilə İdarəetmə

```python
from carboxmol.simulation import GROMACSManager

sim = GROMACSManager("4LGN.pdb", output_dir="md_simulyasiya")

sim.setup_system(
    forcefield="amber99sb-ildn",
    water="tip3p",
    box_type="dodecahedron",
    box_distance=1.2,
    ion_concentration=0.15
)

sim.minimize(max_steps=50000, tolerance=100.0)
sim.equilibrate_nvt(temperature=300.0, duration_ps=100)
sim.equilibrate_npt(pressure_bar=1.0, duration_ps=100)
sim.run_production(duration_ns=10.0, timestep_fs=2.0)
```

---

## 4. Trayektoriya Analiz Alətləri

* **RMSD (Root Mean Square Deviation):** İlkin koordinatlara nəzərən konformasiya sürüşməsini izləyir.
* **RMSF (Root Mean Square Fluctuation):** Amin turşusu qalıqlarının elastikliyini B-faktorları ilə müqayisə edir.
* **$R_g$ (Dönmə Radiusu):** Zülalın kompaktlığını və struktur bütövlüyünü qiymətləndirir.
* **Hidrogen Rabitəsi Sabitliyi:** Vacib hidrogen rabitələrinin zaman boyu davamlılığını təhlil edir.
