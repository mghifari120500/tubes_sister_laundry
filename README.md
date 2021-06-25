Untuk mengakses aplikasi, harus menyalakan brokernya terlebih dahulu


Buka Command Prompt, lalu akses ke direktori di tempat menginstall mosquitto, misalnya : C:\Program Files\mosquitto


Untuk menyalakan brokernya, kita disini akan menyalakan 3 broker dengan port 2222 , 3333 , 4444 


Maka dari itu, masukan perintah sebagai berikut : 

**mosquitto.exe -p 2222 (untuk akses ke Laundry Bojong)**

**mosquitto.exe -p 3333 (untuk akses ke Laundry Soang)**

**mosquitto.exe -p 4444 (untuk akses ke Perbandingan Waktu)**


Kita akan membuka client_subscribe.py terlebih dahulu sebagai akses main menunya, maka dari itu, buka direktori dimana tempat codingan disimpan, masukan perintah pada cmd sebagai berikut : 

**py client_subscribe.py**

Jika sudah, maka akan keluar tampilan seperti ini : 

![image](https://user-images.githubusercontent.com/62027487/123367252-d2536b80-d5a3-11eb-82a5-d091cb88cc7a.png)

Kita mengerjakan secara berurutan terlebih dahulu, kita akan memasukan pilih nomor 1, maka ketik **"01"** , lalu tekan Enter.

![image](https://user-images.githubusercontent.com/62027487/123367321-f2832a80-d5a3-11eb-8879-e5d7fad0f53e.png)

Jika sudah, maka akan keluar tampilan seperti berikut 

![image](https://user-images.githubusercontent.com/62027487/123367408-16467080-d5a4-11eb-887d-97742a01b602.png)

Karena kita memilih nomor 1, disini meminta akses ke Laundry Bojong agar bisa terhubun dan bisa dilanjutkan diprosesnya, maka dari itu, buka direktori dimana tempat codingan disimpan, masukan perintah pada cmd sebagai berikut : 

**py laundrybojong.py**

Jika sudah akan keluar tampilan seperti berikut 

![image](https://user-images.githubusercontent.com/62027487/123367630-7b01cb00-d5a4-11eb-8319-d9d58e6b1cd6.png)

Lalu isikan nama, berat cucian, dan jenis paket. Perlu diingat untuk jenis paket hanya menyediakan 3 jenis paket, diantaranya yaitu : 

**Ekonomis (durasi 3 hari)** 

**Standar (durasi 2 hari)** 

**Kilat (durasi 1 hari)**

Jika sudah diproses, maka hasilnya akan keluar di **client_subscribe.py**

![image](https://user-images.githubusercontent.com/62027487/123367859-ec417e00-d5a4-11eb-87fb-3ce0e64cf7cb.png)



Selanjutnya, kita akan lanjut ke proses selanjutnya nomor 2, buka **client_subscribe.py** pada cmd dengan mengetik **py client_subscsribe.py**

![image](https://user-images.githubusercontent.com/62027487/123367252-d2536b80-d5a3-11eb-82a5-d091cb88cc7a.png)


Karena kita akan memilih nomor 2, maka ketik **"02"**

![image](https://user-images.githubusercontent.com/62027487/123368096-5a864080-d5a5-11eb-9b81-59a4885cf1cd.png)


Jika sudah, maka akan keluar tampilan seperti berikut

![image](https://user-images.githubusercontent.com/62027487/123368173-8275a400-d5a5-11eb-8e8c-ed7c1880f012.png)

Buka cmd pada direktori codingan disimpan, lalu ketik **"py laundrysoang.py"**

Jika sudah, maka akan keluar tampilan sebagai berikut : 

![image](https://user-images.githubusercontent.com/62027487/123368866-cfa64580-d5a6-11eb-860f-b8047204420e.png)

Lalu isikan nama, berat cucian, dan jenis paket. Perlu diingat untuk jenis paket hanya menyediakan 3 jenis paket, diantaranya yaitu : 

**Ekonomis (durasi 3 hari)** 

**Standar (durasi 2 hari)** 

**Kilat (durasi 1 hari)**

Jika sudah diproses, maka hasilnya akan keluar di **client_subscribe.py**

![image](https://user-images.githubusercontent.com/62027487/123368949-f4022200-d5a6-11eb-920d-787e1700f536.png)


Selanjutnya, kita akan lanjut ke proses selanjutnya nomor 3, buka **client_subscribe.py** pada cmd dengan mengetik **py client_subscsribe.py**

![image](https://user-images.githubusercontent.com/62027487/123367252-d2536b80-d5a3-11eb-82a5-d091cb88cc7a.png)

Karena kita akan memilih nomor 3, maka ketik **"03"**

![image](https://user-images.githubusercontent.com/62027487/123383146-05eebf80-d5bd-11eb-9b51-e3433df88ffa.png)

Jika sudah, maka akan keluar tampilan seperti berikut :

![image](https://user-images.githubusercontent.com/62027487/123383249-2880d880-d5bd-11eb-8fb7-46f7023c5642.png)

Isi nama, berat cucian, dan jenis paket. Jenis paket sudah dijelaskan pada penjelasan sebelumnya (Laundry Bojong dan Laundry Soang)

Berikut adalah hasil perbandingan dari kedua laundry tersebut berdasarkan berat cucian dan jenis paket yang telah diinput : 

![image](https://user-images.githubusercontent.com/62027487/123383472-67af2980-d5bd-11eb-8c2c-93f097cdab46.png)


Untuk pilihan no 4, disini program memutuskan untuk berhenti beroperasi, berikut adalah hasilnya : 

![image](https://user-images.githubusercontent.com/62027487/123383594-93caaa80-d5bd-11eb-86c0-75a81be6ca34.png)



























