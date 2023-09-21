# Music Playlist Manager

playlist = []

def display_menu():
    print("\nWelcome to Music Playlist Manager:")
    print("\nMenu:\n")
    menu = [
        'a. Add a song to the playlist',
        'b. Remove a song from the playlist',
        'c. View the current playlist',
        'd. Quit the program'
    ]
    for item in menu:
        print(item)

def add_song(song_name):
    if song_name not in playlist:
        playlist.append(song_name)
        print(f"{song_name} has been added to the playlist")
    else:
        print("Song already exists in the playlist")

def remove_song(song_name):
    if song_name in playlist:
        playlist.remove(song_name)
        print(f"{song_name} has been removed from the playlist")
    else:
        print(f"{song_name} is not in the playlist")

def view_playlist():

    print("\nCurrent Playlist:")
    if not playlist:
        print("The playlist is empty")
    else:
        index = 1
        for song in playlist:
            print(f"{index}: {song}")
            index += 1

def main():
    while True:
        display_menu()
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "a":
            song_name = input("Enter the song name: ").lower()
            add_song(song_name)
        elif user_choice == "b":
            view_playlist()
            song_name = input("Enter the song name to remove: ").lower()
            remove_song(song_name)
        elif user_choice == "c":
            view_playlist()
        elif user_choice == "d":
            print("Exiting Music Playlist Manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option (a, b, c, or d).")

main()

