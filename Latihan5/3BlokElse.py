try:
    # buka file dan baca isinya
    with open('file.txt', 'r') as file:
        data = file.read()

    # ubah teks menjadi bilangan bulat
    num = int(data)

except FileNotFoundError:
    print("File tidak ditemukan!")
except ValueError:
    print("Isi file harus berupa bilangan bulat!")
else:
    # jika tidak terjadi kesalahan, tampilkan hasil konversi
    print("Isi file berhasil dikonversi menjadi bilangan bulat:", num)