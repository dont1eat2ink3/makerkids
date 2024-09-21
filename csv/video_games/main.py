file = open("videogames.csv", "r")

def display_games():
    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]
        
        print("Title: " + title)
        print("Release Year: " + release_year)
        print("Genre: " + genre)
        print("Developer: " + developer)
        print("Platform: " + platform)
        print()


def list_games_by_year():
    year = input("What year are you interested in? ")

    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        if year == release_year:
            print("Title: " + title)
            print("Release Year: " + release_year)
            print("Genre: " + genre)
            print("Developer: " + developer)
            print("Platform: " + platform)
            print()


def list_games_by_developer():
    dev = input("Which Developer are you interested in? ")

    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        if dev.lower() == developer.lower():
            print("Title: " + title)
            print("Release Year: " + release_year)
            print("Genre: " + genre)
            print("Developer: " + developer)
            print("Platform: " + platform)
            print()

def list_games_by_genre():
    user_genre = input("Which Genre are you interested in? ")

    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        if user_genre.lower() == genre.lower():
            print("Title: " + title)
            print("Release Year: " + release_year)
            print("Genre: " + genre)
            print("Developer: " + developer)
            print("Platform: " + platform)
            print()


# def list_games_before_year():
#     user_year = int(input("Enter a year: "))

#     with open("videogames.csv", "r") as file:
#         next(file)

#         for line in file:
#             data = line.split(",")

#             title = data[0]
#             release_year = data[1]
#             genre = data[2]
#             developer = data[3]
#             platform = data[4]

#             if int(release_year) <= user_year:
#                 print("Title: " + title)
#                 print("Release Year: " + release_year)
#                 print("Genre: " + genre)
#                 print("Developer: " + developer)
#                 print("Platform: " + platform)
#                 print()

#display_games()
#list_games_by_year()
# list_games_by_developer()
#list_games_by_genre()
# list_games_before_year()


def list_games_by_platform():
    user_platform = input("Enter a platform: ")

    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        if user_platform.lower() in platform.lower():
            print("Title: " + title)
            print("Release Year: " + release_year)
            print("Genre: " + genre)
            print("Developer: " + developer)
            print("Platform: " + platform)
            print()


list_games_by_platform()