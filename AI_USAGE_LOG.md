# AI Usage Log — Pandas

## Summary

| Member | Role | Tools | ~% code AI-assisted | Interpretation cells AI-assisted? |
| ------ | ------------- | --------------- | ------------------- | --------------------------------- |
| Zaidan | Data Engineer | Gemini | ~20% | No |
| Ihsan | Estimation Analyst | Gemini | ~20% | No |
| Kevin Christman Lumban Tobing | Inference Analyst | None | 0% | No |
| Safani | Hypothesis Analyst | None | 0% | No |
| Fernando | Computation Analyst | None | 0% | No |

## Per-Member Detail

### Member A — Zaidan
| # | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Membuat loop pagination API | Gemini | "Buatkan script tarik data API GitHub Pandas..." | Ya — disesuaikan folder | Sangat membantu mempercepat proses penarikan data mentah dari API GitHub, namun perlu penyesuaian lokasi penyimpanan direktori. |

### Member B — Ihsan
| # | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Penyusunan fungsi MLE | Gemini | "Buatkan struktur fungsi Python untuk Maximum Likelihood Estimation..." | Ya — disesuaikan parameter | Struktur dasar fungsi cukup baik untuk *scaffolding*, namun parameternya harus disesuaikan ulang secara manual agar mematuhi rumus dari referensi Tsun (2020). |

### Member C — Kevin Christman Lumban Tobing
| # | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | - | None | - | - | Tahap Inferensi (Minggu 12) belum dimulai pada eksekusi Checkpoint 1. Direncanakan 100% manual tanpa bantuan AI untuk fase selanjutnya. |

### Member D — Safani
| # | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | - | None | - | - | Tahap Pengujian Hipotesis (Minggu 13) belum dimulai pada eksekusi Checkpoint 1. Direncanakan 100% manual tanpa bantuan AI untuk fase selanjutnya. |

### Member E — Fernando
| # | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Setup repository & dokumentasi | None | - | - | Penyusunan struktur direktori dan dokumen administratif Checkpoint 1 dilakukan murni manual. Tahap komputasi simulasi (Minggu 14) belum dimulai. |

## Group Reflection

Selama pengerjaan Checkpoint 1 pada audit statistik ini, pendekatan kelompok kami terhadap penggunaan AI sangat terukur. Pada tahap awal (*Data Engineering* dan *Estimation*), kami menggunakan AI (Gemini) secara strategis untuk menangani tugas-tugas penulisan *boilerplate code*. AI terbukti sangat tangkas dan efisien dalam merancang skema *loop pagination* untuk berinteraksi dengan API GitHub, serta menyusun kerangka dasar fungsi Python untuk *Maximum Likelihood Estimation* (MLE). Hal ini sangat menghemat waktu teknis penyiapan data kami.

Namun, kami menemukan bahwa hasil keluaran AI membutuhkan koreksi dan pengawasan yang ketat ketika dihadapkan pada spesifikasi matematis yang kaku. Misalnya, pada saat penyusunan fungsi estimasi parameter, AI memberikan struktur dasar yang baik, tetapi Member B tetap harus memodifikasi parameternya secara manual agar benar-benar selaras dengan rumus konjugasi Beta pada referensi utama kami (Buku Tsun, 2020). 

Sebagai komitmen integritas untuk fase selanjutnya (Checkpoint 2 dan 3), kelompok kami secara tegas bersepakat untuk **TIDAK** menggunakan AI sama sekali pada seluruh penulisan interpretasi analitis (sel *Markdown*), serta secara penuh pada fase Inferensi, Pengujian Hipotesis, dan Simulasi Stokastik. Kami menyadari bahwa mendelegasikan penarikan kesimpulan *p-value* dan penjabaran *Confidence Interval* kepada AI akan menghilangkan esensi pemahaman kami terhadap data. Oleh karena itu, Member C, D, dan E akan bekerja murni 100% tanpa AI, memastikan setiap argumen di Laporan Kesehatan Statistik akhir nanti murni merupakan hasil pemikiran analitis dan komputasional kami sendiri.