import random


class Cinema(object):

    def __init__(self, movies):
        self.movies = movies

    def add_movie(self, film):
        if not self.movies:  # lista e goala
            if film.get_type() == "drama" or film.get_type() == "animatie":
                if 0 < film.get_duration() <= 180:
                    self.movies.append(film)
                elif film.get_duration() > 180:
                    try:
                        raise ValueError("filmul are mai mult de 180 de minute")
                    except ValueError:
                        print("Filmul nu va fi adaugat deaorece depaseste 180 de minute")

            else:
                print("\033[1;31;40m Filmul nu poate fi adaugat in lista deoarece nu este drama sau animatie.")
                print('\033[39m')
        else:
            if film.get_type() == "drama" or film.get_type() == "animatie":
                for movie in self.movies:
                    if movie.get_title() != film.get_title() or movie.get_duration() != film.get_duration():
                        if 0 < film.get_duration() <= 180:
                            self.movies.append(film)
                            break
                        elif film.get_duration() > 180:
                            try:
                                raise ValueError("filmul are mai mult de 180 de minute")
                            except ValueError:
                                print("\033[1;31;40m Filmul nu va fi adaugat deaorece depaseste 180 de minute")
                                print('\033[39m')
                    else:
                        print("Filmul se afla deja in lista de filme.")
            else:
                print("Filmul nu poate fi adaugat in lista deoarece nu este drama sau animatie.")

    def showing(self):
        for movie in self.movies:
            movie.showing()

    def showing_animation(self):
        for movie in self.movies:
            if movie.get_type() == "animatie":
                movie.showing()

    def pick_one_movie(self):
        my_movie = random.randint(0, len(self.movies) - 1)
        self.movies[my_movie].showing()

    def save_file(self, my_file):
        for movie in self.movies:
            movie.save_file(my_file)
