# mengatasi AttributeError
class Manusia:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur

manusia = Manusia()

try:
    print(manusia.alamat)

except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")