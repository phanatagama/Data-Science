
# Predictive Analysis
![SAHAM](https://images.unsplash.com/photo-1642621668575-93550304b614?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1031&q=80)
## Domain Proyek

Domain proyek yang dipilih dalam proyek _machine learning_ ini adalah mengenai keuangan dengan judul proyek _"Saham Predictive Analytics"_.

Harga saham suatu perusahaan menunjukkan nilai penyertaan dalam perusahaan. Pada pasar modal yang sempurna dan efisien, harga saham mencerminkan semua informasi yang tersedia secara umum di bursa maupun informasi yang hanya dapat diperoleh dari golongan golongan tertentu. Tinggi rendahnya harga saham dapat dipengaruhi oleh banyak faktor seperti kondisi dan kinerja perusahaan, resiko dividen, tingkat suku bunga, kondisi perekonomian, kebijaksanaan pemerintah, laju inflasi, penawaran dan permintaan serta masih banyak faktor lainnya. Karena dimungkinkan adanya perubahan faktor-faktor di atas, harga saham dapat naik atau turun setiap harinya. Dibutuhkan keputusan yang matang dan memerlukan analisis lanjutan, agar tidak salah dalam mengambil keputusan dan mengakibatkan kerugian dalam melakukan transaksi aset digital tersebut di masa mendatang.

Berdasarkan permasalahan diatas model prediksi yang dibuat diharapkan dapat membantu para investor dalam mengambil tindakan yang tepat sehingga resiko yang ada dapat diminimalisir dengan mengetahui naik turunnya harga saham pada masa yang akan datang. 

## Business Understanding

### Problem Statements

- Bagaimana cara melakukan pra-pemrosesan data harga saham ACES sehingga dapat digunakan untuk membuat model yang baik?
- Bagaimana cara membangun model machine learning untuk predictive analysis saham perusahaam ACE Hardware Indonesia?

### Goals

- Melakukan pra-pemrosesan data harga saham ACES agar dapat digunakan dalam membangun model.
- Membangun model _machine learning_ untuk memprediksi data harga saham ACE Hardware Indonesia
    ### Solution statements
    - **Pra-pemrosesan Data** 
        Pada pra-pemrosesan data dapat dilakukan beberapa tahapan, antara lain:
        - Melakukan pembersihan pada dataset agar dapat diproses dengan baik oleh model.
        - Melakukan pembagian dataset untuk data uji dan data latih.
        - Melakukan pengecekan outlier pada setiap variable/fitur yang berkorelasi dengan harga saham
        - Melakukan standardisasi data fitur numerik pada dataset.
        
    - **Pembangunan Model**  
     Pada pembangunan model terdapat beberapa algoritma yang digunakan, antara lain:
	    - _K-Nearest Neighbor_
		- _Random Forest_
		- _Boosting Algorithm_
		- _Linear Regression_

    - **Dua Metrik**  
      Metrik yang digunakan adalah:
      - Akurasi (Accuracy/score dari sklearn)
      - Mean Squared Error (MSE dari sklearn)

## Data Understanding
- **Informasi Dataset**
 Dataset yang digunakan pada proyek ini yaitu **Dataset Saham Indonesia**, informasi lebih lanjut mengenai dataset tersebut dapat lihat pada tabel berikut:

| Jenis | Keterangan |
| ----------------------- | --------------------------------------------- |
| Sumber | [Dataset Saham Indonesia / Indonesia Stock Dataset - Kaggle](https://www.kaggle.com/datasets/muamkh/ihsgstockdata) |
| Dataset Owner | MUAMMAR KHADAFI |
| Lisensi | [Attribution-NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |
| Kategori | Finance |
| Usability | 8.24 |
| Jenis dan Ukuran Berkas | CSV (144.78 kB) |

Setelah melakukan observasi pada dataset yang diunduh melalui  _link_  Kaggle yaitu  `ACES.csv`, didapatkan informasi sebagai berikut :

  |  timestamp | open | low | high | close |     volume |
  |-----------:|-----:|----:|-----:|------:|-----------:|
  | 2007-11-06 |   98 |  89 |  102 |    98 | 1274430000 |
  | 2007-11-07 |   98 |  97 |  103 |   101 |  349330000 |
  | 2007-11-08 |   99 |  96 |  100 |    99 |   66270000 |
  | 2007-11-09 |   95 |  95 |   97 |    95 |   40075000 |
  | 2007-11-12 |   90 |  89 |   95 |    90 |  113285000 |

-   Terdapat 3959 baris (_records_  atau jumlah pengamatan) yang berisi informasi mengenai data riwayat harga  **Saham ACE**.
-   Terdapat 6 kolom yaitu  `Date, High, Low, Open, Close, Volume`  yang merupakan variabel - variabel pada data
-   Dari kolom-kolom tersebut terdapat 6 kolom numerik dengan tipe data int64, yaitu  `High, Low, Open, Close, Volume` 
-   Tidak terdapat  _missing value_  pada dataset.

### Variabel-variabel pada Dataset Saham Indonesia adalah sebagai berikut:
-   timestamp = Date and time of stock transaction
-   open = opening price
-   low = lowest price in the timespan
-   high = highest price in the timespan
-   close = closing price
-   volume = Total volume traded in the timespan


  | #   | Column | Non-Null Count | Dtype |
  |-----|--------|----------------|-------|
  | --- | ------ | -------------- | ----- |
  | 0   | open   | 3959 non-null  | int64 |
  | 1   | low    | 3959 non-null  | int64 |
  | 2   | high   | 3959 non-null  | int64 |
  | 3   | close  | 3959 non-null  | int64 |
  | 4   | volume | 3959 non-null  | int64 |

- ### Mengidentifikasi Outlier
  ![OUTLIER](https://gcdnb.pbrd.co/images/uHf5UdstYm8j.png?o=1)

  Grafik visualisasi boxplot diatas menunjukkan bahwa tidak terdapat Outlier pada setiap variabel yang dipilih

- ### Univariate Analysis
  Analisis _univariate_ adalah cara melakukan analisis terhadap satu jenis (variasi) variabel saja. Dengan kata lain, analisis univariate merupakan proses untuk mengeksplorasi dan menjelaskan setiap variabel dalam kumpulan data secara terpisah.
  ![UNIVARIATE](https://gcdnb.pbrd.co/images/hjAWPen0I3gS.png?o=1)

  Dari hasil histogram diatas dapat disimpulkan bahwasannya hampir semua variabel Distribusi nilainya miring ke kanan (right-skewed). Hal ini akan berimplikasi pada model nantinya.

- ### Multivariate Analysis
  Analisis _multivariate_ adalah cara melakukan analisis terhadap banyak variasi variabel. Dengan kata lain, multivariate analysis merupakan proses eksplorasi yang melibatkan banyak (dua atau lebih) variabel pada data.
  ![MULTIVARIATE](https://gcdnb.pbrd.co/images/5BZ0atuqK2fY.png?o=1)
  
  Korelasi yang terjadi kebanyakan bernilai positif karena kebanyakan grafik pada sumbu y dan x mengalami peningkatan yang cukup signifikan membentuk sebuah garis

## Data Preparation
-   **Drop column**
 Drop column (menghapus kolom) adalah salah satu proses dalam data preparation (persiapan data) yang digunakan untuk menghapus kolom yang tidak diperlukan dari dataset. Hal ini akan membantu efektivitas dalam fitting model yang dilakukan.
 
-   **Melakukan pembagian dataset**  
    Untuk mengetahui kinerja model ketika dihadapkan pada data yang belum pernah dilihat sebelumnya, maka perlu dilakukan pembagian dataset. Pada proyek ini dataset dibagi menjadi data latih dan data uji dengan rasio 80% untuk data latih dan 20% untuk data uji. Data latih merupakan data yang akan kita latih untuk membangun model  _machine learning_, sedangkan data uji merupakan data yang belum pernah dilihat oleh model dan digunakan untuk melihat kinerja atau performa dari model yang dilatih. Pembagian dataset dilakukan dengan modul  [train_test_split](https://scikit-learn.org/0.24/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split)  dari scikit-learn. Setelah melakukan pembagian dataset, didapatkan jumlah sample pada data latih yaitu 3167 sampel dan jumlah sample pada data uji yaitu 792 sampel dari total jumlah sample pada dataset yaitu 3959 sampel.
    
-   **Standardisasi data pada semua fitur numerik pada dataset**  
    Standardisasi merupakan teknik transformasi yang paling umum digunakan dalam tahap data  _preparation_. Standardisasi membantu untuk membuat semua fitur numerik berada dalam skala data yang sama dan membuat fitur data menjadi bentuk yang lebih mudah diolah oleh algoritma. Pada proyek ini, standardisasi data dilakukan dengan menerapkan teknik  [StandarScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)  dari library Scikitlearn. StandardScaler melakukan proses standardisasi fitur dengan mengurangkan mean (nilai rata-rata) kemudian membaginya dengan standard deviasi untuk menggeser distribusi. StandardScaler menghasilkan distribusi dengan standard deviasi sama dengan 1 dan mean sama dengan 0. Sekitar 68% dari nilai akan berada di antara -1 dan 1.

## Modeling
Pada proyek ini, Proses modeling dalam proyek ini menggunakan 4 algoritma  _machine learning_  yaitu  `K-Nearest Neighbor`,  `Random Forest`   `Boosting Algorithm`  dan `Linear Regression` kemudian membandingkan performanya.

-   **K-Nearest Neighbor**  
    _K-Nearest Neighbors_ (KNN) adalah sebuah algoritma yang digunakan dalam klasifikasi atau regresi. Algoritma ini menentukan kelas dari suatu objek baru berdasarkan kelas dari objek-objek yang paling dekat dengan objek tersebut dalam dataset yang ada. Pada tahap ini pembuatan model dilakukan dengan menggunakan modul  [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)  dari library Scikitlearn dengan nilai k = 8 dan metric Euclidean yang artinya, pada model ini akan membandingkan jarak satu sampel data ke 8 sampel data tetangganya yang terdekat, agar hasil persamaan regresi yang dihasilkannya nantinya lebih halus, tahapan itu akan dilakukan berulang-ulang hingga mendapatkan hasil persamaan regresi dengan nilai yang maksimal. Kemudian proses selanjutnya melakukan prediksi menggunakan data uji dan melakukan pengujian.
    -   Kelebihan:
        -   Algoritma _KNN_ merupakan algoritma yang sederhana dan mudah untuk diimplementasikan.
        -   Dapat di implementasikan pada beberapa kasus seperti klasifikasi, regresi dan pencarian.
    -   Kekurangan:
        -   Algoritma _KNN_ menjadi lebih lambat secara signifikan seiring meningkatnya jumlah sampel dan/atau variabel independen.
        
-   **Random Forest**  
    Algoritma ini disusun dari banyak algoritma pohon (decision tree) yang pembagian data dan fiturnya dipilih secara acak. Pembuatan model dilakukan dengan menggunakan modul  [RandomForestClassifier](https://scikitlearn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)  dari library Scikitlearn. terdapat parameter yang harus digunakan agar hasil dari pembuatan model dapat maksimal. Parameter pertama ialah parameter  `n_estimator`  yang merupakan jumlah  _trees_  (pohon) di  _forest_. Di proyek ini penulis melakukan  _set_  nilai  `n_estimator`  sebesar 64  _trees_. Selanjutnya ialah parameter  `max_depth`  yang merupakan kedalaman atau panjang pohon. Itu merupakan ukuran seberapa banyak pohon dapat membelah (_splitting_) untuk membagi setiap  _node_  ke dalam jumlah pengamatan yang di inginkan, di proyek ini penulis melakukan set nilai  `max_depth`  sebesar 16  _split_. Parameter  `random_state`  digunakan untuk mengontrol  _random number generator_  yang digunakan. Di proyek ini penulis melakukan  _set_  nilai pada parameter  `random_state`  sebesar 2023. Lalu yang terakhir ialah parameter  `n_jobs`  yaitu jumlah  _job_  (pekerjaan) yang digunakan secara paralel. Itu merupakan komponen untuk mengontrol  _thread_  atau proses yang berjalan secara paralel.  `n_jobs = -1`  artinya semua proses berjalan secara paralel. Kemudian proses selanjutnya melakukan prediksi menggunakan data uji dan melakukan pengujian.
    -   Kelebihan :
        -   Algoritma _Random Forest_ merupakan algoritma dengan pembelajaran paling akurat yang tersedia. Untuk banyak kumpulan data, algoritma ini menghasilkan pengklasifikasi yang sangat akurat.
        -   Berjalan secara efisien pada data besar.
        -   Dapat menangani ribuan variabel input tanpa penghapusan variabel.
        -   Memberikan perkiraan variabel apa yang penting dalam klasifikasi.
        -   Memiliki metode yang efektif untuk memperkirakan data yang hilang dan menjaga akurasi ketika sebagian besar data hilang.
    -   Kekurangan :
        -   Algoritma _Random Forest_ overfiting untuk beberapa kumpulan data dengan tugas klasifikasi/regresi yang  _bising/noise_.
        -   Untuk data yang menyertakan variabel kategorik dengan jumlah level yang berbeda, _Random Forest_ menjadi bias dalam mendukung atribut dengan level yang lebih banyak. Oleh karena itu, skor kepentingan variabel dari Random Forest tidak dapat diandalkan untuk jenis data ini.

- **Boosting Algorithm**  
    _Boosting_ adalah sebuah teknik yang digunakan dalam algoritma machine learning untuk meningkatkan kinerja model dengan menggabungkan beberapa model yang lemah menjadi satu model yang lebih kuat. Boosting digunakan untuk mengatasi masalah klasifikasi dan regresi. Pada tahap ini pembuatan model dilakukan dengan menggunakan modul  [Boosting Alghoritm](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)  dari library Scikitlearn. Penulis meenggunakan metode adaptive boosting yaitu _AdaBoost_. Parameter yang penulis gunakan terdapat 2 parameter, yaitu parameter  `learning_rate`  yang merupakan bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi _boosting_, dan parameter  `random_state`  yang digunakan untuk mengontrol random number generator yang digunakan. Kemudian proses selanjutnya melakukan prediksi menggunakan data uji dan melakukan pengujian.    
    -   Kelebihan :
        -   Algoritma _Boosting_ dapat mengurangi bias pada data.
        -   Prosedur _Boosting_ cukup sederhana.
        -   Algoritma ini sangat powerful dalam meningkatkan akurasi prediksi.
        -   Algoritma _boosting_ sering mengungguli model yang lebih sederhana seperti logistic regression dan _random forest_.
    -   Kekurangan :
        -   _AdaBoost_ sangat dipengaruhi oleh outlier.

 - **Linear Regression**  
    _Linear regression_ adalah salah satu algoritma yang digunakan data science dan tergolong pada algoritma supervised learning. Algoritma ini menggunakan prinsip regresi. Regresi membuat model prediksi untuk target variabel berdasarkan dari variabel bebasnya. Jenis algoritma ini sering digunakan untuk mencari hubungan antara variabel-variabel yang ada dan prediksinya.
    -   Kelebihan :
        -   Mudah diimplementasikan dan diinterpretasikan. Hal ini karena _linear regression_ hanya melihat keterhubungan dari variabel input dan variabel output saja.
		  -   Menghasilkan model prediksi yang paling akurat untuk data yang bersifat linear.
			 -   Mudah untuk dilakukan evaluasi dan memiliki beragam metode atau metriks yang mudah diterapkan.
    -   Kekurangan :
        -   Data bersifat linear hanya berdasarkan asumsi, bukan dari hasil uji spesifik.    
		   -   Sering menghasilkan model prediksi yang overfitting, artinya terlalu bagus dan tidak nyata. Ini buruk untuk digunakan pada beragam input baru nantinya.
	     -   Sensitif terhadap outliers.
	     -   Jika pemilihan variabel input tidak dilakukan dengan hati-hati atau teliti, maka akan mempengaruhi kualitas model prediksi

## Evaluation
-   Penggunaan _Linear Regression_ dalam data tersebut terbukti lebih baik berdasarkan metrik akurasi yang diberikan. Namun, terdapat anomali berupa MSE dari _Linear Regression_ lebih tinggi dibandingkan _Random Forest_ dan _KNN_ pada saat pelatihan model. Dari pemodelan ini, penulis akan memilih Logistic Regression sebagai model yang akan digunakan dalam prediksi Saham.

- **Akurasi** (Dalam akurasi, didapatkan bahwa Linear Regression memiliki akurasi yang lebih tinggi bila dibandingkan dengan model lain)

	-   Akurasi merupakan metrik paling awam/paling diketahui pada pemodelan. Ia adalah persentase jumlah data yang diprediksi secara benar terhadap jumlah keseluruhan data. Pada proyek ini, metrik evaluasi yang digunakan untuk mengukur kinerja model yaitu menggunakan metrik **akurasi** dan **MSE**. Akurasi di sini merupakan tingkat keakuratan data prediksi yang didasarkan dari data latih pada model, tingkat akurasi tertinggi ialah pada model Linear Regression sebesar 99.82% dan ini menunjukkan bahwasannya _Linear Regression_ merupakan model terbaik dari ketiga model lainnya dalam memprediksi nilai **Saham** di masa mendatang. 
      Berikut merupakan tabel perbandingan akurasi keempat model
    
    |   | akurasi| 
    | ------------ | ------------ |
    | KNN | 99.761589  | 
    | RF | 99.749817 | 
    | Boosting | 94.174727 |
    | LR | 99.829207 | 
    
     Berdasarkan data pada tabel diatas dalam akurasi, didapatkan bahwa _Linear Regression_ memiliki akurasi yang lebih tinggi bila dibandingkan dengan model lain.

- **MSE** (_Random Forest_ memiliki _MSE_ yang lebih rendah pada hasil data latih, namun asumsi didasarkan pada akurasi yang rendah, maka _MSE_ juga rendah)
	-   _Mean Squared Error_ (MSE) adalah Rata-rata Kesalahan kuadrat diantara nilai aktual dan nilai peramalan. Metode _Mean Squared Error_ secara umum digunakan untuk mengecek estimasi berapa nilai kesalahan pada peramalan. Nilai _Mean Squared Error_ yang rendah atau nilai mean squared error mendekati nol menunjukkan bahwa hasil peramalan sesuai dengan data aktual dan bisa dijadikan untuk perhitungan peramalan di periode mendatang. Metode _Mean Squared Error_ biasanya digunakan untuk mengevaluasi metode pengukuran dengan model regressi atau model peramalan. _MSE_ didefinisikan dalam persamaan berikut:
	   ![MSE_FORMULA](https://camo.githubusercontent.com/fc2156e0e61ff494392eae55e55c468991c205b84cd1ad76ac3300a143a6e350/68747470733a2f2f7777772e707974686f6e706f6f6c2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032312f30382f32303231303831325f3230303933375f303030302d31303234783237302e706e67)

    Keterangan:

    - N = jumlah dataset
    - yi = nilai sebenarnya
    - yi^ = nilai prediksi

  Berikut ini perbandingan grafik metrik _MSE_ pada keempat model:
  
  ![MSE](https://gcdnb.pbrd.co/images/XjnWYGfQlLPs.png?o=1)
  
  Selain akurasi untuk menentukan model terbaik dapat dilihat juga berdasarkan tingkat eror pada grafik di atas, semakin kecil tingkat eror maka semakin baik model tersebut memprediksi data. Berikut tabel perbadingan _MSE_ untuk masing-masing model:
  
    |   | train | test |
    | ------------ | ------------ | ------------ |
    | KNN | 0.086577  | 0.319177 |
    | RF | 0.020277 | 0.334936 |
    | Boosting | 2.238564 | 7.798675 |
    | LR | 0.095724 | 0.228652|

  ![Grafik](https://user-images.githubusercontent.com/48324618/214775994-504b7d99-80e9-4859-8f4e-18dd60e1a09a.png)

  Berdasarkan grafik visualisasi perbandingan hasil prediksi dengan harga real saham ACE diatas, bisa disimpulkan bahwa model Linear Regression memiliki akurasi yang baik dalam melakukan prediksi harga Saham ACE Hardware Indonesia.
