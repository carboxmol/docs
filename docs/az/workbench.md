# CarboxMol 3D İş Masası və WebGL Studio

**İnteraktiv Makromolekulyar Kristalloqrafiya Vizuallaşdırması və Real Fəza Təhlili**

---

## 1. Giriş

**CarboxMol İş Masası** struktur biologiyası və kriyo-EM modellərinin araşdırılması üçün yaradılmış WebGL əsaslı yüksək məhsuldarlıqlı 3D mühitdir. Həm yerli server (`carboxmol server`), həm də sərbəst PWA kimi [https://carboxmol.github.io/studio.html](https://carboxmol.github.io/studio.html) ünvanında mövcuddur.

---

## 2. Təsvir Modelləri

CarboxMol Studio bir neçə eyni vaxtda işləyən render rejimini dəstəkləyir:

* **Karikatura Lentləri (Cartoon):** $\alpha$-spiral silindrləri və $\beta$-təbəqə oxları ilə qlobal zülal bükülməsini nümayiş etdirir.
* **Kürə-və-Çubuq (Ball-and-Stick):** Liqand birləşmə zonaları və katalitik mərkəzlər üçün kovalent rabitələri aydın göstərir.
* **CPK Sferaları:** Van der Vaals atom radiusları vasitəsilə sterik toqquşmaları və boşluqları göstərir.
* **Həlledici Səthi (Solvent Surface):** Cib həndəsəsini və elektrostatik yük paylanmasını əks etdirir.
* **Elektron Sıxlığı Toru (Mesh):** Təcrübi difraksiya məlumatları ilə atom koordinatlarının uyğunluğunu yoxlayır.

---

## 3. İdarəetmə və Naviqasiya

* **Fırlanma:** Sol düymə + Çəkmə kütlə mərkəzi ətrafında kameranı fırladır.
* **Sürüşdürmə (Pan):** Sağ düymə + Çəkmə kameranı ekrana paralel müstəvidə hərəkət etdirir.
* **Yaxınlaşdırma (Zoom):** Siçan çarxı baxış oxu boyu hərəkəti təmin edir.
* **Mərkəzləşdirmə:** İstənilən atom üzərinə ikiqat klik həmin koordinatı kameranın mərkəzinə gətirir.
* **Z-Kəsmə (Slab):** Shift + Çarx daxili strukturları aydınlaşdırmaq üçün ön və arxa kəsmə müstəvilərini nizamlayır.

---

## 4. İnteraktiv Ölçmə Alətləri

* **Məsafə Ölçümü:** İstənilən iki atomu seçməklə evklid məsafəsi hesablanır:
  $$\Delta d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
* **Rabitə Bucağı:** Ardıcıl 3 atom seçilərək $\theta \in [0^\circ, 180^\circ]$ bucağı müəyyən edilir.
* **Dihedral (Torsion) Bucağı:** Peptid onurğasının $\phi, \psi$ bucaqlarını Ramachandran paylanması üzrə qiymətləndirmək üçün 4 atom seçilir.
