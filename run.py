from src.Controller import Controller


print("=== Welcome to Spotify Ripper ===")

while True:
    print("\nWhat would you like to do?")
    user_input = str(input("d - Download playlists from Spotify (by URL)\n" +
                           "u - Update previously downloaded playlists\n" +
                           "c - Enter individual songs to download\n" +
                           "r - Try to re-download failed songs\n" +
                           "q - Quit the program\n"))

    if user_input == "d":
        Controller.download_playlists()
    elif user_input == "u":
        Controller.redownload_playlists()
    elif user_input == "c":
        Controller.download_custom_songs()
    elif user_input == "r":
        Controller.download_failed_songs()
    elif user_input == "q":
        break
    else:
        print("ERROR: INVALID INPUT")

print("\nQuitting Spotify Ripper.....\n")