import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("folder", help ="loads the data in the folder into the program")
args = parser.parse_args()

save_folder = args.folder
all_folder = next(os.walk("Database"))[1]

'''
if save_folder in all_folder:
    print("Loading...")
    print('Welcome to the "Binomo" Interface')
else:
    print(f'Folder "{save_folder}" not found.')
# included in GUI.py, this is for file testing purposes
'''
