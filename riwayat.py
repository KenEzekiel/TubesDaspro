import readerwriter
import standard

def riwayat(save_folder):
    data_riwayat = readerwriter.reader(save_folder, "riwayat.csv")
    length_data = standard.length(data_riwayat)

    if length_data == 1:
        print("")
    else:
        print("")