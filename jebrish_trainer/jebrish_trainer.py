from random import randint, choice
import string 

def jt():
    all_lower = list(string.ascii_lowercase)
    all_upper = list(string.ascii_uppercase)

    others = [", ", " ", "; "]
    enders = [". ", "! ", "? "]
    
    sl = randint(1,100)
    setn = choice(all_upper)
    words = []
    for _ in range(sl):
        wl = randint(1,30)
        w = ""
        for _ in range(wl):
            w += choice(all_lower)

        w += choice(others)

        words.append(w)

    words[0] = setn + words[0]

    sentense = "".join(words)[:-2]

    return sentense #+ choice(enders)


if __name__ == "__main__":
    res = jt()

    print(res)




