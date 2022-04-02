import time

def magicconch():
    x = time.time()                     # Time factor as randomizer
    a = 3
    c = 1
    m = 7
    state = round(((a*x) + c) % m)      # Linear Congruential Generator (LCG)

    # States and outputs
    if state == 0:
        return "Coba lagi."
    elif state == 1:
        return "Ya."
    elif state == 2:
        return "Tidak."
    elif state == 3:
        return "Mungkin."
    elif state == 4:
        return "Jangan deh."
    elif state == 5:
        return "Tanya lagi nanti."
    elif state == 6:
        return "Terserah dah."
    elif state == 7:
        return "Coba tanya doswal."


"""for i in range(10):
    time.sleep(0.3)
    print(magicconch())"""
