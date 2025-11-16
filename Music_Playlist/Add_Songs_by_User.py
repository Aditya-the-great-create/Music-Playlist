print("Welcome to Aditya's Musicals\n")

while True:
    Name = input("Please enter your name: ")
    if Name.isalpha():
       print(f"Hello, {Name}")
       break
    else:
        print("Enter your name again")

album = []

while True:

    print("Select the following: \n"
          "1. Add song to playlist\n"
          "2. View the playlist\n"
          "3. Remove song\n"
          "4. Search\n"
          "5. Exit\n")

    choice = input("Enter the choice number: \n")

    if choice == "1":

        Album = input("Enter the Album name: ")
        Artist = input("Enter the Artist name: ")
        Year = int(input("Enter the Year: "))

        song = {
            "Album": Album,
            "Artist": Artist,
            "Year": Year,
        }

        album.append(song)
        print(f"{Album} by {Artist} added to {Name}'s playlist")


    elif choice == "2":
        if len(album) == 0:
            print("No songs added to the playlist.")
        else:
            for i, song in enumerate(album, start=1):
                print(f"{i}. {song['Album']} - by {song['Artist']} - {song['Year']}")


    elif choice == "3":

        def remove_song():
            if not album:
                print("No songs in playlist! Enter option to add songs\n")
            else:
                print(f"{Name}'s Playlist: \n")
                for i, song in enumerate(album, start=1):
                    print(f"{i}. {Album}")

            try:
                songs_number = int(input("Enter the song choice of your playlist: "))
                if 1 <= songs_number <= len(album):
                    removed_song = album.pop(songs_number - 1)
                    print(f"Removed '{removed_song['Album']}'")
                else:
                    print("The song is not in the playlist")
            except ValueError:
                print("The choice is incorrect! Enter the correct choice number\n")
        remove_song()

    elif choice == "4":
        def search_song():

            if not album:
                print(f"No such song present in the playlist")
            else:
                text = input("Search: ").lower()
                i = 0
                length = len(album)
                found = False


                while i < length:
                    if text in album[i]["Album"].lower() :
                        print(f"{text} is present in the playlist")
                        found = True
                    i += 1

                if not found:
                    print(f"{text} not present in the playlist")


        search_song()


    elif choice == "5":

        print("Exiting")
        break


    else:
        print("Choose again from Choice 1, 2, 3")
