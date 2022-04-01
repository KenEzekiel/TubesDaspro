# Write data ke database dengan dictionary
import csv

def writer(file_name, rows):
    # Membuka file dalam mode write
    with open(f"Database/{str(file_name)}", 'w', encoding='UTF8', newline='') as file:
        # Membuat writer csv
        data_writer = csv.DictWriter(file, fieldnames="")

        # Write sebuah row ke database
        data_writer.writerow(rows)
'''
fieldnames = = ['name', 'area', 'country_code2', 'country_code3']

rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]
'''