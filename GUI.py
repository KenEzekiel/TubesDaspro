import tkinter
#import loader
import readerwriter

#--------------- TKINTER ---------------------
root = tkinter.Tk()
root.title("PROGRAM")
#root.iconbitmap("resources/logo_itb.ico")

font_tuple = ("Colibri", 10)

input_command = tkinter.Entry(root, text="Command", font=font_tuple, bg="#B6D6EB")
input_command.grid(row=1, column=1)
output_field = tkinter.Label(root, text="test", font=font_tuple, bg="#B6D6EB")
output_field.grid(row=2, column=1)
#---------------------------------------------

"""running = False
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
    running = False"""

root.mainloop()