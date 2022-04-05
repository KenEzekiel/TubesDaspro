import loader
import readerwriter

running = False
if loader.save_folder in loader.all_folder:
    print("Loading...")
    print('Welcome to the "Binomo" Interface')
    running = True
else:
    print(f'Folder "{loader.save_folder}" not found.')

while running:
    command = input("command: ")
    filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
    data = [readerwriter.reader(loader.save_folder, file) for file in filenames]
    print(data)
    running = False