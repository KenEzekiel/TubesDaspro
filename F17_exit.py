# Bantuan yang dibutuhkan:
# Jika y adalah input pertama, fungsi quit() berhasil
# Tapi, jika diberi input selain y atau n, kenapa fungsinya malah terjebak di loop while meski sudah diberi input yang benar?

def exit(x):
    # Misalkan, input tidak valid
    # Maka program menanyakan ulang. Input harus berlaku untuk Y atau N dalam huruf kecil maupun besar.
    while (x != "y") and (x != "Y") and (x != "n") and (x != "N"):
        print("")
        print("Input tidak dikenali. Mohon gunakan input berupa (y/n)")
        exit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (x == "y") or (x == "Y"): # Menjalankan prosedur save dan program selesai
        quit()
    elif (x == "n") or (x == "N"): # Menjalankan program seperti biasa dan program tidak selesai, meminta perintah berikutnya
        print("Dimengerti, silahkan gunakan program lain yang tersedia.")

x = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
exit(x)
