import standard

def change_stock(game_data : list) :
    id = int(input("Masukkan ID game: "))
    found = False
    i = 1
    while found == False and i < standard.length(game_data):      # Loop for every line in file game.csv (index 3 on folder save) (ignore the first line)
        if  id == game_data[i][0]:
            line_index = i
            found = True
        else :
            i += 1
    if found == False :
        print("Tidak ada game dengan ID tersebut!")
    else :    
        added_stock = int(input("Masukkan jumlah: "))
        if game_data[line_index][5] + added_stock < 0 :
            print("Stok game", game_data[line_index][1],"gagal dikurangi karena stok kurang. Stok sekarang:", game_data[line_index][5], "(<", abs(added_stock) + ")")
        else :
            game_data[line_index][5] += added_stock
            print("Stok game", game_data[line_index][1], "berhasil dikurangi. Stok sekarang:", game_data[line_index][5])


# data =[[1,"binomo","action","1990",17000,6], [1,"oscta","action","1990",17000,6], [5,"mario","adventure","2022",10000,5]]
# change_stock(data)
# print(data)