# Elektron Sıxlığı Xəritələrinin İzlənməsi və Real Fəzada Kəsilməsi (Carving)

**CCP4/MRC İkili Xəritə Formatı, $\sigma$-Səviyyəli İzokonturlar və Aktiv Mərkəzin Kəsilməsi**

---

## 1. Kristalloqrafik Elektron Sıxlığı Xəritələri

Struktur modelləri təcrübi elektron sıxlığı paylanması $\rho(\mathbf{r})$ ilə müqayisə edilərək dəqiqləşdirilir:

$$\rho(\mathbf{r}) = \frac{1}{V} \sum_{\mathbf{h}} |F(\mathbf{h})| \exp[-2\pi i \mathbf{h} \cdot \mathbf{r} + i \alpha(\mathbf{h})]$$

### Dəstəklənən Xəritə Növləri
* **$2mF_o - DF_c$ Xəritəsi:** Əsas bərpa olunmuş elektron sıxlığı. Standart vizuallaşdırma səviyyəsi $1.0\sigma - 1.5\sigma$-dir.
* **$mF_o - DF_c$ Fərq Xəritəsi:** Təcrübi difraksiya ilə atom modeli arasındakı fərqləri göstərir. Müsbət sıxlıq ($+3.0\sigma$, yaşıl tor) modeldə çatışmayan atomları və ya həlledici molekullarını; mənfi sıxlıq ($-3.0\sigma$, qırmızı tor) isə model xətalarını bildirir.

---

## 2. İkili Xəritə Formatları

* **CCP4:** Standart kristalloqrafik xəritə formatı (Mode 2: 32-bit kəsr ədədlər). Elementar qəfəs parametrlərini ($a, b, c, \alpha, \beta, \gamma$), fəza qrupunu və statistik göstəriciləri saxlayır.
* **MRC / MRC2014:** Birhissəcikli kriyo-EM yenidənqurmaları üçün universal format.
* **DSym:** Vebdə sürətli WebGL axını üçün sıxılmış kristalloqrafik format.

---

## 3. Real Fəzada Sıxlığın Kəsilməsi (Carving)

Bütün elementar qəfəsin təsviri GPU resurslarını həddindən artıq yükləyir. CarboxMol lokallaşdırılmış sıxlıq kürələrini ayıran dinamik xəritə kəsici mühərrikə malikdir:

Seçilmiş mərkəz $\mathbf{r}_0$ və radius $R_{\text{carve}}$ (adətən $5.0 - 8.0\,\text{Å}$) daxilində:
$$\mathcal{V}_{\text{carved}} = \{ \mathbf{r} \in \mathcal{V} \mid \|\mathbf{r} - \mathbf{r}_0\| \le R_{\text{carve}} \}$$

Bu alət xüsusilə katalitik mərkəzlər, liqand cibləri və metal koordinasiya zonaları üçün dəqiq və aydın görüntü təmin edir.
