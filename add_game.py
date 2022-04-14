import standard

# not to be imported
def new_game(game_data : list) :
    """
    Procedure to get input for a new game with validation
    """
    complete = False 
    while complete == False :                       # loop for input validation
        name = str(input("Masukkan nama game: "))
        category = str(input("Masukkan kategori: "))
        release_year = str(input("Masukkan tahun rilis: "))
        price = str(input("Masukkan harga: "))
        stock = str(input("Masukkan stok awal: "))
        if standard.length(name) == 0 or standard.length(category) == 0 or standard.length(release_year) == 0 or standard.length(price) == 0 or standard.length(stock) == 0 :
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        else :
            complete = True

    new_index = game_data[standard.length(game_data)-1][0] + 1       # generating index for the new game by fetching the latest index from the database + 1
    new_data = [new_index , name, category, release_year, int(price), int(stock)]

    return new_data

def add_game (game_data : list) :
    """
    Procedure to add a new valid game to the inventory
    """
    new_data = new_game(game_data)
    print(new_data)
    game_data = standard.append(game_data, new_data) 
    print(game_data)
    print("Selamat! Berhasil menambahkan game", new_data[1] + "." )
    

"""
# Example on how to use
print(data[0])
add_game(data[0])
print(data[0])

data =[[1,"binomo","action","1990",17000,6], [1,"oscta","action","1990",17000,6], [5,"mario","adventure","2022",10000,5]]
add_game(data)
print(data)

"""
data =[[1,"binomo","action","1990",17000,6], [1,"oscta","action","1990",17000,6], [5,"mario","adventure","2022",10000,5]]
add_game(data)
print(data)