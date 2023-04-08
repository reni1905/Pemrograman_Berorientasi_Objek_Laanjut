class Sekolah:
    def __init__(self, nama, jumlah_siswa):
        self.nama = nama
        self.jumlah_siswa = jumlah_siswa

class Jurusan:
    def __init__(self, nama, sekolah):
        self.nama_jurusan = nama
        self.sekolah = sekolah

    def daftar_sekolah(self):
        for sekolah in self.sekolah:
            print(sekolah.nama, sekolah.jumlah_siswa)

sekolah1 = Sekolah("SMK CENDEKIA", 1000)
sekolah2 = Sekolah("SMP BANGODUA", 1500)

jurusan = Jurusan("Komputer Jaringan", [sekolah1, sekolah2])
jurusan.daftar_sekolah()