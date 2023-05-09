try:
    # buka file dan baca isinya
    with open('file.txt', 'r') as file:
        data = file.read()

    # ubah teks menjadi bilangan bulat
    num = int(data)

    # bagi dengan angka ang diinputkan oleh user
    divisor = int(input("Masukkan angka pembagi: "))
    result = num / divisor

    # tampilkan hasil bagi
    print("Hasil bagi adalah:", result)

# tangani beberapa jenis exception
except FileNotFoundError:
    print("File tidak ditemukan!")
except ValueError:
    print("Isi file harus berupa bilangan bulat!")
except ZeroDivisionError:
    print("Angka pembagi tidak boleh nol!")
except Exception as e:
    print("Terjadi kesalahan:", str(e))