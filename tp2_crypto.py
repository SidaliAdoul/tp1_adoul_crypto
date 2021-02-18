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
            print('the hash code: '+h.hexdigest())


sha_crypt()


def sha_256_crypt():
    sha_id = "Adoul Sidali Abdelkader Benmokhtar"
    x = 0x00005d10cc11e27bd8d4d1ce91bc725665ddbaa6ca2498ef38a88a58ad48cdb4
    coun = 0
    for i in range(1999, 4000):
        s1 = sha_id + str(i)
        h1 = hash.sha256(s1.encode())
        if h1.hexdigest() <= hex(x):
            coun += 1
            print('i to find the hash is: ' + str(i))
            print('Succes with count = ' + str(coun))
            print('the hash code: '+h1.hexdigest())


sha_256_crypt()
