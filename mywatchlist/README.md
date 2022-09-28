### Nama  : Khansa Jovita
### NPM   : 2106651686
### Kelas : PBP - D

Link Herokuapp : http://tugas2-khansajovita.herokuapp.com/mywatchlist/

## 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
- HTML : fokus pada penyajian data, tidak memperhatikan _case sensitive_ atau kapital dari huruf. HTML juga hanya fokus pada tampilan data. Selain itu HTML juga berguna untuk mentransfer dokumen berbasis web. Sifat dari HTML sendiri adalah statis.
- XML : fokus pada penyimpanan data yang mana memang dikhususkan seperti perangkat lunak dan keras. Fungsi ini sejujurnya mirip dengan JSON, namun penamaan file XML dan JSON berbeda, XML memiliki format penamaan .xml. XML sendiri sangat memperhatikan _case sensitive_ yang mana ia akan peka terhadap huruf kapital atau pun kecil. Sifat XML sendiri adalah dinamis. 
- JSON : merupakan format _data-interchange_ ringan, format yang berguna untuk menyimpan, membaca serta menukar informasi. Tujuannya adalah agar dapat dibaca oleh manusia. Memiliki format penulisan dan sintaks yang berbeda dengan XML dan HTML. Kekurangannya adalah akan sangat sulit untuk menangani _error_. 

## 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery akan berguna untuk mengirimkan data dari satu stack ke stack lainnya. Hal tersebut membantu komunikasi antar komputer di mana, kita dpaat melakukan penyimpanan, mengirim ataupun menggunakan data yang ingin kita butuhkan. 

## 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Melakukan pembentukan sebuah aplikasi bernama "mywatchlist" dengan menggunakan perintah `python manage.py startapp mywatchlist`, dan nanti akan terbentuk folder bernama mywatchlist yang berisi `views.py`, `models.py`, dan lain sebagainya. Kemudian menambahkan nama aplikasi `mywatchlist` pada variabel `INSTALLED_APPS` di `settings.py` pada folder `project_django`.
2. Tambahkan _routing_ berupa `path('mywatchlist/', include('mywatchlist.urls'))` pada `urlpatterns` di folder `mywatchlist`.
3. Buat class berisikan dengan variabel yang diminta pada soal di dalam file `models.py` di folder `mywatchlist`. Kemudain lakukan perintah makemigrations dan migrate. 
4. Buat folder bernama `fixtures` dalam folder `mywatchlist` yang isinya berupa file dengan format .json dengan isi kode adalah teks yang nantinya akan ditampilkan pada _website_. Barulah eksekusi _loaddata_ untuk memasukkan data ke dalam _database_.
5. Pada `views.py` di `mywatchlist`, buat fungsi untuk HTML, XML, dan JSON.
6. Kemudian buat folder `templates` di dalam folder `mywatchlist` dengan menambah file `mywatchlist.html`. Lakukan _routing_ di dalam file `urls.py` pada folder `mywatchlist`. 
7. Lakukan _routing_ path untuk JSON dan XML. Jika sudah semua dilakukan, maka dapat lakukan `add`, `commit`, `push`. Dan deploy akan secara otomatis akan me-_re-run_ kembali untuk aplikasi pada Herokuapp.

## Screenshot POSTMAN
### HTML
![image](https://github.com/khansajovita/Tugas2/blob/main/mywatchlist/screenshot/Screenshot%20HTML.png)

### JSON
![image](https://github.com/khansajovita/Tugas2/blob/main/mywatchlist/screenshot/Screenshot%20JSON.png)

### XML
![image](https://github.com/khansajovita/Tugas2/blob/main/mywatchlist/screenshot/Screenshot%20XML.png)
