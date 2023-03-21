from movie import Movie


class DramaMovie(Movie):
    def __init__(self, title, time, movie_type, min_age):
        super().__init__(title, time, movie_type)
        self.min_age = min_age

    def showing(self):
        print("Genul filmului este: " + self.movie_type)
        print("Titlul filmului este: " + self.title)
        print("Durata filmului este: ", self.time)
        print("Varsta minima este: ", self.min_age)

    def reading(self):
        self.movie_type = input("Ce gen este filmul?")
        self.title = input("Cum se numeste filmul?")
        self.time = int(input("Cat dureaza filmul?"))
        self.min_age = int(input("Care este varsta minima?"))

    def get_min_age(self):
        return self.min_age

    def get_type(self):
        return "drama"

    def save_file(self, my_file):
        my_file.writelines(f"Filmul {self.title} este de genul {self.movie_type} si dureaza {self.time}"
                           f" minute si varsta minima este {self.min_age}\n")
