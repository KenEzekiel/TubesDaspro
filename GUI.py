import tkinter
import standard
import loader
import readerwriter as rw
import history
import topup 
import os
#---------- Main Program Function ------------
running = False
if loader.save_folder in loader.all_folder:
    print("Loading...")
    print('Welcome to the "Binomo" Interface')
    running = True
else:
    print(f'Folder "{loader.save_folder}" not found.')

filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
data = [rw.reader(loader.save_folder, file) for file in filenames]

callable_commands = {
    'history': history,
    'topup' : topup
}

def inputCommand():
    command = input_command.get()
    input_command.delete(0, tkinter.END)
    if command in callable_commands:
        if command == "history":
            history.historyFromMatrix(data[2])
            last_idx = output_field.index("end")
            output_field.insert(last_idx, "History matrix printed")
        elif command == "topup":
            topup.topup(data[3])
            print(data[3])
            last_idx = output_field.index("end")
            output_field.insert(last_idx, "User balance updated")

        last_index = command_field.index("end")
        command_field.insert(last_index, command)
    else:
        print("Command Not Found")
    
    
#--------------- TKINTER ---------------------
root = tkinter.Tk()
root.geometry("480x640")
root.title("PROGRAM")
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
                            command = quit,
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

    