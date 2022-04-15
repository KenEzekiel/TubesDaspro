# F08 - Membeli Game

def buy_game(game_data : list, my_game: list) :
    ID = str(input("Masukkan ID Game: "))
    for list in my_game:
        if ID in list: # If user already owned the game
            print("Anda sudah memiliki Game tersebut!")
        else:
            for list in game_data:
                if 0 in list: # If there's a lack of stock readily available
                    print("Stok Game tersebut sedang habis!")    
    
# Apabila game belum dimiliki, user memiliki saldo yang cukup, dan terdapat stok pada toko
# print("Game" + "HTTP" + "berhasil dibeli!")

# Apabila user tidak memiliki saldo yang cukup
# print("Saldo anda tidak cukup untuk membeli Game tersebut!")

# Examples regarding usage

data = [["GAME001","BNMO - Play Along With Crypto","Adventure","2022", 100000, 6], ["GAME069","Python Gemink","Programming","1991", 69000, 0], ["GAME666","Hehehe","Comedy","2012", 666000, 5]]
mine = [["GAME001", "BNMO - Play Along With Crypto", "Adventure", "2022", 100000]]
buy_game(data, mine)
