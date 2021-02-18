import hashlib as hash


def sha_crypt():
    sha_id = "Adoul Sidali Abdelkader Benmokhtar"
    y = 0x03b1663dda6549a0939ffdd712a852e0d4234e6b
    count = 0
    for i in range(1999, 2050):
        s = sha_id + str(i)
        h = hash.sha1(s.encode())
        if h.hexdigest() <= hex(y):
            count += 1
            print('i to find the hash is: ' + str(i))
            print('Succes with count = ' + str(count))


sha_crypt()