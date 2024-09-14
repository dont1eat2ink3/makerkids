file = open ("videogames.csv","r")
def display_games():
    for line in file :
        data = line.split(",")
        
        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        print("Title: " + title)
        print("Release year: " + release_year)
        print("Genre: " + genre)
        print("Developer: " + developer)
        print("Platform: " + platform)
display_games()
def list_games_by_year():
    year = input("What year are you the most interested in?")
    for line in file :
        data = line.split(",")
        
        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        print("Title: " + title)
        print("Release year: " + release_year)
        print("Genre: " + genre)
        print("Developer: " + developer)
        print("Platform: " + platform)
list_games_by_year()



def developer():
    dev = input("What developer are you the most interested in?")
    for line in file :
        data = line.split(",")
        
        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        print("Title: " + title)
        print("Release year: " + release_year)
        print("Genre: " + genre)
        print("Developer: " + developer)
        print("Platform: " + platform)
developer()

