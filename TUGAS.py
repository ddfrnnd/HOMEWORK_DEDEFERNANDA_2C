data = []
def insert():

    nama = input('nama barang : ')
    stok = int(input('stok barang : '))
    data_baru = {'nama : ',nama,'stok : ',stok}
    data.append(data_baru)
def view_data():
    if not data:
       print('='*6,'Stok barang Kosong','='*6)
    else:    
     for i in data :
        print('-',i['nama'],i['stok'])
def hapus_data():
    id = int(input('Hapus data index ke : '))
    del data[id]
    print('hapus data berhasil')
def edit_data():
    view_data()
    id = int(input('Masukan data yang akan diedit: '))
    if 0 <= id and id < len(data):
        print(f'Edit data {data[id]["nama"]}')
        new_nama = input('Nama baru: ')
        new_stok = int(input('stok baru: '))
        data[id]['nama'] = new_nama
        data[id]['stok'] = new_stok
        print(f'Data {id} berhasil di edit')
    else:
        print('Gagal diedit')
def jumlah_data():
    print(f'total data: {len(data)}')
def cari_data():
    nama_cari = input('Masukan nama barang yang dicari: ')
    for item in (data):
        if nama_cari.lower() in item["nama"].lower():
            print(f'- nama: {item["nama"]} stok: {item["stok"]}')
        else:
            print('data tidak ditemukan')
