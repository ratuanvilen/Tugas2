heroku : https://rattugas2.herokuapp.com/mywatchlist/

Perbedaan antara JSON, XML, dan HTML
-JSON adalah format data dan digunakan untuk menyimpan informasi secara terorganisir dan mudah diakses
-XML adalah bahasa markup dan digunakan untuk menyimpan data atau transfer data 
-HTML adalah markup standar data atau tampilan data yang mudah dibaca user di website

Mengapa memerlukan data delivery
-Data delivery membantu untuk memberikan data yang didapat dari user ke database untuk disimpan. Data delivery ini juga memungkinkan data tersebut dianatarkan secara cepat dan aman ke berbagai platform yang mempunyai struktur web yang berbeda.

Bagaimana cara kamu mengimplementasikan checklist yang ada di tugas3
-Membuat app mywatchlist di django_app yang sudah ada di respository tugas2
-Membuat models di file models.py yang ada di folder mywatchlish dan menambahkan atribut (watched, title, rating, release_date, review)
-Melakukan migrate data
-Membuat initial_watchlist_data.json untuk 10 data objek MyWatchList
-Melakukan loaddata ke database lokal django
-Membuat fungsi 'show_mywatchlist', 'show_json', dan 'show_xml'. Setalh itu tambahkan path tersebut ke file 'urls.py'.
-Membuat file urls.py dan menambahkan path
-Menambahkan path ke file urls.py yang ada di django_app
-Melakukan deploy ke heroku

Postman screenshot
![html_postman](https://user-images.githubusercontent.com/92584623/191648348-d271ec9d-3713-4f28-9e98-75ae5a4f9630.png)
![json_postman](https://user-images.githubusercontent.com/92584623/191648369-d6f5ecd7-8bdf-45c3-a710-8036a7809f7e.png)
![xml_postman](https://user-images.githubusercontent.com/92584623/191648390-985f0b6e-fb05-468d-8f24-672ddbd3ca6a.png)
