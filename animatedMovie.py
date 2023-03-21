from movie import Movie


class AnimatedMovie(Movie):
    def __init__(self, title, time, movie_type, dubbing_language):
        super().__init__(title, time, movie_type)
        self.dubbing_language = dubbing_language

    def dubbing_language(self):
        return self.dubbing_language

    def showing(self):
        print("Genul filmului este: " + self.movie_type)
        print("Titlul filmului este: " + self.title)
        print("Durata filmului este: ", self.time)
        print(f"Limba in care este dublat filmul este: {self.dubbing_language}")

    def reading(self):
        self.movie_type = input("Ce gen este filmul?")
        self.title = input("Cum se numeste filmul?")
        self.time = int(input("Cat dureaza filmul?"))
        self.dubbing_language = input("In ce limba e dublat?")

    def get_type(self):
        return "animatie"

    def save_file(self, my_file):
        my_file.writelines(f"Filmul {self.title} este de genul {self.movie_type} si dureaza {self.time}"
                           f" minute si limba in care este dublat este {self.dubbing_language}\n")
