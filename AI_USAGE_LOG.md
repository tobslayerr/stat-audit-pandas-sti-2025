# AI Usage Log — Pandas

## Summary

| Member | Role | Tools | ~% code AI-assisted | Interpretation cells AI-assisted? |
| ------ | ------------- | --------------- | ------------------- | --------------------------------- |
| Zaidan | Data Engineer | Gemini | ~20% | No |
| Ihsan | Estimation Analyst | Gemini | ~20% | No |
| Kevin Christman Lumban Tobing | Inference Analyst | Gemini | ~5% | No |
| Safani | Hypothesis Analyst | None | 0% | No |
| Fernando | Computation Analyst | ChatGPT | ~5% | No |

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
| 1 | Memeriksa sintaks fungsi library | Gemini | "Bagaimana cara mendapatkan batas persentil distribusi Beta menggunakan SciPy di Python?" | Ya — disesuaikan dengan parameter lokal. | AI sangat efisien untuk mempercepat pemahaman terhadap dokumentasi library `scipy.stats.beta.ppf`, sehingga saya bisa fokus mengimplementasikan batas probabilitas secara manual tanpa takut terjadi *syntax error*. |

### Member D — Safani Nuraini
**Tools used:** None
**Task:** Pengujian Hipotesis (H0/Ha, Z-Test, Interpretasi P-Value).
**Keterangan:** Seluruh analisis pada Modul 04 dikerjakan 100% secara manual tanpa bantuan AI untuk mematuhi larangan penggunaan AI pada penarikan kesimpulan statistik.

### Member E — Fernando
| # | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1 | Setup repository & dokumentasi | None | - | - | Penyusunan struktur direktori dan dokumen administratif Checkpoint 1 dilakukan murni manual. Tahap komputasi simulasi (Minggu 14) belum dimulai. |
| 2 | Pencarian metode hash unik | ChatGPT | Bagaimana cara generate multiple hash index yang unik di Python untuk Bloom Filter menggunakan satu library bawaan? | Ya — mengadaptasi saran penggunaan hashlib.md5 ke dalam struktur class BloomFilter. | Jawaban sangat efisien dan membantu. Sisa algoritma stokastik Monte Carlo dan MCMC Knapsack berhasil saya bangun secara mandiri tanpa bantuan AI.|

## Group Reflection

Perjalanan tiga minggu pengerjaan audit statistik ini memberikan perspektif mendalam mengenai kolaborasi manusia dan AI dalam riset data. Pada fase awal (Data Engineering dan Estimation), kami menggunakan AI (Gemini) secara strategis untuk scaffolding teknis dan penulisan boilerplate code, seperti penyusunan loop pagination API GitHub. Penggunaan ini terbukti sangat efisien dalam mempercepat penyiapan lingkungan kerja dan struktur dasar modul.

Namun, seiring pengerjaan, kami menyadari bahwa AI memiliki keterbatasan dalam ketelitian matematis yang kaku. Kami melakukan koreksi manual yang signifikan pada setiap modul untuk memastikan kesesuaian formula dengan Buku Tsun (2020), di mana AI seringkali kurang presisi dalam merujuk halaman atau notasi spesifik.

Seiring berjalannya proyek, kami secara tegas mengubah kebijakan internal: kami memilih untuk TIDAK menggunakan AI sama sekali dalam penulisan interpretasi analitis (sel Markdown), perumusan hipotesis (H0/Ha), serta penyusunan rekomendasi manajerial. Kami menyadari bahwa mendelegasikan bagian tersebut kepada AI akan menghilangkan esensi pemahaman kami terhadap data. Momen krusial tersebut adalah saat merumuskan kesimpulan Z-Test dan interpretasi Confidence Interval; kami memutuskan untuk menulisnya murni dari hasil pemikiran tim agar bebas dari ambiguitas istilah (seperti menghindari frasa "accept H0"). Pengalaman ini mengajarkan kami bahwa AI adalah alat akselerasi teknis, namun nalar analitis tetap menjadi tanggung jawab mutlak kami sebagai peneliti. Hasil akhirnya adalah laporan yang tidak hanya akurat secara komputasi, tetapi juga tajam dalam narasi manajerial, yang membuktikan penguasaan kami atas materi perkuliahan secara menyeluruh.
