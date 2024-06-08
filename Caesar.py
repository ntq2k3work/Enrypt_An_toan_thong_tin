def encrypt(message,key):
    encrypted_message = ""
    for i in message :
        encrypted_message += english_alphabet[(english_alphabet.find(i) + key) % 26]
    return encrypted_message

def decrypt(message,key):
    decrypted_message = ""
    for i in message :
        decrypted_message += english_alphabet[(english_alphabet.find(i) - key)]
    return decrypted_message
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
def menu():
    print("1.Nhập nội dung và key .")
    print("2.Mã hoá nội dung vừa nhập .")
    print("3 Giải mã nội dung đã mã hoá.")
    while True:
        choose = input("Nhập lựa chọn : ")
        if choose == '1' :
            message = input("Nhập nội dung : ")
            key = int(input("Nhập key (int): "))
        elif choose == '2':
            message = encrypt(message,key)
            print(f"Nội dung sau khi mã hoá là {message}")
        elif choose == '3':
            message = decrypt(message,key)
            print(f"Nội dung sau khi giải mã là {message}")
        else:
            break
menu()
            