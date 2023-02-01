# Convolutional Neural Network
![CNN](https://149695847.v2.pressablecdn.com/wp-content/uploads/2017/09/localizationVsDetection.png)

Convolutional neural networks (CNNs) pertama kali dikenalkan oleh Yann LeCun et all., pada tahun 1998 dalam makalahnya “Gradient-Based Learning Applied to Document Recognition” [22]. LeCun mengenalkan versi awal CNN yaitu LeNet (berasal dari nama LeCun) yang berhasil mengenali karakter tulisan tangan. Pada saat itu LeNet hanya mampu bekerja dengan baik pada gambar dengan resolusi rendah.

Database yang digunakan dalam LeCun adalah [MNIST database of handwritten digits](http://yann.lecun.com/exdb/mnist/index.html), terdiri dari pasangan angka 0 hingga 9 dengan labelnya. Dataset MNIST dikenal luas hingga saat ini dan banyak digunakan terutama oleh para pemula untuk melatih model machine learning.

## Convolutional Layer
CNN, sebuah jaringan saraf biasa mengenali gambar berdasarkan piksel-piksel yang terdapat pada gambar. Teknik yang lebih optimal adalah dengan menggunakan convolutional layer di mana alih alih mengenali objek berdasarkan piksel-piksel, jaringan saraf dapat mengenali objek berdasarkan atribut-atribut yang memiliki lebih banyak informasi.
Convolutional layer berfungsi untuk mengenali atribut-atribut unik pada sebuah objek.  Atribut-atribut yang lebih rendah membentuk atribut lebih tinggi contohnya atribut wajah dibentuk dari atribut mata, telinga, dan hidung. Atribut mata dibentuk dari garis, lengkungan dan bintik hitam.
![ConvolutionalLayer](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:14ac34e336762719ab04c9cc983eae5620220111145634.png)

## Filter Matrix
Convolutional layer dapat mengenali atribut pada objek menggunakan filter. Filter hanyalah sebuah matriks yang berisi angka-angka. Apa maksudnya? Perhatikanlah gambar di bawah ini.

![Filter](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:36b27f628b8aefc62a825138d31bc79a20211021102339.jpeg)

Pada gambar tersebut, terdapat 3 buah filter yang merupakan matriks 3x3 dan sebuah objek gambar berupa huruf X. Filter yang berada di sebelah kiri digambarkan dapat mengenali garis yang terdapat pada kotak hijau. Setiap filter berbeda dapat mengenali atribut yang berbeda seperti, filter di kanan dapat mengenali atribut objek x yang berada di kotak merah.
Contoh lain dari filter dapat Anda lihat di bawah. Pada sebuah gambar perempuan, aplikasi dari filter yang berbeda menghasilkan gambar yang berbeda.
