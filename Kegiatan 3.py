# Fungsi untuk menghitung nilai akhir satu mahasiswa
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("\nHasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("\nNama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Shabrina': {'uts': 85, 'uas': 90},
        'Novia': {'uts': 70, 'uas': 75},
        'Haikal': {'uts': 95, 'uas': 88},
        # Masukkan data mahasiswa lainnya
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
