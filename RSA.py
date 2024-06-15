import random
import math

# Lưu các số nguyên tố
prime = set()

public_key = None
private_key = None
n = None

# Sàng nguyên tố
def primefiller():
    is_prime = [True] * 10000
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, 100):
        if is_prime[i] == True:
            for j in range(i * i, 10000, i):
                is_prime[j] = False

    for i in range(len(is_prime)):
        if is_prime[i]:
            prime.add(i)


# Chọn ngẫu nhiên một số nguyên tố và xóa số nguyên tố đó
# số trong danh sách vì p!=q
def pickrandomprime():
    global prime
    k = random.randint(0, len(prime) - 1)
    it = iter(prime)
    for _ in range(k):
        next(it)

    ret = next(it)
    prime.remove(ret)
    return ret


def setkeys():
    global public_key, private_key, n
    prime1 = pickrandomprime() # First prime number
    prime2 = pickrandomprime() # Second prime number

    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)

    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1

    # d = (k*Φ(n) + 1) / e for some integer k
    public_key = e

    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1

    private_key = d


# To encrypt the given number
def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text


# To decrypt the given number
def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= n
        d -= 1
    return decrypted



def encoder(message):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded


def decoder(encoded):
    s = ''
    # Calling the decrypting function decoding function
    for num in encoded:
        s += chr(decrypt(num))
    return s


if __name__ == '__main__':
    primefiller()
    setkeys()

    while True:
        print("1. Nhập chuỗi:")
        print("2. Mã hóa chuỗi:")
        print("3. Giải mã:")
        print("4. Thoát")
        choice = int(input("Nhập lựa chọn: "))

        if choice == 1:
            message = input("Nhập nội dung cần mã hóa: ")
        elif choice == 2:
            coded = encoder(message)
            print("\nTin nhắn được mã hóa\n")
            print(''.join(str(p) for p in coded))
        elif choice == 3:
            decoded = decoder(coded)
            print("\nTin nhắn được giải mã\n")
            print(decoded)
        elif choice == 4:
            break
        else:
            print("Lựa chọn không hợp lệ.")