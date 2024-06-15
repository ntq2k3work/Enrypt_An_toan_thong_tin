import numpy as np
from math import *
from math import sqrt,floor,ceil
def convertKeyToMatrix(key,m):
    matrix_key = []
    k = 0
    for i in range(m) :
        matrix_key.append([])
        for j in range(m) :
            matrix_key[i].append(key[k])
            k +=1
    return matrix_key
def convertToMatrix(text,m):
    matrix_text = []
    k = 0
    for i in range(ceil(len(text)/m)) :
        matrix_text.append([])
        for j in range(m):
            if k < len(text) :
                matrix_text[i].append(english_alphabet.find(text[k]))
                k+=1
    return matrix_text
def UCLN(a,b):
    if b == 0:
        return a
    return UCLN(b,a%b)
def encrypt(matrix_key,matrix_text,m):
    matrix_text1 = np.array(matrix_text)
    matrix_key1 = np.array(matrix_key)
    C = matrix_text1@matrix_key1
    for i in range(len(C)) :
        for j in range(len(C[i])) :
            C[i][j] = int(round(C[i][j] % 26))
    for i in range(len(C)) :
        for j in range(len(C[i])) :
            k = int(C[i][j])
            print(english_alphabet[C[i][j]],end='')
    return C


def decrypt(C,matrix_key):
    matrix_key_1 = np.array(matrix_key) #Ma tran khoa 
    C1 = np.array(C) #Ma tran da ma hoa
    det = np.linalg.det(matrix_key_1) #DInh thuc dung
    # Neu det khac 0 va det va 26 nguyen to cung nhau thi moi giai ma duoc
    if det != 0 and UCLN(int(det),26) == 1 :
        # Ma tran nghich dao
        matrix_key_pre = np.linalg.inv(matrix_key_1)
        for i in range(len(matrix_key_pre)) :
            for j in range(len(matrix_key_pre[i])) :
                matrix_key_pre[i][j] = (matrix_key_pre[i][j] * det) % 26
        det %= 26
        K_nghichDao = ((det**-1)%26 * (matrix_key_pre)%26) % 26
        # CHuoi goc 
        P = C1@K_nghichDao
        for i in range(len(P)) :
            for j in range(len(P[i])) :
                P[i][j] = int(round(P[i][j]))
        for i in range(len(P)) :
            for j in range(len(P[i])) :
                k = int(P[i][j])
                print(english_alphabet[k % 26],end='')
    else :
        print("Không thể giải mã")
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'

def menu() :
    print("1. Nhập nội dung và key:")
    print("2. Mã hoá chuỗi ")
    print("3. Giải mã chuỗi ")
    while True :
        choose = input("Nhập lựa chọn : ")
        if choose == '1' :
            plaintext = input("Nhập nội dung : ")
            key = list(map(int,input("Nhập chuỗi mã hoá: ").split(' ')))
            m = int(sqrt(len(key)))
            if m*m != len(key):
                print("Khong phai ma tran vuong")
            
            matrix_key = convertKeyToMatrix(key,m)
            matrix_text = convertToMatrix(plaintext,m)
        elif choose == '2':
            C = encrypt(matrix_key,matrix_text,m)
            print()
        elif choose == '3':
            decrypt(C,matrix_key)
            print()
        else :
            break
menu()
# key : 11 8 3 7