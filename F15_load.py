import argparse
import os


"""
Procedure to load the data into the database, is called automatically
when running the file in the command prompt with
> python GUI.py {save_folder}
"""

parser = argparse.ArgumentParser()
parser.add_argument("folder", help ="the save file that is want to be loaded")
args = parser.parse_args()

save_folder = args.folder
all_folder = next(os.walk("Database"))[1]


# if save_folder in all_folder:
#     print("Loading...")
#     print('Welcome to the "Binomo" Interface')
# else:
#     print(f'Folder "{save_folder}" not found.')
# included in GUI.py, this is for file testing purposes
