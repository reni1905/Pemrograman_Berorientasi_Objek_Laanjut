try:
    inp = input("masukkan input:")
    print ('Tekan Ctrl+c')
except KeyboardInterrupt:
    print ('Tertangkap KeyboardInterrupt')
else:
    print ('Tidak ada except yang terjadi')