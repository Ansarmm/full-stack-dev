print("Welcome to the Music Library")
def print_music_titles_from_file():
    try:
        with open("music-library.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Music library file not found.")

print_music_titles_from_file()

