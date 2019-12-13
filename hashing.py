import hashlib

while True:
    if input("1 to hash, 2 to crack: ") == "1":
        string = input("Your string to hash: ")
        print("md5 : " + hashlib.md5(string.encode()).hexdigest())
        print("sha1 : " + hashlib.sha1(string.encode()).hexdigest())
        print("sha224 : " + hashlib.sha224(string.encode()).hexdigest())
        print("sha256 : " + hashlib.sha256(string.encode()).hexdigest())
        print("sha384 : " + hashlib.sha384(string.encode()).hexdigest())
        print("sha512 : " + hashlib.sha512(string.encode()).hexdigest())
    else:
        crack = input("Your hash: ")
        file = input("Wordlist file: ")
        with open(file,"r") as fil:
            words = fil.read().split("\n")
        if len(crack) == 32:
            for w in words:
                if hashlib.md5(w.encode()).hexdigest() == crack:
                    print(w)
                    break
        elif len(crack) == 40:
            for w in words:
                if hashlib.sha1(w.encode()).hexdigest() == crack:
                    print(w)
                    break
        elif len(crack) == 56:
            for w in words:
                if hashlib.sha224(w.encode()).hexdigest() == crack:
                    print(w)
                    break
        elif len(crack) == 56:
            for w in words:
                if hashlib.sha224(w.encode()).hexdigest() == crack:
                    print(w)
                    break
        elif len(crack) == 64:
            for w in words:
                if hashlib.sha256(w.encode()).hexdigest() == crack:
                    print(w)
                    break
        elif len(crack) == 96:
            for w in words:
                if hashlib.sha368(w.encode()).hexdigest() == crack:
                    print(w)
                    break
        elif len(crack) == 128:
            for w in words:
                if hashlib.sha512(w.encode()).hexdigest() == crack:
                    print(w)
                    break
        else:
            print("Not a recognised hashing function")
        
