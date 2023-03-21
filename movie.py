class Movie(object):
    def __init__(self, title, time, movie_type):
        self.title = title
        self.time = time
        self.movie_type = movie_type

    def showing(self):
        print("Genul filmului este:" + self.movie_type)
        print("Titlul filmului este: " + self.title)
        print("Durata filmului este: ", self.time)

    def get_title(self):
        return self.title

    def get_duration(self):
        return self.time

    def get_type(self):
        return self.movie_type

    def save_file(self, my_file):
        my_file.writelines(f"Filmul {self.title} de genul {self.movie_type} minute are durata {self.time}\n")
