### Nama       : Khansa Jovita
### NPM        : 2106651686
### Kelas      : PBP - D
### Asdos      : FAR
### Link Herokuapp : https://tugas2-khansajovita.herokuapp.com/todolist/

## 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline merupakan kode CSS yang diletakkan pada setiap tag HTML, sesuai dengan _style_ yang kita inginkan. Internal CSS merupakan kode CSS yang diketik pada `tag<style>` dimana letaknya berada paling atas dari _header file_ HTML. Sedangkan Eksternal CSS merupakan kode CSS yang ditulis secara terpisah dari HTML yang nantinya akan digabungkan antara file `.css` dengan file `.html`. 

Kelebihan
- Inline : Dalam kasus perubahan kecil pada satu tag akan lebih mudah, Proses load akan lebih cepat serta memudahkan developer untuk melakukan revisi kode.
- Internal : Tidak mempengaruhi perubahan pada halaman _website_ lain, tidak membutuhkan banyak file untuk mengetikkan CSS.
- Eksternal : Kecepatan _loading_ akan leih cepat, file CSS dapat digunakan oleh banyak file HTML, struktur HTML akan lebih rapi dah memori yang digunakan kecil.

Kekurangan 
- Inline : Tidak efisien karena harus mengetikkan kalimat yang sama pada setiap tag. 
- Internal : Performa web akan lambat karena membutuhkan memori yang besar, serta tidak efisiem.
- Eksternal : Tampilan _website_ akan tidak rapi saat terjadi kegagalan pemanggilan file CSS.

## 2. Jelaskan tag HTML5 yang kamu ketahui.
1. `<!DOCTYPE>` = Untuk menentukan tipe dari dokumen;
2. `<title>` = Menentukan judul dari halaman _web_
3. `<body>` = Tag untuk menentukan elemen _body_
4. `<br>` = Tag untuk membentuk sebuah baris baru
5. `<div>` = Tag untuk mendefinisikan bagian dari dokumen
6. `<h1> - <h6>` = Tag untuk _header_
7. `<input>` = Tag sebagai inputan dari _user_
8. `<li>` = Tag untuk mendefinisikan sebuah list
9. `<p>` = Tag untuk paragraf
10. `<img>` = Tag untuk gambar

## 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selector tag = Selector yang menggunakan tag HTML. Di mana nanti semua tag yang dipilih akan sesuai dengan desain dari CSS kita. Contoh `body {`.
2. Selector class = Menggunakan atribut class pada elemen HTML yang dipilih. Mirip dengan ID, namun class dapat digunakan pada banyak tag. Contoh adalah `.body-title {`.
3. Selector ID = Menggunakan atribut ID pada elemen HTML. Apabila ID digunakan pada salah satu tag, mana seluruh tag tersebut akan berubah mengikuti bentukan CSS kita. Hal ini berbeda dari class yang dapat hanya digunakan pada satu tag yang sama tanpa mempengaruhi tag lain. Contoh `#title-text {`.
4. Selector universam = Tanda bintang `'*'` pada CSS di mana semua tag yang ada akan berubah sesuai dengan CSS kita. 

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Melakukan kostumisasi pada halaman _login_, _register_, dan _create-task_, di mana saya menambahkan _navbar_, serta melakukan desain kecil untuk membentuk tampilan terlihat rapi dan tidak kosong.
2. Menambahkan path untuk bootstrap pada `base.html` serta menghubungkan antara file CSS dengan file HTML kita dengan menggunakan `{% load static %}` pada setiap halaman HTML. 
3. Kostumisasi halaman _todolist_ dengan menambahkan _cards_ untuk setiap _task_.
4. Karena sudah menambahkan bootstrap, otomatis halaman akan menjadi reponsive. 