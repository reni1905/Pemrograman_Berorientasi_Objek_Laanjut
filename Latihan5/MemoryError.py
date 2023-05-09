#mengatasi MemoryError
try:
    data = " " * (10**10)
except MemoryError:
    print("Memory tidak cukup untuk menampung data yang diminta!")