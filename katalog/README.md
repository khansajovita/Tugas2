Nama : Khansa Jovita
NPM  : 2106651686

link menuju Herokuapp : https://tugas2-khansajovita.herokuapp.com/katalog/

## 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![Bagan](https://github.com/khansajovita/Tugas2/blob/main/katalog/Soal%20no%201%20PBP.png "Bagan dari Django")

## 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Agar program yang dijalankan tidak akan bertabrakan dengan versi lain maupun tidak mengganggu program yang berjalan dengan versi yang berbeda. Karena dengan adanya virtual environment, modul pada suatu program akan diisolasi dan program dapat membuat modul sendiri tanpa harus menggunakan modul luar yang bisa saja ter-update. 

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun modul global yang kita gunakan atau butuhkan akan ikut diperbarui saat menggunakan pip, sehingga program tidak bisa berjalan karena banyak fungsi yang harus diubah dan disesuaikan dengan modulnya.

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Pada poin pertama, membuat sebuah fungsi pada file views.py yang dapat mengambil data-data yang ada pada models.py. Fungsi tersebut bernama show_catalog yang isi dari context adalah list dari object atau data yang ada di import dari models.py, nama serta npm kita. Kemudian context tersebut akan di-(_render_) dan ditampilkan nanti pada HTML.

Kemudian, pada nomor 2, akan melakukan routing untuk melakukan pemetaan fungsi dari views.py, yang mana pada proyek django, di file urls.py terdapat variabel urlpatterns yang berisi path dimana path tersebut include urls di katalog. Dan pada urls.py pada folder katalog, path hanya menghubungkan url-nya ke views.py.

Pada nomor 3, untuk memetakan data ke dalam HTML, maka pada katalog.html mengisi data dengan menggunakan curly bracket untuk dapat menampilkan isi dari template.

Terakhir pada nomor 4, pada website Herokuapp membuat sebuah nama aplikasi baru serta menyalin API-KEY, untuk digunakan pada secrets di repositori github tugas 2 yang sebelumnya sudah dilakukan add, commit, dan push, sehingga saat aplikasi di run pada actions github akan sukses dan isi dari aplikasi Herokuapp dapat terlihat.
