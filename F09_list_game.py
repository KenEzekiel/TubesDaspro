# F09 - Melihat Game yang dimiliki

import standard

def list_game(game_data : list) :
    if (standard.length(data) == 0) : # Input validation
        # Present an error message because user haven't bought any game yet.
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else: # Valid output
        # Table structure:
        # ID | Game_name | Category | Release_year | Price
        print("Daftar game:")
        print(data)

# Examples regarding usage

"""
# Input example that will result in an error message as an output
data = []
list_game(data)
"""

# Input example that will result in a valid and proper output
data = [["GAME001", "BNMO - Play Along With Crypto", "Adventure", 2022, 100000], ["GAME069", "Python Gemink", "Programming", 1991, 69000], ["GAME666", "Hehehe", "Comedy", 2012, 666000]]
# list_game(data)
