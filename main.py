from cinema import Cinema
from animatedMovie import AnimatedMovie
from dramaMovie import DramaMovie

if __name__ == "__main__":
    c = Cinema([])
    init = input("\033[1;31;40m Ce comanda vrei sa apelezi?")
    print('\033[39m')
    while True:
        if init == "adauga_drama":
            title = input("Ce titlu are filmul pe care vrei sa-l adaugi: ")
            mins = int(input("Cat dureaza filmul tau: "))
            age = int(input("Care este varsta minima: "))
            dramaMovie = DramaMovie(title, mins, "drama", age)
            c.add_movie(dramaMovie)
            print(end="\n")
            init = input("\033[1;31;40m Ce doriti sa faceti in continuare? (dati o comanda)")
            print('\033[39m')

        elif init == "adauga_animatie":
            title = input("Ce titlu are filmul pe care vrei sa-l adaugi: ")
            mins = int(input("Cat dureaza filmul tau: "))
            limba_dublare = input("In ce limba e dublat: ")
            animationMovie = AnimatedMovie(title, mins, "animatie", limba_dublare)
            c.add_movie(animationMovie)
            print(end="\n")
            init = input("\033[1;31;40m Ce doriti sa faceti in continuare? (dati o comanda)")
            print('\033[39m')

        elif init == "afisare_animatii":
            print(end="\n")
            print("\033[1;31;40m Aestea sunt filmele animate din biblioteca Cinematografului:")
            print('\033[39m')
            print(end="\n")
            c.showing_animation()
            print(end="\n")
            init = input("\033[1;31;40m Ce doriti sa faceti in continuare? (dati o comanda)")
            print('\033[39m')

        elif init == "afisare":
            print("\033[1;31;40m Acestea sunt toate filmele din biblioteca Cinematografului: ")
            print('\033[39m')
            c.showing()
            init = input("\033[1;31;40m Ce doriti sa faceti in continuare? (dati o comanda)")
            print('\033[39m')

        elif init == "alege_film":
            print("\033[1;31;40m Acesta este filmul ales(aleator): ")
            print('\033[39m')
            c.pick_one_movie()
            init = input("\033[1;31;40m Ce doriti sa faceti in continuare? (dati o comanda)")
            print('\033[39m')

        elif init == "salveaza_filme":
            moviesFile = open("fileWithMovies.txt", "w")
            c.save_file(moviesFile)
            moviesFile.close()
            print("\033[1;31;40m Filmele din cadrul Cinematografului au fost salvate in fisier")
            init = input("Ce doriti sa faceti in continuare? (dati o comanda)")
            print('\033[39m')

        elif init == "exit":
            break
