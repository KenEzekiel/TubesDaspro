import loader

running = False
if loader.save_folder in loader.all_folder:
    print("Loading...")
    print('Welcome to the "Binomo" Interface')
    running = True
else:
    print(f'Folder "{loader.save_folder}" not found.')

while running:
    command = input("command: ")
    running = False