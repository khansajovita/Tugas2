### Nama       : Khansa Jovita
### NPM        : 2106651686
### Kelas      : PBP - D
### Asdos      : FAR
### Link Herokuapp : https://tugas2-khansajovita.herokuapp.com/todolist/

## 1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Kegunaan `{% csrf_token %}` sendiri adalah untuk mencegah serangan CSRF atau _Cross-Site Request Forgery_ yang merupakan serangan sederhana pada _web_, dengan memberikan token acak dengan jumlah yang banyak. Dengan begitu penyerang aplikasi tidak bisa menebak token tersebut dan tidak dapat mengirimkan _request_ ke _web_. CSRF ini terjadi karena tanpa sadar _user_ akan mengirimkan sebuah _request_ ke sebuah aplikasi sehingga nanti aplikasi akan mengeksekusi perintah tersebut. Dan biasanya  dikarenakan _user_ tanpa sengaja telah melakukan klik pada sebuah URL yang mengarahkan ke _web_ yang berbahaya. 

## 2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Ya, dapat membuat `<form>` tanpa menggunakan `{{ form.as_table }}`. Karena, kita dapat membuatnya dengan menggunakan tag `<input>` yang berisikan dengan atribut yang disesuaikan dengan kebutuhan, namun biasanya diikuti dengan atribut `type` dan `name`.

## 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.
_User_ akan melakukan input pada `form`, yang kemudian di _submit_ dan form akan mengirimkan data tersebut melalui request GET atau POST (tergantung settingan yang dibuatnya). Kemudian server akan memproses dan masuk ke dalam fungsi pada `views.py` lalu inputan disimpan oleh method `.save()`. Barulah data inputan tadi akan berhasil diakses pada _template_ HTML.

## 4.  Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.
1. Membuat aplikasi django baru dengan menggunakan perintah `python manage.py startapp todolist`.
2. Melakukan pendaftaran aplikasi pada `settings.py` pada folder `project_django` serta menambahkan path untuk _routing_ aplikasi `todolist` pada `urls.py` di folder `project_django`.
3. Menambahkan model `Task` untuk todolist pada `models.py` yang kemudian pada _cmd_ melakukan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk menambahkan skema model ke dalam _database_ django lokal.
4. Menambahkan function untuk _register_, _login_, _logout_, _show todolist_, dan sebagainya pada `views.py`.
5. Melakukan _routing_ pada setiap _function_ di `urls.py` pada folder `todolist`.
6. Membuat sebuat folder `templates` yang berisikan HTML untuk membuat task, login, register, dan tampilan untuk todolist.
7. Melakukan modifikasi pada tampilan HTML dengan menggunakan css pada folder `static`.
8. Melakukan `git add .`, `git commit`, dan `git push` untuk memasukkan ke dalam github yang kemudian secara otomatis akan mendeploy pada Heroku (karena sudah melakukan deploy pada tugas-tugas sebelumnya).
