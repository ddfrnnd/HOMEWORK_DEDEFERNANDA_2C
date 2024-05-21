import TUGAS as db

while True :
   print('='*8,'selamat datang di program Manajemen stok barang! ','='*8)
   print('pilihan: ')
   print('1. Tambah data barang ')
   print('2. hapus data barang ')
   print('3. tampilkan data barang ')
   print('4. edit data ')
   print('5  Jumlah data ')
   print('6  Cari data ')
   print('7  keluar')
   pilihan = int(input('masukan plihan ')) 
   if pilihan == 1:
      db.insert()
   elif pilihan == 2:
      db.hapus_data()
   elif pilihan == 3:
      db.view_data()
   elif pilihan == 4:
      db.edit_data()
   elif pilihan == 5:
      db.jumlah_data()
   elif pilihan == 6:
      db.cari_data()
   elif pilihan == 7:
     print('Arigato sudah berkunjung')
     break
