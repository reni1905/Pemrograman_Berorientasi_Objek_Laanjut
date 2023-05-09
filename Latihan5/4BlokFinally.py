try:
    file = open("file.txt", "r")
    num = int(file.readline())
except ValueError:
    print("Error: input tidak valid!")
finally:
    file.close()