import standard

def change_game (game_data : list):
    id = int(input("Masukkan ID game: "))
    found = False
    i = 1
    while (found == False) and (i < standard.length(game_data)):      # Loop for every line in file game.csv (index 3 on folder save) (ignore the first line)
        if  id == game_data[i][0]:
            line_index = i
            found = True
        else :
            i += 1
    if found == False :
        print("Tidak ada game dengan ID tersebut!")
    else :    
        name = str(input("Masukkan nama game: "))
        if name != "" :
            game_data[line_index][1] = name
        category = str(input("Masukkan kategori: "))
        if category != "" :
            game_data[line_index][2] = category
        release_year = str(input("Masukkan tahun rilis: "))
        if release_year != "" :
            game_data[line_index][3] = release_year
        price = str(input("Masukkan harga: "))
        if price != "" :
            game_data[line_index][4] = int(price)

# data =[[1,"binomo","action","1990",17000,6], [1,"oscta","action","1990",17000,6], [5,"mario","adventure","2022",10000,5]]
# change_game(data)
# print(data)

