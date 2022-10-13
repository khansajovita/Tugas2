### Nama    : Khansa Jovita
### NPM     : 2106651686
### Asdos   : FAR
### Kelas   : PBP-D

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
_Programming synchronus_, terjadi blok eksekusi sehingga perintah selanjutnya belum bisa dijalankan dan harus menunggu proses antrian hingga perintah yang sedang dieksekusi selesai. Sedangkan _programming asynchronus_, perintah lain dapat dijalankan tanpa harus menunggu perintah yang sedang dieksekusi, sehingga perintah lain tidak perlu mengantri untuk menunggu eksekusi selanjutnya. 

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming memiliki alur program yang ditentukan oleh event seperti melakukan klik pada _button_ yang dilakukan oleh _user_ sehingga memunculkan sebuah hasil atau _output_. Salah satu contohnya adalah pada saat user melakukan klik pada _button create task_.

## Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronus programming sendiri dapat menjalankan perintah lain selama perintah yang dieksekusi sedang dijalankan, sedangkan dengan adanya AJAX, maka selama _request_ AJAX berlangsung, web dapat dijalankan seperti biasa yang mana _request_ tersebut dijalankan pada latar belakang. Sehingga, dengan AJAX, website tidak perlu melakukan _reload_ dan dapat menampilkan tampilan yang sudah di-_update_ secara langsung. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat _function_ pada `views.py` untuk mengambil dan mengembalikan data dalam bentuk json (untuk AJAX GET);
2. Buat _routing_ url pada `urls.py` yang mengarahkan _function_ tersebut;
3. Membuat _function_ dengan menggunakan AJAX untuk melakukan GET data yang akan mengambil data dari JSON;
4. Buat modal `add task` yang digunakan untuk menambah _task_ baru dengan menggunakan AJAX;
5. Membuat _function_ baru pada `views.py` untuk menyimpan data baru dalam JSON pada _database_;
6. Melakukan _routing_ untuk fungsi tersebut;
7. Buat AJAX juga untuk mengumpulkan data dan mengirimkannya melalui POST tanpa harus melakukan _refresh_.
8. Lakukan _deploy_ ke heroku.

