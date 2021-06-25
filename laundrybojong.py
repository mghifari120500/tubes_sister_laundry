# Library
import paho.mqtt.client as mqtt
import datetime
import time
import os

# Function untuk publish data
def publish(nama, berat, jenis_paket):
    # IP broker yang akan dituju
    ip_broker = 'localhost'
    # Buat client baru
    client = mqtt.Client('Bojong', clean_session=False)
    # Buat koneksi ke broker
    client.connect(ip_broker, port=2222)
    # Proses komunikasi
    client.loop_start()
    print('')
    print('Melakukan publishing data terhadap subscriber')
    time.sleep(3)
    print('')

    # Waktu pengajuan cucian
    t = datetime.datetime.now()
    TW_Pengajuan = str(t.strftime('%d-%m-%y')) + \
        ' ('+str(t.strftime('%H:%M:%S'))+') '

    # Waktu penjemputan cucian Laundry Bojong
    plus_minutes = t + datetime.timedelta(minutes=10)
    Penjemputan_Cucian = str(plus_minutes.strftime(
        '%d-%m-%y')) + ' ('+str(plus_minutes.strftime('%H:%M:%S'))+') '

    # Waktu Pengembalian cucian Laundry Bojong
    # Waktu 3 hari 10 menit setelah penjemputan cucian
    if jenis_paket == 'Ekonomis':
        plus_hours = t + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=10) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 2 hari 15 menit setelah penjemputan cucian
    elif jenis_paket == 'Standar':
        plus_hours = t + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=15) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 1 hari 10 menit setelah penjemputan cucian
    elif jenis_paket == 'Kilat':
        plus_hours = t + \
            datetime.timedelta(
                days=1) + datetime.timedelta(minutes=10) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '

    # Berat
    float_berat = float(berat)
    str_berat = str(float_berat) + ' Kg'

    # Harga Laundry Bojong
    # Jika menggunakan paket Ekonomis
    if jenis_paket == 'Ekonomis':
        # Berat kurang dari atau sama dengan 1kg = berat x 7000 + 500
        if float_berat <= 1:
            int_harga = int(float_berat * 7000)
            str_harga = str(int_harga) + ' + 500 = ' + str((int_harga) + 500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 10000 + 1000
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 10000)
            str_harga = str(int_harga) + ' + 1000 = ' + str((int_harga) + 1000)
        # Berat lebih dari 2kg = berat x 12000 + 1500
        else:
            int_harga = int(float_berat * 12000)
            str_harga = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)

    # Jika menggunakan paket Standar
    elif jenis_paket == 'Standar':
        # Berat kurang dari atau sama dengan 1kg = berat x 8000 + 1000
        if float_berat <= 1:
            int_harga = int(float_berat * 8000)
            str_harga = str(int_harga) + ' + 1000 = ' + str((int_harga) + 1000)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg =  berat x 11000 + 1500
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 11000)
            str_harga = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)
        # Berat lebih dari 2kg = berat x 13000 + 2000
        else:
            int_harga = int(float_berat * 13000)
            str_harga = str(int_harga) + ' + 2000 = ' + str((int_harga) + 2000)

    # Jika menggunakan paket Kilat
    elif jenis_paket == 'Kilat':
        # Berat kurang dari atau sama dengan 1kg = berat x 9000 + 1500
        if float_berat <= 1:
            int_harga = int(float_berat * 9000)
            str_harga = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 12000 + 2000
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 12000)
            str_harga = str(int_harga) + ' + 2000 = ' + str((int_harga) + 2000)
        # Berat lebih dari 2kg = berat x 14000 + 2500
        else:
            int_harga = int(float_berat * 14000)
            str_harga = str(int_harga) + ' + 2500 = ' + str((int_harga) + 2500)

    # Mempublish data ke client
    client.publish('datalaundry', ''+nama+'|'+TW_Pengajuan+'|'+str_berat+'|'+jenis_paket +
                   '|'+Penjemputan_Cucian+'|'+Pengembalian_Cucian+'|'+str_harga+'', qos=1, retain=False)

    client.loop_stop()


# Main Program
loop = True
while loop:
    os.system('cls')
    print('')
    print('+------------------------------------------+')
    print('|        Masukan data Laundry Bojong       |')
    print('+------------------------------------------+')
    # 1. Nama
    Nama = input('Nama        : ')
    # 2. Berat
    Berat = input('Berat       : ')
    # 3. Jenis Paket
    Jenis_Paket = input('Jenis Paket : ')
    if Jenis_Paket == 'Ekonomis' or Jenis_Paket == 'Standar' or Jenis_Paket == 'Kilat':
        publish(Nama, Berat, Jenis_Paket)
        pil = input('Coba lagi? [Y/n] ')
        if pil == 'Y' or pil == 'y':
            time.sleep(3)
            loop = True
        else:
            loop = False
            time.sleep(3)
            print('')
            print('Keluar dari program...')
    else:
        time.sleep(3)
        print('')
        print('+-----------------------------------+')
        print('|       Mohon maaf, input salah     |')
        print('+-----------------------------------+')
        pil = input('Coba lagi? [Y/n] ')
        if pil == 'Y' or pil == 'y':
            time.sleep(3)
            loop = True
        else:
            loop = False
            time.sleep(3)
            print('')
            print('Program berhenti...')