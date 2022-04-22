# Python standard library
import os
import tkinter

# Local library
import standard
import readerwriter as rw
import B01_cipher
import B02_magicconch
import B03_TicTacToe
import F02_register
import F03_login
import F04_add_game
import F05_change_game
import F06_change_stock
import F07_game_listing
import F08_buy_game
import F09_list_game
import F10_search_my_game
import F11_search_game_at_store
import F12_topup
import F13_history
import F14_help
import F15_load
import F16_saver
import F17_exit


#---------- Main Program Function ------------
running = False
if F15_load.save_folder in F15_load.all_folder:
    print("Loading...")
    print('Welcome to the "Binomo" Interface')
    running = True
else:
    print(f'Folder "{F15_load.save_folder}" not found.')

filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
data = [rw.reader(F15_load.save_folder, file) for file in filenames]

admin_callable_commands = [
    'register',
    'login',
    'add_game',  # tambah_game in F04
    'change_game',  # ubah_game in F05
    'change_stock',  # ubah_stok in F06
    'list_available_game',  # list_game_toko in F07
    'search_at_store',  # search_game_at_store in F11
    'topup',
    'help',
    'save',
    'exit',
    'magicconch',
    'tictactoe'
]

user_callable_commands = [
    'login',
    'list_available_game',  # list_game_toko in F07
    'buy_game',
    'list_my_game',  # list_game in F09
    'search_my_game',
    'search_at_store',  # search_game_at_store in F11
    'history',  # riwayat in F13
    'help',  
    'save',
    'exit',
    'magicconch',
    'tictactoe'
]

logged_in = False

def inputCommand():
    global logged_in
    command = input_command.get()
    input_command.delete(0, tkinter.END)

    if not logged_in:

        if command not in ['help', 'login']:
            last_idx = output_field.index("end")
            output_field.insert(last_idx, f"You are not logged in. Please log in first. Enter \"help\" for more info.")
            print(f"You are not logged in. Please log in first. Enter \"help\" for more info.")

        elif command == 'help':
            F14_help.help("", F15_load.save_folder)

            last_index = command_field.index("end")
            command_field.insert(last_index, command)
            print("")

        elif command == 'login':
            login_valid = F03_login.login(F15_load.save_folder, data[3])
            if login_valid:
                global user_info
                last_idx = output_field.index('end')
                user_info = data[3][F03_login.user_line_index]
                output_field.insert(last_idx, 'Successfully logged in')
                print('Successfully logged in')
                logged_in = True

                last_index = command_field.index("end")
                command_field.insert(last_index, command)
                print("")

    else:

        if command in admin_callable_commands and command not in user_callable_commands and user_info[4] == 'Admin':

            if command == 'register':
                F02_register.register(data[3])
                last_idx = output_field.index('end')
                output_field.insert(last_idx, 'Successfully registered new user')

            elif command == 'add_game':
                data[0] = F04_add_game.add_game(data[0])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Added game")


            elif command == 'change_game':
                data[0] = F05_change_game.change_game(data[0])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Changed game")


            elif command == 'change_stock':
                data[0] = F06_change_stock.change_stock(data[0])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Changed game stock")


            elif command == "topup":
                data[3] = F12_topup.topup(data=data[3])
                #print(data[3])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "User balance updated")

            last_index = command_field.index("end")
            command_field.insert(last_index, command)
            print("")

        elif command in user_callable_commands and command not in admin_callable_commands and user_info[4] == 'User':
            
            if command == 'buy_game':
                F08_buy_game.buy_game(saldo=data[3][F03_login.user_line_index][5], game_data=data[0], my_game=data[1])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Bought a game")

            elif command == 'list_my_game':
                F09_list_game.list_game(data=data[1])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "All of your games are printed")

            elif command == 'search_my_game':
                F10_search_my_game.search_my_game(data[1], data[3], data[0])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Search result printed")

            elif command == 'history':
                F13_history.historyFromMatrix(data[2])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "History matrix printed")

            last_index = command_field.index("end")
            command_field.insert(last_index, command)
            print("")

        elif command in user_callable_commands and command in admin_callable_commands:
            
            if command == 'login':
                print("already logged in")

            elif command == 'list_available_game':
                F07_game_listing.sorting(data=data[0])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "List of all available game printed")

            elif command == 'search_at_store':
                F11_search_game_at_store.search_game_at_store(data=data[0])
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Searched the store")

            elif command == 'help':
                user = user_info[1]
                save_folder = F15_load.save_folder
                F14_help.help(user, save_folder)
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Printed Help")

            elif command == 'save':
                F16_saver.save(data)
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Saved data")

            elif command == 'exit':
                F17_exit.exit(data)
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Bye bye")

            elif command == 'magicconch':
                question = input("What do you want to ask the magic conch? \n")
                output = B02_magicconch.magicconch()
                print(output)
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "The Magic Conch gives its wisdom")
            
            elif command == 'tictactoe':
                B03_TicTacToe.tictactoe()
                last_idx = output_field.index("end")
                output_field.insert(last_idx, "Playing TicTacToe")


            last_index = command_field.index("end")
            command_field.insert(last_index, command)
            print("")
    
def exit_command():
    F17_exit.exit(data)    
    
#--------------- TKINTER ---------------------
root = tkinter.Tk()
root.geometry("480x640")
root.title("BNMO")
root.iconbitmap("resources/logo_itb.ico")
font_tuple = ("Arial", 10)

bg = tkinter.PhotoImage(file = "Resources/bg-image.png")
label_bg = tkinter.Label(root, image = bg)
label_bg.place(x = 0, y = 0)


input_frame = tkinter.Frame(root)
input_frame.place(x=62,y=310)

input_button_frame = tkinter.Frame(root)
input_button_frame.place(x=340,y=310)

# Creating A Main Frame
main_frame = tkinter.Frame(root,
                        bg="#7fbd91")
main_frame.place(x=72,y=72)

# Creating A Canvas
output_canvas = tkinter.Canvas(main_frame,
                            width=325,
                            height=185,
                            bg="#7fbd91")
output_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

# Creating a frame inside the canvas
output_frame = tkinter.Frame(output_canvas)
output_frame.pack()

exit_button_frame = tkinter.Frame(root)
exit_button_frame.place(x=415,y=580)

input_command = tkinter.Entry(input_frame, 
                            text="Command", 
                            font=font_tuple, 
                            bg="#B6D6EB", 
                            width = 33, 
                            borderwidth = 3)
input_button = tkinter.Button(input_button_frame, 
                            text="Execute", 
                            bg="#B6D6EB",
                            width = 11,
                            command=inputCommand)
command_field = tkinter.Listbox(output_frame,
                            height=7,
                            bg="#7fbd91")
command_field.insert(1, "Command Log: ")
output_field = tkinter.Listbox(output_frame,
                            height=7,
                            width=30,
                            bg="#7fbd91")
output_field.insert(1, "Output: ")
exit_button = tkinter.Button(exit_button_frame,
                            text="Exit", 
                            bg="#e53835",
                            command = exit_command,
                            width = 5,
                            height = 2)
input_command.grid(row=1, column=1)
input_button.grid(row=1, column=1)
exit_button.grid(row=1, column=1)
command_field.grid(row=1, column=1)
output_field.grid(row=1, column=2)

#---------------------------------------------

if running:
    root.mainloop()
    running = False
