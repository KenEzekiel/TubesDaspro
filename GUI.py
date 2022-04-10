import tkinter
import standard
import loader
from readerwriter import *
from history import *
import os
#---------- Main Program Function ------------
callable_commands = {
    'reader' : reader,
    'writer' : writer,
    'history': history,
    
}

def inputCommand():
    global command
    command = input_command.get()
    input_command.delete(0, tkinter.END)
    last_index = output_field.index("end")
    output_field.insert(last_index, command)
    if command in callable_commands:
        func = callable_commands[f"{command}"]
        func(loader.save_folder)
    else:
        print("Command Not Found")
    

def readOutput(string):
    output = tkinter.Label(output_frame,
                        text=string,
                        bg="#7fbd91", 
                        anchor="w").pack()
    


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

"""
# Adding a scrollbar to the Canvas
scrollbar = tkinter.Scrollbar(main_frame, orient=tkinter.VERTICAL, command=output_canvas.yview)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# Configuring the Canvas
output_canvas.configure(yscrollcommand=scrollbar.set)
output_canvas.bind('<Configure>', lambda e: output_canvas.configure(scrollregion=output_canvas.bbox("all")))
"""
# Creating a frame inside the canvas
output_frame = tkinter.Frame(output_canvas)
output_frame.pack()
"""
# Adding the output_frame to a window in the canvas
output_canvas.create_window((0, 0), window = output_frame_1, anchor="nw")
"""
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
output_field = tkinter.Listbox(output_frame,
                            height=7,
                            bg="#7fbd91")
output_field.insert(1, "Output: ")
exit_button = tkinter.Button(exit_button_frame,
                            text="Exit", 
                            bg="#e53835",
                            width = 5,
                            height = 2)
input_command.grid(row=1, column=1)
input_button.grid(row=1, column=1)
exit_button.grid(row=1, column=1)
output_field.pack(fill=tkinter.BOTH, expand=1)

#---------------------------------------------

running = False
if loader.save_folder in loader.all_folder:
    print("Loading...")
    print('Welcome to the "Binomo" Interface')
    running = True
else:
    print(f'Folder "{loader.save_folder}" not found.')

if running:
    root.mainloop()
    
    filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
    data = [reader(loader.save_folder, file) for file in filenames]
    print(data)
    running = False

    