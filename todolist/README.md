https://rattugas2.herokuapp.com/todolist/login/
https://rattugas2.herokuapp.com/todolist/register/
https://rattugas2.herokuapp.com/todolist/create_task/
https://rattugas2.herokuapp.com/todolist/logout


Kegunaan {% csrf_token %} pada elemen dan yang terjadi apabila tidak ada potongan kode tersebut pada elemen
-{% csrf_token %} berguna  untuk melindungi dan menghidari serangan dari data form dengan method POST dan mengenerate token pada server
-Jika tidak menggunakan {% csrf_token %} maka akan terjadi eror dan akan ada beberapa route link

Membuat elemen ' ' secara manual
-Dapat dilakukan dengan method POST dan csrf token yang akan menerima dan menyimpan data yang nantinya dapat diakses dengan method get()

Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML
-User memberikan input data di form HTML yang nantinya diterima oleh fungsi-funsgi dan disimpan di suatu variabel
-Fungsi akan menginisiasi object baru
-Menyimpan data object task ke database
-Mengambil object task sesuai dengan user
-Data object task dirender ke template HTML
-Ditampilkan di website


Immplementasi checklist
-Membuat aplikasi baru, todolist, pada django si tugas sebelumnya
-Menambahkan path pada urls.py di folder todolist
-Menambahkan path todolist di urls.py pada project_django
-Membuat model Task dengan atribut user, date, title, descriptioin pada models.py di todolist
-Melakukan migration
-Menambahkan fungsi login_user, register, logout_user pada file view.py
-Membuat file html todolist, login, register, create_task di folder baru bernama templates
-Melakukan push ke github dan deploy ke Heroku
-Mmebuat 2 akun dan 3 dummy data

![Screenshot (7)](https://user-images.githubusercontent.com/92584623/192929026-3e003831-061c-42d3-82c2-0f8670f5eb2b.png)
![Screenshot (5)](https://user-images.githubusercontent.com/92584623/192929025-a3bba92c-f115-4a09-a753-d8fe6dfb6b0b.png)
