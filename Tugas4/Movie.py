class Movie:
    def __init__(self, genre, durasi):
        self.genre = genre
        self.durasi = durasi

class Youtube:
    def __init__(self, genre, movie):
        self.genre = genre
        self.movie = movie

    def daftar_movie(self):
        for movie in self.movie:
            print(movie.genre, movie.durasi)

movie1 = Movie("Tarzan", 50.00)
movie2 = Movie("Mowgli", 30.00)

youtube = Youtube("Streaming", [movie1, movie2])
youtube.daftar_movie()