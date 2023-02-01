# System Recommendation
![NETFLIX](https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80)
## Project Overview

Sejarah perkembangan rating usia film dimulai pada tahun 1968, ketika Motion Picture Association of America (MPAA) menerapkan sistem rating usia untuk film yang ditayangkan di Amerika Serikat. Sistem ini dibuat untuk membantu orang tua dan penonton lainnya mengetahui tingkat kecocokan suatu film untuk berbagai usia. Sistem rating usia yang diterapkan oleh MPAA terdiri dari lima kategori: G (Umum), PG (Parental Guidance), PG-13 (Parental Guidance 13), R (Restricted), dan NC-17 (Not Suitable for Children Under 17).

Seiring dengan perkembangan teknologi dan kebutuhan pasar, sistem rating usia diperbaharui dan diperluas. Pada tahun 1990, MPAA menambahkan kategori rating "NC-17" yang menunjukkan bahwa film tersebut tidak cocok untuk anak-anak di bawah 17 tahun. Pada tahun 1996, MPAA menambahkan kategori rating "NC-17" yang menunjukkan bahwa film tersebut tidak cocok untuk anak-anak di bawah 17 tahun.

Selain MPAA, beberapa negara juga menerapkan sistem rating usia untuk film yang ditayangkan di wilayah mereka. Misalnya, di Indonesia, Lembaga Sensor Film (LSF) yang berperan dalam memberikan rating usia film yang diputar di Indonesia. Sistem rating yang diterapkan oleh LSF terdiri dari lima kategori: SU (Semua Umur), 13+, 17+, 21+, dan D (Dilarang).

Secara umum, rating usia film diperlukan untuk membantu penonton menemukan film yang sesuai dengan usia mereka dan preferensi mereka. Rating usia juga membantu dalam menghindari situasi yang tidak sesuai dengan anak-anak menonton film yang tidak sesuai dengan usia mereka. Berdasarkan latar belakang tersebut penulis ingin mengembangkan sistem rekomendasi berbasis machine learning untuk mempermudah dalam menemukan film yang relevan dengan rating usia berdasarkan judul film yang diinput.

## Business Undestanding

Sistem rekomendasi film berdasarkan rating usia diperlukan untuk membantu penonton menemukan film yang sesuai dengan usia mereka dan preferensi mereka. Rating usia diberikan oleh badan yang berwenang untuk menunjukkan tingkat kecocokan film untuk berbagai usia. Dengan sistem rekomendasi ini, orang tua dapat dengan mudah menemukan film yang sesuai untuk anak-anak mereka, sementara remaja dapat menemukan film yang sesuai dengan usia mereka. Ini juga membantu dalam menghindari situasi yang tidak sesuai dengan anak-anak menonton film yang tidak sesuai dengan usia mereka. Sistem rekomendasi ini juga dapat digunakan oleh individu untuk menemukan film yang sesuai dengan preferensi mereka.

### Problem Statement

*   Bagaimana cara membangun sistem rekomendasi film kepada pengguna berdasarkan data maturity rating?

### Goals

*   Membangun model _machine learning_ untuk merekomendasikan sebuah film berdasarkan kemiripan maturity rating.

### Solution

Untuk menyelesaikan masalah ini, penulis akan menggunakan solusi algoritma _content-based filtering_ yang merupakan cara untuk memberi rekomendasi berdasarkan maturity rating.

## Data Understanding

*   **Informasi Dataset**  
    Dataset yang digunakan pada proyek ini yaitu dataset film lengkap dengan rating, informasi lebih lanjut mengenai dataset tersebut dapat lihat pada tabel berikut:

| Jenis | Keterangan |
| --- | --- |
| Sumber | Dataset: [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows/download?datasetVersionNumber=5) |
| Dataset Owner | Shivam Bansal |
| Lisensi | CC0: Public Domain |
| Kategori | Movies & TV Shows |
| Usability | 10.00 |
| Jenis dan Ukuran Berkas | ZIP (3.4 MB) |
| Jumlah File Dataset | 1 File (CSV) |

*   **Fitur Dataset**  
    Dataset ini memiliki 8870 baris dan 12 kolom, berikut penjelasan masing-masing fitur:
    *   **title**, merupakan judul film.
    *   **show\_id**, berisi id penayangan.
    *   **type**, merupakan jenis film (Movie/Tv Show).
    *   **director**, berisi nama penanggungjawab program/film.
    *   **cast**, daftar pemeran yang bermain dalam film.
    *   **country**, daerah asal film diproduksi.
    *   **date\_added**, tanggal film di masukkan ke dalam dataset.
    *   **release\_year**, tahun film rilis.
    *   **rating**, kategori rating usia yang diperbolehkan menonton film tersebut.
    *   **duration**, durasi waktu film dari awal hingga selesai.
    *   **listed\_in**, berisi kategori film.
    *   **description**, merupakan deskripsi atau sinopsis film.
*   **Sebaran/Distribusi pada dataset**
    *   **Distribusi Rating Film**

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/28bfe6e6eec22817edd0841ec2b0349e868449110802db11.png)

Dari grafik plot rating diatas dapat diketahui bahwa konten dengan rating TV-MA (Mature Audiences) memiliki angka tertinggi daripada konten dengan rating yang lain seperti TV-14, TV-PG dan seterusnya.

*     **Distribusi Tahun Rilis**

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/95f29b36651afcfc1a517e3a54a749d0ea0e5049995f9721.png)

Grafik plot diatas menunjukkan sebagian besar film dirilis pada tahun 2018. Fakta yang menarik adalah pada tahun 2019, 2020 dan 2021 jumlah konten yang diproduksi sedikit. Ini sebagian besar karena pandemi Covid-19.

## Data Preparation

Data preparation diperlukan untuk mempersiapkan data agar ketika nanti dilakukan proses pengembangan diharapkan akurasi akan semakin baik dan meminimalisir terjadinya bias pada data. Berikut ini merupakan tahapan-tahapan dalam melakukan pra-pemrosesan data:

*   **Melakukan Pengecekan Missing Value**  
    Melakukan pengecekan nilai null pada setiap kolom dataset. Penanganan yang penulis lakukan pada _missing value_ yaitu dengan melakukan drop data
*   **Melakukan Filter Kolom yang Tidak Dibutuhkan**  
    Pada proses ini yang diperlukan hanyalah 2 kolom saja yaitu kolom title dan rating sehingga penulis melakukan filter pada data.
*   **Menyesuaikan Data Rating Yang Tidak Relevan**  
    Mengidentifikasi value unik pada kolom rating kemudian melakukan penyesuaian data yang tidak relevan agar tidak terjadi bias pada data nantinya.
*   **Melakukan Pengelompokan Rating Menjadi 4 Kelompok**  
    Untuk mempermudah pengembangan dilakukan pengelompokan rating menjadi 4 bagian yaitu ‘Adults’, ‘Teens’, ‘Older Kids’, ‘Kids’

## Modelling

Pada proyek ini, Proses modeling dalam proyek ini menggunakan metode _Cosine Similarity_. _Cosine Similarity_ akan penulis gunakan untuk Sistem Rekomendasi berbasis `Content-Based Filtering` yang akan menghitung kemiripan antara satu film dengan lainnya berdasarkan fitur yang terdapat pada satu film. Berikut penjelasan tahapannya: 

### Content-Based Filtering

Pada tahap ini digunakan TF-IDF Vectorizer untuk menemukan representasi fitur penting dari setiap rating usia. Fungsi yang penulis gunakan adalah tfidfvectorizer() dari library sklearn dengan parameter stopword `english`. Selanjutnya penulis melakukan fit dan transformasi ke dalam bentuk matriks. Keluarannya adalah matriks berukuran (8803, 4). Nilai 8803 merupakan ukuran data dan 4 merupakan matriks rating film.

Untuk menghitung derajat kesamaan (_similarity degree_) antar film, penulis menggunakan teknik _cosine similarity_ dengan fungsi _cosine\_similarity_ dari _library_ sklearn. Berikut dibawah ini adalah rumusnya:

[![Rumus Cosine Similarity](https://camo.githubusercontent.com/8d30a8f1b354dfa7fab96839c43c2288d5640f651d822eaca2a430e1fd716fdb/68747470733a2f2f69302e77702e636f6d2f68656e64726f707261736574796f2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f30342f696d6167652d332e706e673f726573697a653d3430372532433131302673736c3d31)](https://camo.githubusercontent.com/8d30a8f1b354dfa7fab96839c43c2288d5640f651d822eaca2a430e1fd716fdb/68747470733a2f2f69302e77702e636f6d2f68656e64726f707261736574796f2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f30342f696d6167652d332e706e673f726573697a653d3430372532433131302673736c3d31)

Langkah selanjutnya yaitu menggunakan _argpartition_ untuk mengambil sejumlah nilai k tertinggi dari _similarity_ data kemudian mengambil data dari bobot (tingkat kesamaan) tertinggi ke terendah. Kemudian menguji akurasi dari sistem rekomendasi ini untuk menemukan rekomendasi film yang mirip dari film yang ingin dicari.

Berikut ini adalah konten yang dijadikan referensi untuk menentukan 10 rekomendasi film tertinggi yang memiliki kesamaan rating yang sama:

<table><tbody><tr><td>Title</td><td>Rating</td></tr><tr><td>Bullitt County</td><td>Adults</td></tr></tbody></table>

Terlihat pada tabel diatas bahwasannya penulis akan menguji coba model berdasarkan judul film "Bullitt County" dengan rating Adults.

Berikut ini adalah hasil rekomendasi tertinggi dari model _Content Based Filtering_ berdasarkan referensi film diatas:

|   |                                             title | rating |
|---|---------------------------------------------------|--------|
| 0 |        Chelsea Handler: Uganda Be Kidding Me Live | Adults |
| 1 |                              We Are the Champions | Adults |
| 2 |                          The Perfect Dictatorship | Adults |
| 3 |                                  Hot Girls Wanted | Adults |
| 4 | Jen Kirkman: I'm Gonna Die Alone (And I Feel F... | Adults |
| 5 |                        Chris D'Elia: Incorrigible | Adults |
| 6 |                                      Advantageous | Adults |
| 7 |                                        Lilyhammer | Adults |
| 8 |                                        My Own Man | Adults |
| 9 |                      Kevin Hart: Zero F**ks Given | Adults |

## Evaluation

Untuk mengevaluasi model maka dilakukan pengujian untuk mendapatkan rekomendasi film dari judul yang diinputkan kemudian menghitung hasil yang relevan dibanding dengan total rekomendasi dengan rumus berikut:

![dos:819311f78d87da1e0fd8660171fa58e620211012160253.png](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:819311f78d87da1e0fd8660171fa58e620211012160253.png)

Precision Metric Test:

**Data Sample**
|   |                 title | rating |
|---|-----------------------|--------|
| 0 |        Bullitt County | Adults |

**Hasil Rekomendasi**
|   |                                             title | rating |
|---|---------------------------------------------------|--------|
| 0 |        Chelsea Handler: Uganda Be Kidding Me Live | Adults |
| 1 |                              We Are the Champions | Adults |
| 2 |                          The Perfect Dictatorship | Adults |
| 3 |                                  Hot Girls Wanted | Adults |
| 4 | Jen Kirkman: I'm Gonna Die Alone (And I Feel F... | Adults |
| 5 |                        Chris D'Elia: Incorrigible | Adults |
| 6 |                                      Advantageous | Adults |
| 7 |                                        Lilyhammer | Adults |
| 8 |                                        My Own Man | Adults |
| 9 |                      Kevin Hart: Zero F**ks Given | Adults |

Langkah pertama adalah melakukan pengecekan data film berdasarkan title. Dapat dilihat bahwa judul film Bullitt County memiliki maturity rating Adults. Dari 10 item yang direkomendasikan, seluruh item memiliki kategori maturity rating yang sama (similar). Artinya, precision sistem kita sebesar 10/10 atau sebesar 100%.
