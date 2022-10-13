https://rattugas2.herokuapp.com/todolist/

-Perbedaan Inline, Internal, dan External CSS, kelebihan dan kekurangan masing masing style
Inline CSS adalah cara penulisan styling CSS yang dilakukan langsung dalam tag elemen yang bersangkutan.
Kelebihan:
Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
Berguna untuk memperbaiki kode dengan cepat.
Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
Kekurangan:
Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.
<p style="color:blue;text-align:center;">Hello World</p>

Internal CSS adalah cara penulisan CSS yang berada di file yang sama pada file HTML. Styling CSS tersebut unik untuk file HTML itu saja.
Kelebihan:
Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
Class dan ID bisa digunakan oleh internal stylesheet.
Kekurangan:
Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website

<style> .selector {styling properties} </style>.

Eksternal CSS adalah cara penulisan CSS pada satu file yang terpisah dari HTML.
Kelebihan:
Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
Loading website menjadi lebih cepat.
File CSS dapat digunakan di beberapa halaman website sekaligus
Kekurangan :
Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.
 <link rel="stylesheet" href="mystyle.css">. File yang dituliskan dalam href adalah nama file .css yang telah dibuat. Isi dari file CSS eksternal akan mengubah styling untuk semua file .html.


-Jelaskan tag HTML5 yang kamu ketahui.
Beberapa tag HTML yang umum digunakan adalah :
<head> :  memberikan informasi tentang dokumen,
<body> : berisi data yang ingin ditampilkan di website
<h1>, <h2>, <h3>, dst : tag heading dari 1-6 dengan 1 ukuran paling gede
<p> : paragraph, untuk text <div> : division, sebagai container <form> : untuk membuat form <input> : untuk menerima input dari user

-Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Ada 6 tipe selector CSS:

Tag : disebut juga type selector, memilih elemen berdasarkan tag. --> seperti tag p, button, table, dst
p {
    insert code here
}

Class : memilih elemen berdasarkan nama class yang sudah diberikan --> <p class="nama-class"></p>
.nama-class {
    insert code here
}

ID : memilih elemen berdasarkan id --> <p id="nama-id"></p>
#nama-id {
    insert code here
}

Atribut : memilih elemen berdasarkan atribut dari sebuah tag. Misal tag input memiliki beberapa tipe, salah satunya adalah text.
input[type=text] {
    insert code here
}

Universal : sesuai namanya selektor ini berlaku untuk semua atribut,
* {
    insert code here
}

Pseudo : a. pseudo-class : untuk state element, seperti saat di click, hover, dst
a:hover {
    insert code here
}
b. pseudo-element : untuk element semu di HTML , misal seperti elemen di dalam elemen

-Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Membuat card di file todolist.html agar data yang sudah dimasukan biasa menjadi card
Tambahkan styling pada masing-masing file html, seperti warna, font, margin, dll.
Pastikan responsif.
Deploy
