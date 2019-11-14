import math,string,egcd

def Find_ModInvKey(key,m):
    
    key_inv = egcd.egcd(key,m)

    return key_inv


def decrypt(ctext,key):

    let_num_map = {}
    num_let_map = {}
    num = 0
    letters_and_symbols = string.ascii_letters + string.digits + string.punctuation + " "

    lent=len(letters_and_symbols)

    inv_key = Find_ModInvKey(key,lent)

    for char in letters_and_symbols:

        let_num_map[num]=char
        num_let_map[char]=num
        num+=1

    num_map = {}
    cipher_symbols = {}

    for i in range(lent):

        num_map[i]=(i*inv_key)%lent
        cipher_symbols[(i*inv_key)%lent]=let_num_map[(i*inv_key)%lent]

    ptext = ""

    for letter in ctext:

        newNum=num_map[num_let_map[letter]]
        ptext+=cipher_symbols[newNum]

    print(ptext)

if __name__ == '__main__':

    cipher_text=input("Enter the text you want to decrypt: ")
    key=int(input("Enter the key used for decryption: "))
    decrypt(cipher_text,key)
